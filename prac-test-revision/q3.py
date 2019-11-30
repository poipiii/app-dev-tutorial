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
        self.__author = author
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
    
    #def __str__(self):
    #    return 'There are {} copies of {} ({}) written by {}'.format(self.get_quantity(),self.get_title(),self.get_isbn(),self.get_author())
#
#b = Book('012345678901z','Python for Everyone','Python King',100)
#
#print(b)


#class BookStore:
#  def __init__(self):
#    self.books = {}
#    #self.create_dummy_books()
#    self.load_books()
# 
#  def create_dummy_books(self):
#    file = open('prac-test-revision/books.txt', 'w')
#    file.write('012345678901z,Python for Everyone,Python King,100\n')
#    file.write('112345678901y,Intermediate Python,John Python,200\n')
#    file.write('212345678901x,Advanced Python,Anaconda,300\n')
#    file.write('312345678901v,Beginner Python,Twisted Python,400\n')
#    file.close()
# 
#  # initialize the books attribute with data from books.txt file
#  def load_books(self):
#    
#
#    file = open('prac-test-revision/books.txt', 'r')
#  
#    for i in file:
#        try:
#            book = i.rstrip('\n').split(',')
#            isbn = book[0]
#            title = book[1]
#            author = book[2]
#            quantity = book[3]
#            obj = Book(isbn,title,author,quantity)
#            self.books[isbn] = obj
#        except IndexError:
#            pass
#    file.close()
#    
#        
#
# 
#  # display all the book isbn and titles
#  def display(self):
#      for i in self.books.values():
#          print('There are {} copies of {} ({}) written by {}'.format(i.get_quantity(),i.get_title(),i.get_isbn(),i.get_author()))
# 
#bs = BookStore()
#bs.display()



#class BookStore:
#  def __init__(self):
#    self.books = {}
#    self.create_dummy_books()
#    self.load_books()
# 
#  def create_dummy_books(self):
#    file = open('prac-test-revision/books.txt', 'w')
#    file.write('012345678901z,Python for Everyone,Python King,100\n')
#    file.write('112345678901y,Intermediate Python,John Python,200\n')
#    file.write('212345678901x,Advanced Python,Anaconda,300\n')
#    file.write('312345678901v,Beginner Python,Twisted Python,400\n')
#    file.close()
# 
#  # initialize the books attribute with data from books.txt file
#  def load_books(self):
#    file = open('prac-test-revision/books.txt', 'r')
#    for i in file:
#        book = i.rstrip('\n').split(',')
#        self.isbn = book[0]
#        self.title = book[1]
#        self.author = book[2]
#        self.quantity = book[3]
#        self.books[self.isbn] = self.isbn,self.title,self.author,self.quantity
#    file.close()
#
# 
#  # display all the book isbn and titles
#  def display(self):
#    print(self.books)
# 
#bs = BookStore()
#bs.display()

















import random
fruit = {}
class Fruit:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

# This function
# (1) ask the user to enter the fruit name and description 3 times.
# (2) store the Fruit object in a dictionary
'''
Sample output:

Enter the fruit name: Apple
Enter the description of the fruit: Snow White ate this fruit
Enter the fruit name: Orange
Enter the description of the fruit: Many people buy this fruit for CNY
Enter the fruit name: Watermelon
Enter the description of the fruit: This fruit is big and round.

'''
def store_fruits():
    for i in range(3):
        fruit_name = input('Enter the fruit name:')
        fruit_desc = input('Enter the description of the fruit:')
        f = Fruit(fruit_name,fruit_desc)
        fruit[i+1] = f


# This function:
# 1. Randomly pick a fruit from the dictionary and display its description
# 2. Ask the user to guess the fruit. User will be given 3 chances.
# 3. If the user guesses correctly or used up the 3 chances, ask the user if he wants to try again.
# 4. If yes, repeat step 2 to 4. If no, exit.
'''
Sample output:

Description of the fruit:
Snow White ate this fruit.

Guess a fruit: orange
You have 2 chance(s) left
Guess a fruit: apple
Bingo
Do you want to try again (Y/N)? y

Description of the fruit:
Many people carry this fruit during CNY

Guess a fruit: pear
You have 2 chance(s) left
Guess a fruit: apple
You have 1 chance(s) left
Guess a fruit: banana
You have 0 chance(s) left
Do you want to try again (Y/N)? n

'''
def guess():
    chance = 3
    num = random.randint(1,3)
    while True:
        if chance > 0:
            print(fruit[num].desc)
            guess = input('Guess a fruit:')
            if guess == fruit[num].name:
                print('bingo')
                again = input('Do you want to try again (Y/N)?')
                if again.lower() == 'n':
                    break
                else:
                    chance = 3
                    num = random.randint(1,3)
                    continue
            else:
                chance -= 1
                print('you have {} chance(s) left'.format(chance))               
                continue
        else:
            again = input('Do you want to try again (Y/N)?')
            if again.lower() == 'n':
                break
            else:
                chance = 3
                num = random.randint(1,3)
                continue



store_fruits()
guess()






