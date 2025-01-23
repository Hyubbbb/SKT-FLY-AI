import cv2
import numpy as np
import pytesseract
from PIL import Image

# Tesseract 실행 파일 경로 설정
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
# /opt/homebrew/Cellar/tesseract/5.5.0
# TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe" #테서렉스 설치 경로

imgpath='4_CV/chap08/proj/images/3.JPG'  #이미지 파일 경로
win_name = "Image To Text"  #OpenCV 창 이름
img = cv2.imread(imgpath)   #이미지 읽어오기

if img is None:
    raise FileNotFoundError(f"이미지 파일을 찾을 수 없습니다: {imgpath}")

korean_data_path = '/opt/homebrew/Cellar/tesseract/5.5.0/tessdata/'

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding to preprocess the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# apply median blurring to remove noise
thresh = cv2.medianBlur(thresh, 3)

text = pytesseract.image_to_string(thresh, lang='kor+eng', config=f'--tessdata-dir "{korean_data_path}"')

print(text)

# # 마우스 이벤트 처리 함수
# def onMouse(event, x, y, flags, param):

#     return 0



# # 이미치 처리 함수
# def ImgProcessing():
    
#     return 0


# # OCR 함수
# def GetOCR():
#     #이미지 불러오기
#     global img

#     #OCR모델 불러오기
#     pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

#     #OCR모델로 글자 추출
#     text = pytesseract.image_to_string(img, lang='kor+eng')
        
#     return text


# cv2.imshow(win_name, img)   #이미지 출력
# cv2.waitKey(0)              #입력 대기
# text = GetOCR()             #OCR함수로 텍스트 추출
# print(text)                 #텍스트 출력