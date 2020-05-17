def functions(m, queue, time):
    while True:
        notice = 1
        for i in range(1, len(queue)):
            if(queue[0][1] < queue[i][1]):
                queue.append(queue[0])
                del queue[0]
                notice = 0
                break
        if(notice == 0):
            continue
        else:
            time += 1
            if(queue[0][0] == m):
                break
            else:
                del queue[0]
    return time


# ip = int(input())

answer = [] ## 출력 값

list1 = []
list2 = []
# for i in range(ip):
list1.clear()
list2.clear()
N, M = map(int, input().split())
list1 = list(map(int, input().split()))
for j in range(N):
    list2.append([j, list1[j]])
answer = functions(M, list2, 0)

print(answer)