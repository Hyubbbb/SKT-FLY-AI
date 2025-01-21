import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("Source/chap06/images/draw_hist.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")
    
hist = cv2.calcHist()
hist_img = draw_histo(hist)


# 히스토그램 그리기 (OpenCV 함수를 사용하여 이미지에 그리기)
hist_img = np.full((200, 256), 255, np.uint8)
cv2.normalize(hist, hist, 0, 200, cv2.NORM_MINMAX)

for x in range(256):
    cv2.line()


cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.waitKey(0)

# 히스토그램을 matplotlib을 사용하여 그리기

