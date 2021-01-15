#※모르는 함수가 있을때는 구글에 opencv (내용)입력하기※
#https://docs.opencv.org/master/


#import sys
#import numpy as np
#import cv2



#chapter 1 함수

#sys모듈 : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있도록 해주는것.

'''
sys.argv : 명령 행에서 인수 받은 내용 출력해주는것
sys.exit : 강제 스크립트 종료 



cv2.imread(파일이름 , 플래그(옵션)(cv2.IMREAD_)) : 영상파일 불러오기
옵션은 주로 color(BGR컬러 영상으로 읽기) grayscale(흑백으로 읽기) unchanged(영상그대로 읽기) 이용 
연산이 제대로 되는지 확인하는 코드 작성해주기.(if문)

cv2.imwrite(저장할 파일이름(확장자 선택가능) , 저장할 영상 데이터 , 옵션(속성&값의 정수 쌍)) : 영상파일 저장하기
#옵션예시 = cv2.IMWRITE_JPEG_QUALITY,90 : JPG파일 압축률을 90%로 지정

cv2.namedWindow (창의 이름,옵션)
옵션 : cv2.WINDOW_NORMAL : 영상크기를 창 크기에 맞게 지정 ,cv2.WINDOW_AUTOSIZE : 창 크기를 영상 크기에 맞게 변경(마우스로 크기 조절가능)

cv2.destroyWindow(닫고자하는 창 이름) 
cv2.destroyAllWindows()
destroyWindow()는 닫고자하는 창 만 닫음 하지만 destroyAllWindows()는 모든 창을 다 닫는다.

cv2.moveWIndow(창 이름,x,y) : x와y좌표로 이동시키기.

cv2.resizeWindow(창 이름, 창의 가로크기, 창의 세로크기) : 창 크기 조절하기
(cv2.WINDOW_NORMAL 속성으로 창을 생성해야한다.)

cv2.imshow(창 이름, 출력할 영상 데이터) : 영상 출력하기
영상 데이터는 uint8타입을 사용해야함. 
ctrl+s = png형태로 파일저장 ctrl+c = 복사
cv2.namedWindow 없이도 사용할 수 있다(WINDOW_AUTOSIZE)
무조건 cv2.waitKey()가 있어야함.

cv2.waitKey() : 키보드 입력 대기 및 영상을 화면에 출력해주는 역할
cv2.waitKeyEX() : 키보드 특수키 입력 처리하기 (f1,f2,Home등등)
cv2.waitKey(시간(ms)) 
특정 키를 입력했을때 프로그램을 닫게 할 수 있음.
While True:
    if cv2.waitKey()==27(특정숫자)
        break
ESC(27) ENTER(13) TAP(9)
특정 키 입력값을 알고싶으면 ord()이용

cv2.cvtColor(src(색바꿀이미지),code(코드))(imread(BGR)------> Matplotlib(RGB))
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)(img_color영상을 color에서 grayscale로 바꿈)


특정 폴더에 있는 이미지 파일(jpg)목록 읽기
os.listdir() : 모든 파일목록 불러올 수 있음
glob.golb() : 특정 패턴의 문자열 형태의 파일을 모두 불러올 수 있음.

setWindowProperty : 창을 전체화면으로 띄우기

round : 반올림 함수

write : 문자열을 파일에 쓰게 해줄 수 있음.

format : 문자열에 어떤 값을 개입시킬 수 있음.

'''


#chapter2 함수

'''
영상 속성과 픽셀 값

nidm : 차원수 (len(img.shape))와 같음

shape : 각 차원의 크기(h , w) : grayscale
                  (h , w , 3) : color
size : 전체 원소 개수


dtype : 원소 데이터 타입 (영상데이터는 uint8)

영상 생성 복사 부분 영상 추출
np.empty(shape , dtype = np.unit8) : 임의의 값으로 초기화된 배열 생성

np.zeros(shape , dtype = np.uint8) : 0으로 초기화된 배열 생성

np.ones (shape , dtype = np.uint8) : 1로 초기화된 배열 생성

np.full(shape , fill_value , dtype = np.uint8) : fill_value로 초기화된 배열 생성
img4 = np.full((240,320) , 128 , dtype = np.uint8) 

a : img1 = img2
b : img3 = img1.copy 
a와 b의 차이점 : a는 참조, b는 대입

OpenCV 그리기 함수

Opencv에서 그리기 함수 이용할때 영상의 픽셀값이 바뀌기 때문에 복사본 만들기.
grayscale 영상에서는 color로 그리기가 되지 않기때문에 cv2.cvtColor()함수로 BGR컬러 영상으로 변환후 그리기 함수 호출

cv2.line(img(그림그릴영상),pt1(시작점),pt2(끝점),color(선 색상(BGR)튜플 or 정수값),thickness(선두께),
             lineType(선타입 cv2.LINE_4,cv2.LINE_8,cv2.LINE_AA 중 선택),shift(그리기 좌표 값의 축소비율(일반적케이스는 0))
         : 직선그리기
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)  # (50,50)에서 시작해서 (200,50)으로 빨간색 5두께로 직선을 그리겠음


1.cv2.rectangle(img(그림그릴영상),pt1,pt2(사각형의 두 꼭짓점 좌표(x1,y1(튜플)),color(선 색상(BGR)튜플 or 정수값),thickness(선두께)(기본값1,음수(-1)은 내부색 채움),
             lineType(선타입 cv2.LINE_4,cv2.LINE_8,cv2.LINE_AA 중 선택),shift(그리기 좌표 값의 축소비율(일반적케이스는 0))       


2.cv2.rectangle(img(그림그릴영상),rec(사각형 위치정보(x,y,w,h(튜플)),color(선 색상(BGR)튜플 or 정수값),thickness(선두께(기본값1,음수(-1)은 내부색 채움),
             lineType(선타입 cv2.LINE_4,cv2.LINE_8,cv2.LINE_AA 중 선택),shift(그리기 좌표 값의 축소비율(일반적케이스는 0))
         : 사각형 그리기


cv2.circle(img(그림그릴영상),center(중심좌표(x,y)(튜플)),radius(반지름),color(선 색상(BGR)튜플 or 정수값),thickness(선두께(기본값1,음수(-1)은 내부색 채움),
             lineType(선타입 cv2.LINE_4,cv2.LINE_8,cv2.LINE_AA 중 선택),shift(그리기 좌표 값의 축소비율(일반적케이스는 0))
         : 원 그리기
         
         
cv2.polylines(img(그림그릴영상),pts(꼭짓점 좌표(기억해서 사용하기)(np.array형태)),isClosed(폐곡선여부(True or False)), color(선 색상(BGR)튜플 or 정수값),thickness(선두께(기본값1,음수(-1)은 내부색 채움),
             lineType(선타입 cv2.LINE_4,cv2.LINE_8,cv2.LINE_AA 중 선택),shift(그리기 좌표 값의 축소비율(일반적케이스는 0))
         : 다각형 그리기


cv2.putText(img(그림그릴영상),text(출력할 문자열),org(문자열의 좌측 하단 좌표),fontFace(폰트종류),fontScale(폰트크기), color(선 색상(BGR)튜플 or 정수값),thickness(선두께(기본값1,음수(-1)은 내부색 채움),
             lineType(선타입 cv2.LINE_4,cv2.LINE_8,cv2.LINE_AA 중 선택),bottomLeftOrigin()


cv2.VideoCapture(index(정수값(숫자0은 기본카메라를 열음),apiPreference) : 카메라 열기

#기본 카메라 열기 : cv2.VideoCapture(0)

#isOpened : 카메라가 잘 열렸는지 확인 (if와 사용)
if not cap.isOpened():         카메라가 열리지 않으면 (isOpend) 아래문장 실행 (cap : 변수이름)
    print('camera open failed!')
    sys.exit()


#release : 사용한 자원 해제

※※※※※※※※※※※※※※※※※※※※※※※※※※※※중요※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※

read : 프레임을 받아오는 함수 (Bul , fps) 
 
while True:                   while문을 돌면서 한 프레임씩 받아오는 작업
    ret , frame = cap.read()  프레임을 받아오는 함수(열려있는 카메라로 부터 한 프레임씩 받아오는 작업실행)
                              read 함수는 프레임을 받아오는것뿐만아니라 잘 받고있는지 True False같은 bul 타입도 지님.
                              따라서 변수를 두개 지정해야함 (bul , frame).

    if not ret:               ------->카메라가 열리지 않으면 실행종료
        break
※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※

cv2.VideoCapture(파일이름) : 동영상 열기

cv2.Canny : 윤곽선이 보이게 나타냄
cv2.Canny(frame, 50, 150)  : frame : 이미지 이름 , 50 150 : 각각 최소 최대 스레숄드



#프레임창 조절하기 
set(cv2.CAP_PROP_FRAME_WIDTH,320)    
set(cv2.CAP_PROP_FRAME_HEIGHT,240)


#카메라 프레임 받아오기
get(cv2.CAP_PROP_FRAME_WIDTH)       
get(cv2.CAP_PROP_FRAME_HEIGHT)





cv2.VideoWriter(파일이름,fourcc,fps(초당프레임수),frameSize(프레임크기(튜플형식)),isColor(bul형식) : 프레임 동영상을 저장할 수 있음.
isColor의 기본값은 True 컬러영상을 저장하는용도임. grayscale로 저장하기위해서는 color포멧으로 변환(cvtColor이용)해서 저장해야함.
예시 : out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

fourcc(4문자코드) : 동영상 파일의 코덱,압축방식,색상,픽셀 포맷 등을 정의하는 정수 값
DIVX 
XVID
FMP4
X264
MJPG

inversed = ~frame  : 프레임 반전코드

cv2.setMouseCallback((처리할 창 이름),(onMouse(마우스 이벤트 처리를 위한 콜백 함수 이름(onMouse(event , x, y , flags, param)))),param(콜백함수에 전달할 데이터))
setMouseCallback함수는 호출할 창 이름이 있을때 써야함.

콜백함수 형식 : onMouse((onMouse(event , x, y , flags, param)))
event : 마우스 이벤트 종류 cv.EVENT_로 시작하는 상수 (event를 이용할때는 ==사용)
x,y : 마우스 이벤트 발생 장소           
flags : 마우스 이벤트 발생 시 상태. cv2.EVENT_FLAG_로 시작하는 상수 (flags는 &사용하는게 좋음)
param : cv2.setMouseCallback() 함수에서 설정한 데이터.


트랙바 : 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤

cv2.createTrackbar(trackbarName, windowName, value , count , onChange)
trackbarName : 트랙바 이름
windowName : 트랙바를 생성할 창 이름
value : 트랙바 위치 초기값 
count : 트랙바 최대값 (최솟값은 0임)
onChange : 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름 (onChange(pos)형식)

###############255를 넘어가면 검정색으로 바뀌어서 코드를 작성해줘야함.################

def on_level_changed(pos):
    global img
    
    #img[:,:] = pos*16         
    # level = pos * 16
    if level >=255:
        level = 255

연산시간 측정
cv2.TickMeter() --->tm

tm : cv2.TickMeter객체
tm.start() : 시간측정 시작
tm.stop()  : 시간측정 끝
tm.reset() : 시간 측정 초기화

예시:

import numpy as np
import cv2

img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()
tm.start()                   #시간측정 시작

edge = cv2.Canny(img , 50 , 150)

tm.stop()                    #시간측정 끝

print('Elapsed time : {} ms.' , format(tm.getTimeMilli(())))     # 측정시간 밀리 초 단위


2-10에 동영상 합성하는 코드 있음 참조할것.
























