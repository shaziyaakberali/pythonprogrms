class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
         return book(self.pages+other.pages)

    def __sub__(self, other):
        return book(self.pages - other.pages)

    def __truediv__(self, other):
        return book(self.pages / other.pages)

    def __str__(self):
        return str(self.pages)
b1=book(1)
b2=book(2)
b3=book(3)
print(b1+b2+b3)
print(b1-b2)
print(b1/b2)