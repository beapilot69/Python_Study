queue = []   #리스트를 생성(선입선출의 공간)

work_Num, target_Num = map(int, input("작업개수, 구할 작업번호 쓰세요: ").split())   #작업 개수, 구할 작업번호
priorities = list(map(int, input("우선순위를 차례대로 입력하세요: ").split()))      #우선 순위 입력

for i in range(work_Num):
    queue.append(int(i))     #큐 리스트에 작업 개수만큼 요소를 입력

output = queue[0]   #첫번째 마주한 작업을 output으로 선언

if priorities[0] == 9:
    out = output
else:
    save = output
    queue[i-1] = queue[i]
    queue[i] = save

print(output)
print(out)
  
