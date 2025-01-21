import numpy as np, cv2
# import matplotlib.pyplot as plt

image = cv2.imread("4_CV/chap06/images/draw_hist.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 히스토그램 계산
hsize, ranges = [32], [0, 256] # 히스토그램 간격수, 값 범위
hist_opencv = cv2.calcHist([image], [0], None, hsize, ranges) # OpenCV 함수

# 히스토그램 출력
print("OpenCV 함수: \n", hist_opencv.flatten()) # 행렬을 벡터로 변환하여 출력

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()