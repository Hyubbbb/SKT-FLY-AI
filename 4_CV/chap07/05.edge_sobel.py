import numpy as np, cv2

image = cv2.imread("Source/chap07/images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
    


  


cv2.imshow("edge- sobel edge", image)
cv2.imshow("dst1- vertical_OpenCV", dst1)
cv2.imshow("dst2- horizontal_OpenCV", dst2)
cv2.waitKey(0)