import cv2
from Common.utils import put_string

capture = cv2.VideoCapture("4_CV/chap04/images/video_file.avi")	   # 동영상 파일 개방
if not capture.isOpened(): raise Exception("동영상 파일 개방 안됨")		# 예외 처리

frame_rate = capture.get(cv2.CAP_PROP_FPS)           		# 초당 프레임 수
delay = int(1000 / frame_rate)                         		# 지연 시간
frame_cnt = 0                                       		# 현재 프레임 번호

while True:
    ret, frame = capture.read()                     # 다음 프레임 읽기
    if not ret or cv2.waitKey(delay) >= 0: break	# 프레임 읽기 실패시 종료
    
    blue, green, red = cv2.split(frame)              # 채널 분리
    frame_cnt += 1
    
    if 100 <= frame_cnt < 200:	 cv2.add(blue, 100, blue) 	 # 100 ~ 200번째 프레임
    elif 200 <= frame_cnt < 300: cv2.add(green, 100, green)  # 201 ~ 300번째 프레임
    elif 300 <= frame_cnt < 400: cv2.add(red, 100, red)		 # 301 ~ 400번째 프레임
    
    frame = cv2.merge( [blue, green, red] )                  # 단일채널 영상 합성
    put_string(frame, "frame_cnt : ", (20, 30), frame_cnt)
    cv2.imshow("Read Video File", frame)

capture.release()