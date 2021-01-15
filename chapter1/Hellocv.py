#5강


import sys 
import cv2


print('Hello opencv', cv2.__version__)

img = cv2.imread('cat.bmp')    #imread = (이미지를 불러오는 함수 (파일이름 , 이미지를 읽는 방법설정))

if img is None :
    print('Image load failed!') #영상을 못 불러왔을때
    sys.exit()

cv2.namedWindow('image')        #opencv에서 지원하는 창을 생성해주는 함수 (image라는 이름을 가진 창을 만듦)
cv2.imshow('image' , img)       #창에다가 영상 데이터를 보여주는 함수 (어떤창에 (image),어떤영상을 보여줄거?(img))
cv2.waitKey()                   #키보드 입력을 기다리면서 동시에 영상이 화면에 보여지게함

cv2.destroyAllWindows()  #화면에 있는 모든 창을 닫아라.