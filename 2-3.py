import sys
import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

cv2.copyTo(src,mask , dst) # src mask dst는 사이즈가 모두 같아야함.
                           # src와 dst는 타입이 같아야함(graysclae면 grayscale)
                           # mask는 무조건 grayscale 타입이어야 한다.


#투명한 png파일을 불러와서 합성하기

src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)   #png 파일 불러오기위해 UNCHANGED사용해야함.
       #shape가 4갠데 4개는 컬러값이고 한개는 mask값으로 사용할 수 있음

mask = src[:,:,-1]
src = src[:,:,0:3]
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

#cv2.copyTo(src,mask , dst)코드 쓰면 안됌 (크기가 다름)

h,w = src.shape[:2]

crop = dst[10:h+10 , 10:w+10]  #crop는 dst의 일부분인데 픽셀값을 공유함. (10픽셀 띄우기)

cv2.copyTo(src, mask, crop)



cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용 

