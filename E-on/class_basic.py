왜 안되노 도대체
# class Person():
#     def __init__(self, name, age, address):
#         self.hello = "안녕하세요"
#         self.name = name
#         self.age = age
#         self.address = address

#     # def __str__(self):


#     def greeting(self):
#         print('{0] 저는 {1}입니다'.format(self.hello, self.name))




# james = Person("팽대원", 25, "수원")
# Fred = Person("정영윤", 24, "수원")

# print(james)

class calculater:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

call = calculater()

print(call)