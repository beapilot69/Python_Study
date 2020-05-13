import cv2
from cv2 import cv2

def nothing(x):    # 더미함수를 정의 사용하진 않지만 트랙바 생성에 필요
    pass

cv2.namedWindow('Binary') #트랙바를 붙일 윈도우를 네임드윈도우함수로 생성해주어야한다
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)  #트랙바를 이름이 바이너리인 윈도우에 붙인다. 조정가능한 값 0~255)
cv2.setTrackbarPos('threshold', 'Binary', 119)     # 초기값을 127로 설정

img_color = cv2.imread('C:/project/yoon.jpg')

cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

while(True): #트랙바 이용시 결과를 바로 확인할 수 있도록 루프를 추가 트랙바 현재값 가져와서 스레시홀드 임계값으로 사용하도록 수정해준다. (low를 추가 + esc누르면 루프 빠져나오도록해줌)
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret,img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)   # threshold함수의 첫번째 아규먼트는 이진화할 이미지파일 대상(그레이스케일이어야함), 두번째 쓰레스홀드(이것을 기준으로 결과이미지가 흰색/검정색 결정), 네번째 트레시바이너리인 경우 쓰레시홀드보다 입력이미지 픽셀이 클 때 세번째 아규먼트로 지정된 255를 결과이미지의 픽셀값으로 함. 작다면 0을 픽셀값으로 함.
    cv2.imshow("Binary", img_binary)

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('Result', img_result)
    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()