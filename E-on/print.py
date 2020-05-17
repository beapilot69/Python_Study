n, m = map(int, input("총 작업 개수, 구할 작업 번호 입력: ").split())
priorities = list(map(int, input("각 우선순위 차례로 입력: ").split()))

priorities2 = []
for i in range(n):
    priorities2.append(0)

priorities2[m] = 'target'  #구할 작업 번호의 위치를 priorities_ 리스트의 같은 위치에 1로 설정
time = 0    #출력시간 초기값 지정

while True:
    if priorities[0] == max(priorities):    #처음에 9라 했다가 가장 큰 우선순위가 무엇인지 모를 수 있으므로 max사용.
        time += 1       #첨부터 가장 큰 우선순위면 바로 출력이므로 출력시간 = +1분
        if priorities2[0] == 'target':
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