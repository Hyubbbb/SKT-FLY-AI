import cv2

def display_info(frame, text, pt, value, color=(120, 200, 90)): 
    text += str(value)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, pt, font, 0.7, color, 2)


capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))
print("대비 %d" % capture.get(cv2.CAP_PROP_CONTRAST))
print("채도 %d" % capture.get(cv2.CAP_PROP_SATURATION))

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받아오기
    if not ret:
        break  # 프레임 수신 오류시 종료
    if cv2.waitKey(30) >= 0:
        break
    
    # (200, 100) 좌표에서 100X200 크기의 영역 선택
    roi = frame[100:300, 200:400]
    # 녹색 성분 값 50 증가
    roi[:, :, 1] = cv2.add(roi[:, :, 1], 50)
    # 테두리를 두께 3의 빨간색으로 표시
    cv2.rectangle(frame, (200, 100), (400, 300), (0, 0, 255), 3)
    
    brightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)  # 밝기 속성
    contrast = capture.get(cv2.CAP_PROP_CONTRAST)  # 대비 속성
    saturation = capture.get(cv2.CAP_PROP_SATURATION)  # 채도 속성
    display_info(frame, "Brightness: ", (10, 40), brightness)
    display_info(frame, "Contrast: ", (10, 70), contrast)
    display_info(frame, "Saturation: ", (10, 100), saturation)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기

capture.release()
cv2.destroyAllWindows()