import sys
import numpy as np
import cv2

oldx = oldy = -1

def on_mouse(event,x,y,flags,param):      #무조건 5개의 인자를 갖고있어야함(안써도 써줘야함)
    global img, oldx, oldy   #img , oldx , oldy변수를 쓰겠다.

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx , oldy = x,y #왼쪽 버튼이 눌렸을때 oldx와 oldy를 x,y좌표로 세팅함.
        print('EVENT_LBUTTONDOWN: {},{}'.format(x,y)) #마우스 왼쪽 버튼을 누르면 그쪽에서의 좌표가 나오도록 함
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: {},{}'.format(x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:          #마우스를 누를때 아래 코드(#부분) 실행(이 코드 없음 마우스 움직이기만해도 좌표나옴)
            #print('EVENT_MOUSEMOVE: {},{}'.format(x,y))

            #마우스로 그리기
            #cv2.circle(img,(x,y),5 (0,0,255),-1)    #마우스가 빠르게 움직이면 놓치는 부분 생김 --> line 함수 이용.
            cv2.line(img,(oldx,oldy),(x,y),(0,0,255),5,cv2.LINE_AA)
            cv2.imshow('image',img)
            oldx,oldy=x,y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255       #픽셀이1인 컬러 영상에 255를 곱함 

#cv2.setMouseCallback()  이 위치에 setMouseCallback을 실행하면 안된다. 창이 미리 떠 있어야함. namedWindow or imshow 뒤에 있어야함.
cv2.imshow('image', img)
cv2.setMouseCallback('image',on_mouse)
cv2.waitKey()

cv2.destroyAllWindows()


#16.08
