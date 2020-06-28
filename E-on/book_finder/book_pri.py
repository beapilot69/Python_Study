import os
import book_collection

class pri:
    def __init__(self):
        self.collection = book_collection.menu_collection()
    def list_menu(self):
        print("--------------------")
        print("1. 도서 추가")
        print("2. 도서 검색")
        print("3. 도서 정보 수정")
        print("4. 도서 삭제")
        print("5. 도서 목록 출력")
        print("6. 저장")
        print("7. 종료(자동저장됨)")
        print("-------------------")
    def menu(self,booklist):
        self.list_menu()
        menu_num = int(input("메뉴를 선택하세요 : "))
        if menu_num == 1:
            self.collection.add_book(booklist)
            self.menu(booklist)
        elif menu_num == 2:
            self.collection.search_book(booklist)
            self.menu(booklist)
        elif menu_num == 3:
            self.collection.edit_book(booklist)
            self.menu(booklist)
        elif menu_num == 4:
            self.collection.delete_book(booklist)
            self.menu(booklist)
        elif menu_num == 5:
            self.collection.printing_booklist(booklist)
            self.menu(booklist)
        elif menu_num == 6:
            self.collection.save_booklist(booklist)
            self.menu(booklist)
        elif menu_num == 7:
            self.collection.save_booklist(booklist)
            print("<<프로그램을 종료합니다>>")
        else:
            print("<<다시 입력하세요>>")
            self.menu(booklist)
this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder,'input.txt')
f = open(my_file,'r')
booklist = f.readlines()
do1 = pri()   
do1.menu(booklist)