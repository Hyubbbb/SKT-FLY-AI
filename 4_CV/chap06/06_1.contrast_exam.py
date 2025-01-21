import numpy as np, cv2

image1 = cv2.imread("4_CV/chap06/images/add1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
image2 = cv2.imread("4_CV/chap06/images/add2.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기

if image1 is None: raise Exception("영상 파일 읽기 오류 발생")
if image2 is None: raise Exception("영상 파일 읽기 오류 발생")


image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)  # 이미지 합성

# 영상 띄우기
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("image3: image1 + image2", image3)

cv2.waitKey(0)