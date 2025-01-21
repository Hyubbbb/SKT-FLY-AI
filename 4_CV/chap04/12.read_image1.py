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

title1, title2 = "16bit Image", "32bit Image" # 윈도우 이름
image16bit  = cv2.imread(                                ) #  
image32bit = cv2.imread(                                )# 

if image16bit is None or image32bit is None:
    raise Exception("영상파일 읽기 에러")


# 행렬 내 한 화소 값 표시
print(title1, "원소 자료형 ", ) # 원소 자료형
print(title1, "화소값(3원소) ", ) # 행렬 내 한 화소 값 표시
print(title2, "원소 자료형 ", )
print(title2, "화소값(3원소) ", )

print_matInfo(title1, gray2gray)
print_matInfo(title2, gray2color)

cv2.imshow(title1, )
cv2.imshow(title2, )
cv2.waitKey(0)