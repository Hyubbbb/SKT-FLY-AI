import cv2

image = cv2.imread("4_CV/chap04/images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 50) # JPEG 화질 설정 (50%)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 5] # PNG 압축 레벨 설정 (0~9)

## 행렬을 영상 파일로 저장
cv2.imwrite("4_CV/chap04/output_images/high_quality.jpg", image) # 최고 화질로 저장 
cv2.imwrite("4_CV/chap04/output_images/medium_quality.jpg", image, params_jpg) # 중간 화질로 저장
cv2.imwrite("4_CV/chap04/output_images/medium_compression.png", image, params_png) # 중간 압축률로 저장
cv2.imwrite("4_CV/chap04/output_iamges/image_output.bmp", image) # BMP 파일로 저장

print("저장 완료")