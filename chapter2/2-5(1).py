import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture()   #기본카메라 open하겠다
cap.open(0)                #cap = cv2.VideoCapture(0)

if not cap.isOpened():        #카메라가 열리지 않으면 (isOpend) 아래문장 실행
    print('camera open failed!')
    sys.exit()

#카메라 장치 속성값(get ,set 이용(opencv에 더 많은거 있음))

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)       #카메라 프레임 받아오기
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)           
print(w,h)

#set이용할 수 도 있음

cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)    #프레임창 조절하기 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

#중요 부분

while True:                   #while문을 돌면서 한 프레임씩 받아오는 작업
    ret , frame = cap.read()  #프레임을 받아오는 함수(열려있는 카메라로 부터 한 프레임씩 받아오는 작업실행)
                              #read 함수는 프레임을 받아오는것뿐만아니라 잘 받고있는지 True False같은 bul 타입도 지님.
                              #따라서 변수를 두개 지정해야함 (bul , frame).
    if not ret:   
        break

    edge = cv2.Canny(frame, 50, 150)   #윤곽선이 저장된 edge영상(Canny)
    
    cv2.imshow('frame',frame) 
    cv2.imshow('edge', edge)
    #cv2.waitKey(20)          이렇게만 써주면 while문을 빠져나올 수 없음
    if cv2.waitKey(20) == 27: #ES C
        break
cap.release()                 #사용한것 해제
cv2.destroyAllWindows

#동영상 파일 만들기

''' cap = cv2.VideoCapture(video1.mp4(파일이름)) #위 코드에다가 파일이름 넣어주기
카메라 세팅 제외시키기