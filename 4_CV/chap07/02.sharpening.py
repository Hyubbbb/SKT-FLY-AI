import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("4_CV/chap07/images/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# Filter code
def filter(image, mask):
    rows, cols = image.shape[:2] # 입력 행렬 크기
    dst = np.zeros((rows, cols), np.float32) # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2 # 마스크 중심 좌표
    
    for i in range(ycenter, rows - ycenter): # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1 # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1 # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32") # 관심영역 형변환
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst # 자료형 변환하여 반환

# 샤프닝 마스크 원소 지정 
data1 = [0, -1, 0,
         -1, 5, -1,
         0, -1, 0] # 1dimensional list
data2 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]] # 2dimensional list

mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32)

sharpen1 = filter(image, mask1) # 회선 수행 - 행렬 처리 방식
sharpen2 = filter(image, mask2) # 회선 수행 - 행렬 처리 방식
sharpen1 = cv2.convertScaleAbs(sharpen1) # 윈도우 표시를 위한 형변환
sharpen2 = cv2.convertScaleAbs(sharpen2) 


cv2.imshow("image", image)
cv2.imshow("sharpen1", cv2.convertScaleAbs(sharpen1))  # 윈도우 표시 위한 형변환
cv2.imshow("sharpen2", cv2.convertScaleAbs(sharpen2))
cv2.waitKey(0)