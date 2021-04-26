from socket import *

print("Server TCP Initialize ... ")

#print("input SERVER IP ADDRESS : ")
#name = input() 
name = '192.168.0.68'

print("input SERVER PORT NUMBER : ")
port = int(input())

def cal_sum():
    c = str(a+b) #무조건 문자열로 보낼 수 있는 거 같음. int형으로 반환하니 "send() argument 1 must be string or buffer, not int" 라는 에러메세지가 출력 됨.
    return c

number = 30
for i in range(number):
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((name, port))
    print("Server connected... ")
    ############
    print("Input 2 numbers what you want to sum! :")
    a = int(input())
    b = int(input())
    ############
    cal_sum()
    clientSock.send(cal_sum().encode())
    recv_str = clientSock.recv(1024)
    print("server : ", recv_str)
