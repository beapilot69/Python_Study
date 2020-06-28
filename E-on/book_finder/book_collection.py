import os
TF = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(TF,'input.txt')
f = open(my_file,'r')
booklist = f.readlines()

# print(booklist)
print(f)