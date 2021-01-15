import sys
import numpy as np
import cv2


img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

#이 코드는 i키를 두번 눌러야 반전이 된다 (if 와 elif에서 한번한번씩 두번)

'''while True:
    if cv2.waitKey() ==27:
        break
    
    elif cv2.waitKey() == ord('i'):
        img = ~img # ~ : 비트연산자(픽셀값을 255에서 뺀값으로 처리해줌) 
        cv2.imshow('image',img) 
    '''
while True:
    key = cv2.waitKey()             # i 키 한번만 하려면 변수 지정해줘야함.
    if key == 27:
        break
    elif key == ord('i') or key == ord('I'):
        img = ~img
        cv2.imshow('image',img)

cv2.destroyAllWindows()