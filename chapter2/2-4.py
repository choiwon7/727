import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8) #img는 흰색으로 채워진 400x400짜리 컬러영상

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5) # (50,50)에서 시작해서 (200,50)으로 빨간색 5두께로 직선을 그리겠음
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

cv2.rectangle((img), (50,200,150,100),(0,255,0) , 2) #(50,200)에서 시작해서 가로로 150,세로로100정도의 사각형그리기
cv2.rectangle((img), (70,220),(180,280),(0,128,0),-1)#(70,220)부터 (180,280)까지 사각형을그림(위의 사각형의 내부) (음수를 채우면 내부를 채움)

cv2.circle((img), (300,100),30,(255,255,0),-1,cv2.LINE_AA)#(300,100)을 중심으로 반지름이 30인 원을 그림. cv2.LINE_AA:부드럽게 그려주고싶으면
cv2.circle((img), (300,100),60,(255,0,0),3,cv2.LINE_AA)

pts = np.array([[250,200],[300,200],[350,300],[250,300]]) #네개의 점을 2차원 행렬 np.array로 만듦 
cv2.polylines(img,[pts],True,(255,0,255),2,cv2.LINE_AA) #pts이용할때 리스트 형태로 감싸서 이용해야함.

text='Hello? Opencv' + cv2.__version__
cv2.putText(img,text,(50,350),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA) #(50,350)에 text출력하고 0.8배로 줄임


cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()