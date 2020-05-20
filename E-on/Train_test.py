f = open("C:/project/Study/E-on/TrainList.txt",'r')    

#변수 초기화
t_dep = 0           #출발시간
station_dep = 0     #출발역
station_arr = 0     #도착역
train = 0           #열차 종류
seat_remain = 0     #잔여석

def menu1():
    global f, t_dep, station_dep, station_arr, train
    t_dep, station_dep, station_arr, train = list(input('*******************\n원하는 출발 시간을 입력하세요(hhmm 형식): ')),input('출발역을 입력하세요: '),input('도착역을 입력하세요: '),input('열차종류를 입력하세요: ')
    # 입력한 경로, 기차종류와 일치하는 리스트 중 입력시간과 가장 가까운 정보 출력함.
    a = []
    while breakpoint:
        line = f.readline()
        if not line: break
        myline = a.append(line.split(' '))
    t_res = 0               # 입력 시간을 총 분으로 변환
    if t_dep[0] == '0':     # 10의 자리가 0일때
        hour_res = int(t_dep[1])
        minute_res = int(t_dep[2] + t_dep[3])
        t_res = hour_res*60 + minute_res
    elif t_dep[0] == '1'or'2':
        hour_res = int(t_dep[0]+t_dep[1])
        minute_res = int(t_dep[2]+t_dep[3])
        t_res = hour_res*60 + minute_res           
    time_txt2 = []
    sub_t_list = []
    t_tot = 0
    for j in range(1,20):
        if station_dep == a[j][1] and station_arr == a[j][3] and train == a[j][4]:  #출발역, 도착역, 기차종류 같으면
            time_txt2 = a[j][0]                                  #그 열의 시간을 time_txt2 리스트에 저장한다.
            if time_txt2[0] == '0':                                 #만약 time_txt2 리스트의 첫번째 값이 0이면 즉,한자리 수 시간이면
                hour_txt = int(time_txt2[1])                            #입력한 시간의 두번째 자리 즉 1의 자리가 hour_txt이다.
                minute_txt = int(time_txt2[3] + time_txt2[4])               #입력한 시간의 3,4번째 자리 즉 분이 minute_txt이다.
                # t_tot_ = t_tot.append(hour_txt*60 + minute_txt)
                t_tot = hour_txt*60 + minute_txt                    # 시간:분을 총 분으로 계산
                sub_t = t_tot - t_res
                absolute_time = sub_t_list.append(abs(sub_t))       
            elif time_txt2[0] == '1' or '2':
                hour_txt = int(time_txt2[0]+time_txt2[1])
                minute_txt = int(time_txt2[3]+time_txt2[4])
                # t_tot_ = t_tot.append(hour_txt*60 + minute_txt)
                t_tot = hour_txt*60 + minute_txt
                sub_t = t_tot - t_res
                absolute_time = sub_t_list.append(abs(sub_t))
                listtime = abs(sub_t)
            min_sub = min(sub_t_list)
            p = sub_t_list.index(min_sub)
            for e in range(len(time_txt2)):
                if sub_t_list[e] == min_sub:
                    print(time_txt2[e])
    # print neartime_information                                                                  #시간 간격 가장 작은 것 출력하기
            # myneartime_information = neartime_information.append(sub_t_list[j-1])
            # sub_t[j-1] 중에서 min을 출력
            

            # while breakpoint:
            #     line = f.readline()
            #     if not line: break
            #     myline = a.append(line.split(' '))
    # mostnear = min(neartime_information)
    


    # find_near_time()
    #예매 여부 판단 -> 함수로 만들어 주어도 될 거 같다.
    while breakpoint:
        reserve = int(input('예매 하려면 1, 아니면 2를 입력해주세요: '))
        if reserve == 1:    #예매 하면 좌석 수를 -1 해줘야함
            print('예매완료.')
            # a = []
            # while breakpoint: 
            #     line = f.readline()
            #     if not line: break
            #     myline = a.append(line.split(' '))
            for k in range(1, len(a)):      #잔여 좌석수 정수로 출력 ----->>>>>> 가까운 시간 계산되면 그 줄의 좌석만 삭제하여 출력하기
                if k == j:
                    print(int(a[k][5])-1)
            break
        elif reserve == 2:  #예매 안 할 거면 다시 열차정보 입력부터 해야함
            print('처음으로 돌아갑니다.')
            break
        else:
            print('**잘못 입력하셨습니다. 다시 입력하세요**') 
            pass
def menu2():
    global f
    while breakpoint: 
        line = f.readline()
        if not line: break  #더이상 읽을 줄이 없으면 
        print(line)
def menu3():
    #나의 예매 현황 출력 및 예매 취소
    pass


# inf = input().split(' ')

menu = int(input('***********메뉴***********\n1번 : 열차정보 조회\n2번 : 열차시간 보기\n3번 : 예매 현황 조회/취소\n**************************\n메뉴를 선택하세요: '))

while True:
    if menu == 1:
        menu1()
    elif menu == 2:
        menu2()
    elif menu == 3:
        menu3()
    elif menu == 4:
        break
    else:
        print('다시 입력해주세요.')
        pass


# def seat_remain_():
#     while breakpoint: 
#         line = f.readline()
#         if not line: break  #더이상 읽을 줄이 없으면
#         myline = a.append(line.split(' '))
#     for i in range(1, len(a)):      #잔여 좌석수 정수로 출력
#                 print(int(a[i][5]))