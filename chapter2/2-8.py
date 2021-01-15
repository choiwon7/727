import numpy as np
import cv2

#픽셀값

def on_level_changed(pos):
    global img
    
    #img[:,:] = pos*16     #끝값은 검정색이다. 255보다 큰 값이라서(256) --->변수지정)
    level = pos * 16
    if level >=255:
        level = 255
    
    img[:,:] = level
    cv2.imshow('image',img)


img = np.zeros((480, 640), np.uint8)  #zeros : 픽셀 0


#createTrackbar는 무조건 창이 생성된 이후에 사용해야한다.


cv2.imshow('image', img)

#트랙바 작성

cv2.createTrackbar('level' , 'image' , 0,16,on_level_changed) #on_level_changed:콜백함수이름
 
cv2.waitKey()
cv2.destroyAllWindows()
