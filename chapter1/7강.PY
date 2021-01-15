#컬러영상
#cv2.imread()는 BGR순서이고   Matplotilb는 RGB로 인식 RGB순서로 변경해야함--->cv2.cvtColor()함수 이용

#그레이스케일 영상
#plt.imshow()함수에서 컬러맵을 cmap(colormap)='gray'로 지정 

import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('cat.bmp')    #--->컬러 순서가 BGR
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) #--->cvtColor 함수를 이용해서 BGR을 RGB순서로 바꿈

plt.axis('off')        #off를 안하면 xy축이 생김.
plt.imshow(imgRGB)     #RGB순서로 되어있는걸 이용해야함. 변수 지정안하고 plt.imshow(imgBGR, cv2.COLOR_BGR2RGB)해도 된다.
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)               #subplot(여러영상을 하나의 창에 표현하고싶을때) : 1행에 표현 2열로 나누고 1열에 그림 그려라. 
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray') #subplot : 1행에 표현 2열로 나누고 2열에 그림 그려라. 
plt.show()
