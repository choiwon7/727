#연산 시간 측정 방법(TickMeter  ->tm )

import sys
import time
import numpy as np
import cv2


img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()  #tm 객체 생성

tm.reset()

tm.start()#------------------edge 함수 시간 측정 시작-----------------
t1 = time.time()
edge = cv2.Canny(img, 50, 150)
 
tm.stop()#-------------------------edge 함수 시간 측정 끝--------------------
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))