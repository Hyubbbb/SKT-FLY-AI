import numpy as np, cv2


image = cv2.imread("chap07/images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [0, 1, 0,                                               # 마스크 선언 및 초기화
        1, 1, 1,
        0, 1, 0]

mask = 
th_img = 

dst2 = 
# dst2 = cv2.morphologyEx(th_img, cv2.MORPH_ERODE, mask)         # OpenCV의 침식 함수

cv2.imshow("image", image)
cv2.imshow("binary image", th_img)
cv2.imshow("OpenCV erode", dst2)
cv2.waitKey(0)