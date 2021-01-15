import numpy as np
import cv2


# 새 영상 생성하기
'''img1 = np.empty((240, 320), dtype=np.uint8)       # grayscale image
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    # color image (zeros: 모든픽셀0)
img3 = np.ones((240, 320,3), dtype=np.uint8) *255   # dark gray (ones:모든픽셀1) (*255하면 모든픽셀에 255를 곱함 따라서 흰색)
img4 = np.full((240, 320), 128, dtype=np.uint8)   # (full : fill values 값으로 초기화시켜줌)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()'''


#영상 불러오기
'''img1 = cv2.imread('HappyFish.jpg')

img2 = img1  #img1과 img2가 같은 코드를 쓴다(참조)
img3 = img1.copy() #img3과 img1은 복사코드 (대입) img1이 어떻게 바뀌던 상관없음

img1[:,:] = (0,255,255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()'''

#부분 영상 출력하기(슬라이싱 방법 이용)

img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120 , 30:150] #(40~120행 , 30~150열)
img3 = img1[40:120 , 30:150].copy() 

img1[:,:] = (0,255,255)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
