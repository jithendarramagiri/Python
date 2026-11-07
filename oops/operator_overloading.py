class book :
    def __init__(self,book1,book2,book3):
        self.book1 = book1
        self.book2 = book2
        self.book3 = book3
    def __add__(self,other):
        return self.book1 + self.book2 + self.book3
    def __str__(self):
        return f"book pages: {self.book1} {self.book2} {self.book3}"
b = book(100,200,300)
print("Total pages:", b +b)





