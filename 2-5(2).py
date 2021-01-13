import sys
import cv2

#카메라를 연담에 영상을 비디오로 저장하기 , opencv는 소리는 재생이 안된다. 영상만 저장 가능.

cap = cv2.VideoCapture(0)  #기본카메라 오픈           

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #round : 반올림 함수
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) #프레임수 정하기. (카메라 성능에 따라 fps =30 이렇게 강제로 써줘도 괜찮음.)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X' #코덱 지정함.
delay = round(1000 / fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h)) #비디오 이름 : outpput.avi , 압축방식:fourcc(DIVX),fps.프레임 크기

if not out.isOpened():           #제대로 오픈 되지 않았을경우
    print('File open failed!')
    cap.release()
    sys.exit()

while True:                      #--------------------------------
    ret, frame = cap.read()
                                 #카메라에서 프레임 받아오는 코드
    if not ret:
        break                    #---------------------------------

    inversed = ~frame            #프레임 반전 코드
     
    '''edge = cv2.Canny(frame,50,150) # edge는 grayscale로 저장되갖고 color로 바꿔줘야함
    edge_color = cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR) #gray영상을BGR로 변환해라(컬러로 변환시킴)
    out.write(edge_color)'''
    out.write(inversed)

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
