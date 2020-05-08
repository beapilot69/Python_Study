import cv2
from cv2 import cv2

cap = cv2.VideoCapture(0) # 0을 아규먼트로 비디오 객체를 생성

fourcc = cv2.VideoWriter_fourcc(*'XVID') #아래 아규먼트에 선언된 비디오 코덱을 선언해줌
writer = cv2.VideoWriter('output.avi',fourcc, 30.0, (354, 472))  #비디오 파일을 저장. 아규먼트(파일이름, 동영상저장시 사용되는 코덱, 초당 프레임, 영상의 크기(캡쳐되는 이미지 크기와 일치시켜야함))


while(True):    #캡쳐를 무한번 반복 = 영상을 출력
    ret, img_color = cap.read()  # 비디오 캡쳐객체의 리드함수를 호출하여 카메라로부터 이미지 한 장을 가져옴

    if ret == False:    #캡쳐가 되지 않은 경우 루프를 첫줄부터 다시시작
        continue #간혹 처음에 캡쳐되지 않는 캠이 있기때문에 해주는 것
    
    # 컬러이미지로 인한 영상을 그레이스케일로 출력해보자
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) 
    #루프가 실행되면서 CVTCOLOR함수의 첫번재 아규먼트인 컬러이미지가 계쏙 새로운 이미지로 변경되기 때문에 그레이스케일이미짇 계속 새로운 이미지가 돼서 영상으로 보이게 됨

    cv2.imshow('Color', img_color)
    cv2.imshow("Gray", img_gray)

    writer.write(img_color)  #카메라로 부터 캡쳐된 이미지를 반복적으로 저장하여 동영상을 만든다.

    if cv2.waitKey(1)&0xFF == 27:    #esc누르면 탈출, 키보드 입력까지 1초를 기다리겠다
        break

cap.release()
writer.relaese()   #사용이 끝난 비디오 라이터 객체의 자원을 해제
cv2.destroyAllWindows()
