##빠른시간 기차 예매 프로그램
##원하는 열차 정보와 시간를 입력하면 가장 가까운 시간대에 열차를 출력하며, 예매를 진행하는 프로그램을 코딩하시오.

f = open("C:/project/Study/E-on/TrainList.txt",'r')     #f에 TrainList 파일을 저장함
a = []
while breakpoint: #모든 줄을 읽어서 출력
    line = f.readline()
    if not line: break  #더이상 읽을 줄이 없으면 
    myline = a.append(line.split(' '))
f.close()

# for i in range(1, len(a)):      #잔여 좌석수 정수로 출력
#     print(int(a[i][5]))

t_dep = 0           #출발시간
station_dep = 0     #출발역
station_arr = 0     #도착역
train = 0           #열차 종류
seat_remain = 0     #잔여석

menu = int(input('menu: '))  #메뉴 입력

# def write():
# def printing():
# while True:
if menu == 1:
    # 정보 입력
    t_dep = input('원하는 출발 시간을 입력하세요 ex)0605: ')
    station_dep = input('출발역을 입력하세요: ')
    station_arr = input('도착역을 입력하세요: ')
    train = input('열차 종류를 입력하세요: ')
    
    # 입력 시간과 가장 가까운 시간대에 열차 정보와 잔여석 출력
    for i in range(1, len(a)):      #출발 시간만 문자열로 가져옴
        departure_time = a[i][0]

    # 텍스트 파일의 각 줄을 문자열로 


    while breakpoint:
        booking = int(input('예매 하려면 1, 아니면 2를 입력해주세요: '))
        if booking == 1:    #예매 하면 좌석 수를 -1 해줘야함
            print('예매완료.')
            # a[??][5] -= 1
            break
        elif booking == 2:  #예매 안 할 거면 다시 열차정보 입력부터 해야함
            print('처음으로 돌아갑니다.')
            break
        else:
            print('잘못 입력하셨습니다. 다시 입력해주세요.') 
            pass
elif menu == 2:     #전체 기차 리스트 출력 및 
    for line in range(1, len(a)):
        print(line)
    f.close()

elif menu == 3:     #나의 예매 현황 출력 및 예매 취소
    pass    
else:               #프로그램 종료
    pass    
# # if seat_remain == 0:
# #     print('매진입니다')