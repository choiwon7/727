import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) 
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

#영상 크기 알려주기

print(type(img1))
print(img1.shape)    #grayscale는 2차원으로 잡힌다 (세로 , 가로 , 차원)
print(img2.shape)    #color은 3차원으로 잡힌다
print(img1.dtype)    #unit 8 이용
print(img2.dtype)    #unit 8 이용

h, w = img1.shape
print('w x h = {} x {}'.format(w, h))

h, w = img2.shape[:2]   # img2는 3차원이기 때문에 w,h만으로 나타낼 수 없기때문에 앞에 2개만 데려옴.
                        # img2.shape[:2] 영상의 세로, 가로 크기를 받아오는 일반적인 형태
print('w x h = {} x {}'.format(w, h))

if img1.ndim ==2:    #ndim : 차원을 알려줌 len(img1.shape) ==2:
    print('img1 is a grayscale image')

#영상 픽셀 불러오기
x = 20
y = 10
p1 = img1[y,x]   #img1 (10,20)의 위치의 픽셀값
print(p1)

p2 = img2[y,x]   #img2 (10,20)의 위치의 픽셀값(BGR)
print(p2) 

#픽셀값을 조절 할 수 있다.
img1[y,x] = 0          
img2[y,x] = (0,0,255)


'''모든 픽셀을 조절하고싶을때 for 이용   쓰지말기.

for y in range(h):
    for x in range(w)
        img1[y, x] =0
        img2[y, x] = (0,255,255)
'''

'''모든 픽셀 조절할때 
img1[:,:] = 0 #[:,:] : y좌표 전체, x좌표 전체
img2[:,:] = (0,255,255)
'''

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindows()
