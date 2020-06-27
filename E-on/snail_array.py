import numpy as np

n = int(input('n*n배열--n을 입력하세요 : '))
o = n
array = np.zeros((n,n), dtype = int)
count = 0
number = 1
dan = 0
def snail(number, count, n, o, array, dan):
    # while number == n:
    while True:
        for i in range(number,o+1):         #오른쪽으로 카운트
            count = count + 1
            array[dan][i-1] = count
        number = number + 1

        for i in range(number,o+1):         #아래로 카운트
            count = count + 1
            array[i-1][o-1] = count
        
        for i in range(o+1,number,-1):      #왼쪽으로 카운트
            count = count + 1
            array[o-1][i-3] = count

        for i in range(o+1, number+1,-1):   #위로 카운트
            count = count + 1  
            array[i-3][dan] = count
        dan = dan + 1                       #단 증가
        n = n - 2                           #안쪽 배열로 연산 시작
        o = o -1                            #단 증가에 따른 반복횟수 감소
        if n == -2 or n == -1:
            break
        snail(number,count, n, o, array, dan) #<수정>재귀함수 쓰임 명확히 할 것
snail(number,count, n, o, array, dan)

for f in array: #<참고> Asterisk(*)의 활용
    print( *f )