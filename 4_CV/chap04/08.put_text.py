import numpy as np
import cv2

# Define colors
olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
blue, red = (255, 0, 0), (0, 0, 255)

# 문자열 위치 좌표
pt1, pt2 = (50, 150), (50, 250)

# 3채널 컬러 영상 생성 및 초기화: 흰색 배경
image = np.zeros((400, 600, 3), np.uint8)
image.fill(255)

# 텍스트 출력
cv2.putText(image, "HELLO", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, blue, 2)
cv2.putText(image, "WORLD", (50, 200), cv2.FONT_HERSHEY_DUPLEX, 2, red, 2)
cv2.putText(image, "OPEN CV", pt1 ,cv2.FONT_HERSHEY_TRIPLEX, 3, violet, 2)
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC # 글자체 상수
cv2.putText(image, "PYTHON", pt2, fontFace, 3, olive, 2)

# 윈도우에 영상 표시
cv2.imshow("Put Text", image)
cv2.waitKey(0) # 키 이벤트 대기
cv2.destroyAllWindows() # 윈도우 제거