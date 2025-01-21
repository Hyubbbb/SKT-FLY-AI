import cv2

def print_matInfo(name, image):
    if image.dtype == 'uint8':     mat_type = "CV_8U"
    elif image.dtype == 'int8':    mat_type = "CV_8S"
    elif image.dtype == 'uint16':  mat_type = "CV_16U"
    elif image.dtype == 'int16':   mat_type = "CV_16S"
    elif image.dtype == 'float32': mat_type = "CV_32F"
    elif image.dtype == 'float64': mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    ## depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type,  nchannel))

# 새로운 윈도우의 이름
title1, title2 = "16bit Image", "32bit Image" # 윈도우 이름
image16bit = cv2.imread("4_CV/chap04/images/read_16.tif", cv2.IMREAD_UNCHANGED)
image32bit = cv2.imread("4_CV/chap04/images/read_32.tif", cv2.IMREAD_UNCHANGED)

if image16bit is None or image32bit is None:
    raise Exception("영상파일 읽기 에러")


# 새로운 화소의 위치
pixel_pos = (20, 20)

# 행렬 내 한 화소 값 표시
print("16/32비트 영상 행렬 좌표 (20, 20) 화소값")
print(title1, "원소 자료형 ", type(image16bit[pixel_pos][0])) # 원소 자료형
print(title1, "화소값(3원소) ", image16bit[pixel_pos]) # 행렬 내 한 화소 값 표시
print(title2, "원소 자료형 ", image32bit[pixel_pos][0])
print(title2, "화소값(3원소) ", image32bit[pixel_pos])
print()

# 행렬 정보 출력
print_matInfo(title1, image16bit)
print_matInfo(title2, image32bit)

cv2.imshow(title1, image16bit)
cv2.imshow(title2, (image32bit*255).astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()