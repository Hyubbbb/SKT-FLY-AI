import numpy as np, cv2

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th2", "result")
    
    # OpenCV 이진화 함수 이용 - 상위값과 하위값 제거
    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)
    cv2.imshow("result", result)

image = cv2.imread("4_CV/chap06/images/color_space.jpg", 
                   cv2.IMREAD_COLOR) # 컬러 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

HSV_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 컬러 공간 변환
hue = np.copy(HSV_img[:, :, 0]) # Hue 채널

th = [50, 100] # 초기 임계값
# cv2.namedWindow("result")
cv2.namedWindow("result", cv2.WINDOW_NORMAL) # GPT

cv2.createTrackbar("Hue_th1", "result", th[0], 255, onThreshold)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, onThreshold) # Error
# cv2.createTrackbar("Hue_th2", "result", 0, 255, onThreshold) # 이렇게 실행하면 된다
print(th[0], th[1])

onThreshold(th[0]) # 이진화 수행
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()