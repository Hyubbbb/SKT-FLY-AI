import numpy as np, cv2

image = cv2.imread('4_CV/chap08/images/perspective.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일을 읽기 에러")


pst1 = np.float32([(80, 40), (315, 133), (75, 300), (335, 300)]) # 입력 영상 좌표
pst2 = np.float32([(50, 60), (340,  60), (50, 320), (340, 320)]) # 목적 영상 좌표

perspect_mat = cv2.getPerspectiveTransform(pst1, pst2) # perspective transformation matrix(원근 변환 행렬)
dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1], cv2.INTER_CUBIC)
print(f'{perspect_mat} = perspect_mat')

cv2.imshow("image", image)
cv2.imshow("dst_perspective", dst)
cv2.waitKey(0)