# class Library:
#
#     def __init__(self,name,login,logout):
#         self.name=name
#         self.login=login
#         self.logout=logout
#
#
#
#     def name_library(self):
#
#         print("The  name of the library is",self.name)
#         print(f"The  login time  is {self.login} AM")
#         print(f"The  logout time is {self.logout} PM")
#
#
# oxford=Library("oxford",10,12)
# (oxford.name_library())


class Librarian:

    def __init__(self,no_of_book):
        self.no_of_book=122

    librarian = None

    @classmethod
    def working_hours(cls):

        cls.librarian

    def lend_book(self):
        print(f"the librarian lend {self.no_of_book} book")

vishal = Librarian(12)




vishal.working_hours()
print(vishal.working_hours(vishal.librarian))




# class Book:
#
#     def __init__(self,bookname,pages):
#
#         self.bookname=bookname
#         self.pages=pages
#
#     book_name = "Sky is high"
#
#     def openbook(self):
#         print()
#
#     @classmethod
#     def reading(self, bookname):
#         print(f"Im reading {bookname} in")
#
#     @classmethod
#     def writing(self, bookname):
#         print(f"The new book im writing is {bookname}")
#
# class Member:
