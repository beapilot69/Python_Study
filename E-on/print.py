n, m = map(int, input("총 작업 개수, 구할 작업 번호 입력: ").split())    
priorities = list(map(int, input("각 우선순위 차례로 입력: ").split()))

priorities2 = []
for i in range(n):
    priorities2.append(int(i))

priorities2[m] = m  #단순 연산만을 위한 리스트
time = 0    #출력시간 초기값 지정

while True:
    if priorities[0] == max(priorities):  #가장 큰 우선순위가 무엇인지 모를 수 있으므로 max사용.
        time += 1       #첨부터 가장 큰 우선순위면 바로 출력이므로 출력시간 = +1분
        if priorities2[0] == m:
            print(time)
            break
        else:
            del priorities[0]
            del priorities2[0]
    else:
        priorities.append(priorities[0])
        del priorities[0]
        priorities2.append(priorities2[0])
        del priorities2[0]
