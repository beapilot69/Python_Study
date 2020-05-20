f = open("C:/project/Study/E-on/TrainList.txt",'r')    

a = []
time = []
while breakpoint:
    line = f.readline()
    if not line: break
    myline = a.append(line.split(' '))

print(len(a))


#---------------------------------------------------------------------------------------------
            # time_txt = []
            # sub_t_list = []          # 시간 차이 리스트 -> 시간의 차이들이 저장 되어있음
            # t_tot = 0
            # for i in range(1,len(a)-1):
            #     time_txt = a[i][0]
            #     if time_txt[0] == '0':
            #         hour_txt = int(time_txt[1])                 #time 이라는 리스트에 시간을 모두 저장
            #         minute_txt = int(time_txt[3] + time_txt[4])
            #         t_tot = hour_txt*60 + minute_txt
            #         sub_t = t_tot - t_res
            #         absolute_time = sub_t_list.append(abs(sub_t))      #sub_t_list에 시간 차이 절대값들이 들어있음

            #         # print(hour)
            #         # print(minute)

            #     elif time_txt[0] == '1':
            #         hour = int(time_txt[0]+time_txt[1])
            #         minute = int(time_txt[3] + time_txt[4])
            #         t_tot = hour*60 + minute
            #         sub_t = t_tot - t_res
            #         absolute_time = sub_t_list.append(abs(sub_t))
            #         # print(hour)
            #         # print(minute)
            #     elif time_txt[0] == '2':
            #         hour = int(time_txt[0]+time_txt[1])
            #         minute = int(time_txt[3]+time_txt[4])
            #         t_tot = hour*60 + minute
            #         sub_t = t_tot - t_res
            #         absolute_time = sub_t_list.append(abs(sub_t))
            #     #이제 입력한 시간의 시간/분 과 hour,minute을 비교해서 가까운 것 출력 
            #         # if min(sub_t[j])