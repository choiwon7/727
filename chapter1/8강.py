import sys
import glob
import cv2

img_files = glob.glob('.\\images\\*.jpg')  #현재 폴더 안에 있는 ~~.jpg파일을 모두 불러와

if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)  ##여기까지 전체화면으로 띄우기 성공

#첫번째 부터 다섯번째까지 다 보여주고 첫번째로 다시 돌아가기위한 작업
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])  #img를 불러오기 0번째 부터 불러옴

    if img is None:
        print('error')
        break

    cv2.imshow('image',img)  #image 창에 img 출력해라
    cv2.waitKey(1000)     #1초기다림

    if cv2.waitKey(1000) == 27: #만약에 ESC키를 눌렀으면
        break #while 루프를 빠져나옴
    
    idx += 1
    if idx >= cnt: #다시 첫번째로 돌아가기위한 작업
        idx=0

cv2.destroyAllWindows()
    