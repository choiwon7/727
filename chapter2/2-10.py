import sys
import numpy as np
import cv2


# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('video1.mp4')  
cap2 = cv2.VideoCapture('video2.mp4')

#예외처리 코드 작성해주기
if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) #1번 동영상 전체 프레임
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT)) #2번 동영상 전체 프레임
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)   #첫번째동영상의 끝부분 2초 , 두번째동영상의 앞부분 2초가 겹쳐져 합성이 되게 작성

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

delay = int(1000 / fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))  #동영상1 가로크기
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)) #동영상2 세로크기
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

#-----------동영상 이어 붙히기 시작-------------------

#첫번째 동영상
while True:
    ret1,frame1 = cap1.read()

    if not ret1 :
        break

    out.write(frame1)
    
    cv2.imshow('frame',frame1)
    cv2.waitKey(delay) #delay = int(1000 / fps) : 두 프레임 사이의 시간간격 계산한 수식

#두번째 동영상
while True:
    ret2,frame2 = cap2.read()

    if not ret2 :
        break

    out.write(frame2)
    
    cv2.imshow('frame',frame2)
    cv2.waitKey(delay)
#---------------------------동영상 이어붙히기 끝 --------------------------

#동영상 합성하기

for i in range(frame_cnt1 - effect_frames): # 1번동영상에서 뒤에 48프레임 정도 남겨두고 앞 부분은 output동영상에 저장
    ret1,frame1 = cap1.read()

    if not ret1 :
        break

    out.write(frame1)
    
    cv2.imshow('frame',frame1)
    cv2.waitKey(delay) #delay = int(1000 / fps) : 두 프레임 사이의 시간간격 계산한 수식

#합성하는 구간 : 1번 2번 동영상에서 프레임을 가져와야한다.
for i in range(effect_frames):
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()

    dx = int(w / effect_frames) * i

    frame = np.zeros((h , w, 3) , dtype=np.uint8)
    frame[:, 0:dx] = frame2[:, 0:dx]
    frame[:, dx:w] = frame1[:, dx:w]
    
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(delay)
    


for i in range(effect_frames,frame_cnt2): #2번동영상에서 앞에 48프레임 정도 남겨두고 뒷 부분은 output동영상에 저장
    ret2,frame2 = cap2.read()

    if not ret2 :
        break

    out.write(frame2)
    
    cv2.imshow('frame',frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
