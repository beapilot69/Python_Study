import os

class menu_collection:
    def add_book(self,booklist):
        self.inf_book = str(input("[도서추가]제목 저자 발행년도 출판사 카테고리 순으로 입력하세요.\n:"))
        booklist.append('\n'+self.inf_book+'\n')
        print("<<추가되었습니다>>")
        return booklist
    def search_book(self,booklist):
        search = str(input("검색어를 입력하세요 :"))
        for i in range(0,len(booklist)):
            if search in booklist[i]:
                print("검색결과 : "+booklist[i])
    def edit_book(self,booklist):
        for i in range(len(booklist)):
            print(i,'.', booklist[i])
        list_num = int(input("수정할 도서 번호를 입력하세요 :"))
        booklist[list_num] = str(input("[도서정보 수정]제목 저자 발행년도 출판사 카테고리 순으로 입력하세요.\n:"))
        print("<<수정되었습니다>>")
        return booklist
    def delete_book(self,booklist):
        for i in range(len(booklist)):
            print(i,'.', booklist[i])
        list_num = int(input("삭제할 도서 번호를 입력하세요 :"))
        booklist.pop(list_num)
        print("<<삭제되었습니다>>")
        return booklist
    def printing_booklist(self,booklist):
        print("[도서 목록]")
        print(booklist)
    def save_booklist(self,booklist):
        new_booklist = ''.join(booklist)
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder,'input.txt')
        fwrite = open(my_file,'w')
        fwrite.write(new_booklist)
        fwrite.close
        print("<<저장되었습니다>>")