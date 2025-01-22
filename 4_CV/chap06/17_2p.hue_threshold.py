import numpy as np
import cv2

# 트랙바 이벤트 콜백 함수
def onThreshold(value):
    try:
        # 트랙바 값 가져오기
        th[0] = cv2.getTrackbarPos("Hue_th1", "result")
        th[1] = cv2.getTrackbarPos("Hue_th2", "result")
        print(f"Trackbar values - Hue_th1: {th[0]}, Hue_th2: {th[1]}")  # 디버깅 출력

        # Threshold 적용
        _, temp_result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
        _, result = cv2.threshold(temp_result, th[0], 255, cv2.THRESH_BINARY)

        # 결과 출력
        cv2.imshow("result", result)
    except cv2.error as e:
        print(f"Error occurred: {e}")

# 이미지 읽기
BGR_img = cv2.imread("4_CV/chap06/images/color_space.jpg", cv2.IMREAD_COLOR)
if BGR_img is None:
    raise Exception("영상파일 읽기 오류")

# HSV 변환 및 Hue 채널 추출
HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)
hue = np.copy(HSV_img[:, :, 0])

# 초기 Threshold 값 설정
th = [50, 100]

# 윈도우 생성 및 트랙바 초기화
cv2.namedWindow("result")
cv2.createTrackbar("Hue_th1", "result", th[0], 255, lambda x: None)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, lambda x: None)

# 초기 출력
onThreshold(th[0])
cv2.imshow("BGR_img", BGR_img)

# 대기
cv2.waitKey(0)
cv2.destroyAllWindows()