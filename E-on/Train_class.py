#변수 초기화
t_dep = 0           #출발시간
t_dep2 =0
station_dep = 0     #출발역
station_arr = 0     #도착역
train = 0           #열차 종류
seat_remain = 0     
station_dep2 = 0    
station_arr2 = 0    
train2 = 0          
seat_remain2 = 0     
a = []
reservated_list = []
number_of_ind = []

f = open("C:/project/Study/E-on/TrainList.txt",'r')

def menu1():
    global f, t_dep, station_dep, station_arr, train, t_dep2, station_dep2, station_arr2, train2, seat_remain2, a, line, myline, reservated_list, number_of_ind
    t_dep, station_dep, station_arr, train = list(input('*******************\n원하는 출발 시간을 입력하세요(hhmm 형식): ')),input('출발역을 입력하세요: '),input('도착역을 입력하세요: '),input('열차종류를 입력하세요: ')
    # 입력한 경로, 기차종류와 일치하는 리스트 중 입력시간과 가장 가까운 정보 출력함.
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
    
    time_txt2 = [] #1행1열짜리임. 그 순간의 시간만 저장
    time_txt = []
    sub_t_list = []
    sts_dep = []
    sts_arr = []
    trn = []
    seats = []
    t_tot = 0
    j = 0
    for j in range(1,20):
        if station_dep == a[j][1] and station_arr == a[j][3] and train == a[j][4]:  #출발역, 도착역, 기차종류 같으면

            time_txt2 = a[j][0]                                  #그 열의 시간을 time_txt2 리스트에 저장한다.
            time_txt_ = time_txt.append(a[j][0])
            sts_dep_ = sts_dep.append(a[j][1])
            sts_arr_ = sts_arr.append(a[j][3])
            trn_ = trn.append(a[j][4])
            seats_ = seats.append(a[j][5])
            
            if time_txt2[0] == '0':                                 #만약 time_txt2 리스트의 첫번째 값이 0이면 즉,한자리 수 시간이면
                hour_txt = int(time_txt2[1])                            #입력한 시간의 두번째 자리 즉 1의 자리가 hour_txt이다.
                minute_txt = int(time_txt2[3] + time_txt2[4])               #입력한 시간의 3,4번째 자리 즉 분이 minute_txt이다.
                t_tot = hour_txt*60 + minute_txt                    # 시간:분을 총 분으로 계산
                sub_t = t_tot - t_res
                absolute_time = sub_t_list.append(abs(sub_t))       
            elif time_txt2[0] == '1' or '2':
                hour_txt = int(time_txt2[0]+time_txt2[1])
                minute_txt = int(time_txt2[3]+time_txt2[4])
                t_tot = hour_txt*60 + minute_txt
                sub_t = t_tot - t_res
                absolute_time = sub_t_list.append(abs(sub_t))

    sub_min = min(sub_t_list)
    sub_min_ind = sub_t_list.index(sub_min) #절대값 가장 작은 인덱스 찾았음
    print(time_txt[sub_min_ind], end=' ')
    print(sts_dep[sub_min_ind], end=' ')
    print(' -> ', end=' ')
    print(sts_arr[sub_min_ind], end=' ')
    print(trn[sub_min_ind], end=' ')
    print(seats[sub_min_ind])

    # find_near_time()
    #예매 여부 판단 -> 함수로 만들어 주어도 될 거 같다.
    while breakpoint:
        reserve = int(input('예매 하려면 1, 아니면 2를 입력해주세요: '))
        if reserve == 1:    #예매 하면 좌석 수를 -1 해줘야함
            # print(time_txt[sub_min_ind], end=' ')
            # print(sts_dep[sub_min_ind], end=' ')
            # print(' -> ', end=' ')
            # print(sts_arr[sub_min_ind], end=' ')
            # print(trn[sub_min_ind], end=' ')
            print('*****예매완료*****\n')
            print('해당 열차의 남은 좌석수: ', end=' ')
            print(int(seats[sub_min_ind])-1)
            print('\n')

            t_dep2 = time_txt[sub_min_ind]
            station_dep2 = sts_dep[sub_min_ind]
            station_arr2 = sts_arr[sub_min_ind]
            train2 = trn[sub_min_ind]
            seat_remain2 = int(seats[sub_min_ind])-1
            for w in range(1,20):
                if a[w][0] == t_dep2 and a[w][1] == station_dep2 and a[w][3] == station_arr2 and a[w][4] == train2:
                    sr = int(a[w][5])
                    a[w][5] = sr-1  #잔여석 -1 해서 텍스트파일에 적용됨
                    print('\n')
                    number_of_ind_ = number_of_ind.append(w)   #출력한 열차정보의 인덱스를 number_of_ind 리스트에 저장.                 
                    reservated_list_ = reservated_list.append(a[w])

            # print(type(number_of_ind))
            break

        elif reserve == 2:  #예매 안 할 거면 다시 열차정보 입력부터 해야함
            print('처음으로 돌아갑니다.')
            break
        else:
            print('**잘못 입력하셨습니다. 다시 입력하세요**') 
            pass

       
def menu2():
    global a
    for o in range(len(a)):
        for q in range(len(a[o])):
            print(a[o][q], end=' ')
        print('\n')
    

def menu3():
    global number_of_ind, reservated_list, f, a
    last_menu = int(input('\n--------------\n1번 : 예매 현황 출력\n2번 : 예매 취소\n3번 : 뒤로가기\n--------------\n번호를 입력하세요: '))
    print('\n')
   
    while True:
        if last_menu == 1:
            for g in range(0,len(number_of_ind)):
                inttype_of_number_of_ind = int(number_of_ind[g])
                for l in range(0,5):
                    print(a[inttype_of_number_of_ind][l], end=' ')
                print('\n')
            break
            # for i in range(0,20):
            #     for o in range(len(a)):
            #         for q in range(len(a[o])):
            #         print(a[o][q], end=' ')
            #     print('\n')

        elif last_menu == 2:
            print('시스템 점검으로 예매 취소가 불가능합니다.')
        elif last_menu == 3:
            break
    # f.close()

# while True:

while True:
    print('\n***********메뉴***********\n1번 : 열차정보 조회\n2번 : 열차시간 보기\n3번 : 예매 현황 조회/취소\n**************************\n')
    menu = int(input('메뉴를 선택하세요: '))
    # while breakpoint:
    #     line = f.readline()
    #     if not line: break
    #     myline = a.append(line.split(' '))
    if menu == 1:
        menu1()
    elif menu == 2:
        menu2()
    elif menu == 3:
        menu3()
    elif menu == 4:
        print('프로그램을 종료합니다.')
        break
    else:
        print('\n다시 입력해주세요.\n')
        pass
f.close()


# def seat_remain_():
#     while breakpoint: 
#         line = f.readline()
#         if not line: break  #더이상 읽을 줄이 없으면
#         myline = a.append(line.split(' '))
#     for i in range(1, len(a)):      #잔여 좌석수 정수로 출력
#                 print(int(a[i][5]))