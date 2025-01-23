import cv2
import dlib
from deepface import DeepFace
import numpy as np
from collections import deque
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import time

# 최근 예측값(감정, 성별, 시선 방향)을 저장하기 위해 deque를 초기화
emotion_deque = deque(maxlen=30)
gender_deque = deque(maxlen=5)
eye_gaze_deque = deque(maxlen=30)

detector = dlib.get_frontal_face_detector() # Dlib의 정면 얼굴 검출기
predictor = dlib.shape_predictor("4_CV/chap08/proj2/shape_predictor_68_face_landmarks.dat") # 68개 얼굴 랜드마크를 예측하는 모델

# 웹캠 연결 
def capture_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Unable to access the webcam.")
    return cap

def detect_faces_and_landmarks(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 프레임을 흑백 이미지로 변환
    faces = detector(gray) # 얼굴 검출
    landmarks = [predictor(gray, face) for face in faces] #  각 얼굴에 대해 랜드마크 추출
    return faces, landmarks



def analyze_face(face_image):
    ### START 모델 변경 파트 ###
    # # 모델 이름: "VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"
    # emotion_model = DeepFace.build_model("Facenet")
    # gender_model = DeepFace.build_model("Facenet")
    # age_model = DeepFace.build_model("Facenet")
    # ### END 모델 변경 파트 ###
    
    predictions = DeepFace.analyze(face_image, 
                                #    actions=['emotion', 'gender', 'age'], 
                                   actions=['emotion', 'gender', 'age', 'race'], 
                                   enforce_detection=False, # 얼굴 이미지에서 감정, 성별, 나이를 분석 (강제하지는 않았다.)
                                #    models={
                                #        "emotion": emotion_model,
                                #        "gender": gender_model,
                                #        "age": age_model
                                #        }
                                   ) 
    # print(predictions)  # 반환값 확인용
    
    # 리스트의 첫 번째 요소만 사용
    if isinstance(predictions, list):
        predictions = predictions[0]
    return predictions

# 감정 딕셔너리에서 가장 높은 값을 가진 감정을 선택
def measure_emotion_intensity(emotion_dict):
    sorted_emotions = sorted(emotion_dict.items(), key=lambda x: x[1], reverse=True)
    dominant_emotion = sorted_emotions[0][0]
    intensity = sorted_emotions[0][1]
    return dominant_emotion, intensity

def eye_gaze_estimation(landmarks):
    # 왼쪽 눈(36~41)과 오른쪽 눈(42~47)의 좌표 추출
    left_eye = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(36, 42)])
    right_eye = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(42, 48)])

    # 각 눈의 중심 계산
    left_center = np.mean(left_eye, axis=0)
    right_center = np.mean(right_eye, axis=0)

    # 시선 방향 계산 (예제: 단순히 두 눈 중심 비교)
    eye_gaze_direction = "Center"  # 기본값
    if left_center[0] < right_center[0] - 5:  # 왼쪽 시선
        eye_gaze_direction = "Left"
    elif left_center[0] > right_center[0] + 5:  # 오른쪽 시선
        eye_gaze_direction = "Right"

    return eye_gaze_direction


def smooth_predictions(gender, emotion, eye_gaze):
    gender_deque.append((gender, time.time()))
    emotion_deque.append((emotion, time.time()))
    eye_gaze_deque.append(eye_gaze)

    stable_gender = max(set(g[0] for g in gender_deque), key=(lambda g: [x[0] for x in gender_deque].count(g)))
    stable_emotion = max(set(e[0] for e in emotion_deque), key=(lambda e: [x[0] for x in emotion_deque].count(e)))
    stable_eye_gaze = max(set(eye_gaze_deque), key=eye_gaze_deque.count)

    return stable_gender, stable_emotion, stable_eye_gaze

# 시선 방향에 따라 결과를 텍스트로 반환
def determine_eye_gaze(eye_gaze_direction):
    if eye_gaze_direction == "Left":
        return "Looking Left"
    elif eye_gaze_direction == "Right":
        return "Looking Right"
    elif eye_gaze_direction == "Center":
        return "Looking Center"
    else:
        return "Unknown"

class FaceRecognitionApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.cap = capture_video()
        self.last_update_time = time.time()
        self.age = None  # Initialize age as None
        self.timer.start(10)

    def initUI(self):
        self.setWindowTitle('Real-Time Facial Recognition and Analysis')
        self.setGeometry(100, 100, 1280, 720)
        self.label = QtWidgets.QLabel(self)
        self.label.resize(1280, 720)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            faces, landmarks = detect_faces_and_landmarks(frame)

            for i, face in enumerate(faces):
                x, y, w, h = (face.left(), face.top(), face.width(), face.height())
                face_image = frame[y:y + h, x:x + w]

                try:
                    predictions = analyze_face(face_image)

                    # 예측값 추출
                    dominant_emotion = predictions['dominant_emotion']
                    emotion_intensity = max(predictions['emotion'].values())
                    gender = predictions['dominant_gender']
                    age = predictions['age']
                    dominant_race = predictions['dominant_race']

                    if i < len(landmarks):
                        eye_gaze_direction = eye_gaze_estimation(landmarks[i])
                    else:
                        eye_gaze_direction = "Unknown"

                    # 안정화된 예측값 계산
                    stable_gender, stable_emotion, stable_eye_gaze = smooth_predictions(gender, dominant_emotion, eye_gaze_direction)

                    # 프레임에 텍스트 및 사각형 추가
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(frame, f"Gender: {stable_gender}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(frame, f"Emotion: {stable_emotion}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(frame, f"Age: {age}", (x, y - 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(frame, f"Race: {dominant_race}", (x, y - 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(frame, f"Eye Gaze: {stable_eye_gaze}", (x, y - 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                except Exception as e:
                    print(f"Error processing face: {e}")

            self.display_frame(frame)

    def display_frame(self, frame):
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        qImg = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def closeEvent(self, event):
        self.cap.release()
        cv2.destroyAllWindows()
        event.accept()

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    face_recognition_app = FaceRecognitionApp()
    face_recognition_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
