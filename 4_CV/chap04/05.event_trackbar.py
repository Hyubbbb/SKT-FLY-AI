import numpy as np
import cv2

def onChange(value):												# 트랙바 콜백 함수
    global image                        	# 전역 변수 참조

    add_value = value - initial_value
    print("추가 화소값:", add_value)
                	
    image[:] = np.clip(image + add_value, 0, 255)  # 행렬과 스칼라 덧셈 수행, 화솟값 클리핑
    cv2.imshow(title, image)

initial_value = 127
image = np.full((400, 600), initial_value, np.uint8) # 영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar("Brightmness", title, initial_value, 255, onChange)	# 트랙바 콜백 함수 등록

cv2.waitKey(0)
cv2.destroyWindow(title)