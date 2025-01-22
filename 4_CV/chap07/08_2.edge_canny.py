# import numpy as np, cv2

# def on_trackbar(val):
#     # 트랙바에서 임곗값을 가져옴
    
#     low_threshold = cv2.getTrackbarPos('Low Threshold', 'Canny Edge Detection')
#     high_threshold = cv2.getTrackbarPos('High Threshold', 'Canny Edge Detection')
    
#     # Canny Edge Detection 적용
#     edges = cv2.Canny(gray, low_threshold, high_threshold)
    
#     # 결과 이미지 표시
#     cv2.imshow('Canny Edge Detection', edges)

# image = cv2.imread("4_CV/chap07/images/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
# if image is None: raise Exception("영상 파일 읽기 오류")

# # 그레이스케일로 변환
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # 윈도우 생성
# cv2.namedWindow('Canny Edge Detection')

# # 트랙바 생성
# cv2.createTrackbar('Low Threshold', 'Canny Edge Detection', 0, 1000, on_trackbar)
# cv2.createTrackbar('High Threshold', 'Canny Edge Detection', 0, 1000, on_trackbar)

# # 초기 임곗값 설정
# cv2.setTrackbarPos('Low Threshold', 'Canny Edge Detection', 50)
# cv2.setTrackbarPos('High Threshold', 'Canny Edge Detection', 150)

# # 초기 Canny Edge Detection 수행
# on_trackbar(0)

# # 키 입력 대기
# cv2.waitKey(0)
# cv2.destroyAllWindows()