class Book:
    def __init__(self,isbn,title,author,quantity):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__quantity = quantity

    def set_isbn(self,isbn):
        self.__isbn = isbn
    def set_title(self,title):
        self.__title = title
    def set_author(self,author):
        self.__author= author
    def set_quantity(self,quantity):
        self.__quantity = quantity

    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author

    def get_quantity(self):
        return self.__quantity


# b =Book('012345678901z','Python for Everyone','Python King',100)
# print('there are {} of {}({}) written by {}'.format(b.get_quantity(),b.get_title(),b.get_isbn(),b.get_author()))
class BookStore:
    def __init__(self):
        self.books = {}
        self.create_dummy_books()
        self.load_books()

    # def create_dummy_books(self):
    #     file = open('books.txt', 'w')
    #     file.write('012345678901z,Python for Everyone,Python King,100\n')
    #     file.write('112345678901y,Intermediate Python,John Python,200\n')
    #     file.write('212345678901x,Advanced Python,Anaconda,300\n')
    #     file.write('312345678901v,Beginner Python,Twisted Python,400\n')
    #     file.close()

    def create_dummy_books(self):
        file = open('books.txt', 'w')
        file.write('012345678901z;Python for Everyone;Python King;100\n')
        file.write('112345678901y;Intermediate Python;John Python;200\n')
        file.write('212345678901x;Advanced Python;Anaconda\n')
        file.write('312345678901v;Beginner Python;Twisted Python;400\n')
        file.close()
    # initialize the books attribute with data from books.txt file
    def load_books(self):
        try:
            fw = open('books.txt','r')
            for i in fw:
                line = i.rstrip('\n').replace(';',',').split(',')
                if len(line) == 4:
                    b = Book(line[0],line[1],line[2],line[3])
                    self.books[b.get_isbn()] = b
                else:
                    pass
            fw.close()
        except IOError:
            print('file not found')
        except:
            print('unknown error')

    # display all the book isbn and titles
    def display(self):
        for b in self.books.values():
            print('there are {} of {}({}) written by {}'.format(b.get_quantity(), b.get_title(), b.get_isbn(),b.get_author()))


bs = BookStore()
bs.display()





