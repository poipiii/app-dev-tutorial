# class Animal:
#     def __init__(self,species):
#         self.species = species
#     def make_sound(self):
#          print('grrrrrrrr')
#     def __str__(self):
#         return 'i am a {}'.format(self.species)

# class Cat(Animal):
#     def __init__(self,food):
#         super().__init__('cat')
#         self.food = food
#     def make_sound(self):
#         print('meow')
#     def __str__(self):
#         return 'i am a {} my favorite food is {}'.format(self.species,self.food)

# class Pig(Animal):
#     def __init__(self):
#         super().__init__('pig')
#     def make_sound(self):
#         print('oink')


# def to_list():
#     ani_list = []
#     cat1 = Cat('Fish')
#     ani_list.append(cat1)
#     pig2 = Pig()
#     ani_list.append(pig2)
#     cat3 = Cat('Biscuit')
#     ani_list.append(cat3)
#     cat4= Cat('Canned Food')
#     ani_list.append(cat4)
#     return ani_list

# ani_list = to_list()
# for i in ani_list:
#     print(i)

# a = Animal('dog')
# print(a)
# a.make_sound()
# c = Cat('fish')
# print(c)
# c.make_sound()
# p = Pig()
# print(p)
# p.make_sound()

# class fruit:
#     def __init__(self,fruit,desc):
#         self.fruit = fruit
#         self.desc = desc
# def tolist():
#     f_list = []
#     fw =  open('Revision.txt','r')
#     for i in fw:
#         line = i.rstrip('\n').split(',')
#         f = fruit(line[1],line[0])
#         f_list.append(f)
#     fw.close()
#     new_list(f_list)
# def new_list(list):
#     fw =  open('new-fruit.txt','a')
#     for i in list:
#         fw.write('{} is {} \n'.format(i.fruit,i.desc))
#
#     fw.close()
#
#
#
# tolist()
# import random
# while True:
#     name = input('enter your name')
#     if len(name) < 2:
#         print('Nmae too short .')
#         continue
#     else:
#         pass
#     num1 = int(input('enter number 1:'))
#     num2 = int(input('enter number 2:'))
#     r1 = random.choice(name)
#     r2 = random.choice(name)
#     print(r1*num1)
#     print(r2*num2)
#     break


import  random , shelve


class urls:
    def __init__(self,long):
        self.short = ''
        self.long = long
        self.convert_small(long)

    def convert_small(self,url):
        st = url[4:-4]
        letter1 = random.choice(st)
        letter2 = random.choice(st)
        letter3 = random.choice(st)
        self.short = 'www.'+letter1+letter2+letter3+'.com'

    def to_shelve(self,obj):
        db = shelve.open('url.db','c')
        db[self.short] = obj
        db.close()

    





# url = ["www.google.com","www.yahoo.com","www.facebok.com"]

# url_list = []
# for i in url:
#     u = urls(i)
#     u.to_shelve(u)

def swap(url_to_swap):
        db = shelve.open('url.db','c')
        url_obj = db[url_to_swap]
        if url_to_swap == url_obj.short:
            db[url_obj.long] = url_obj
            del(db[url_to_swap])
        elif url_to_swap == url_obj.long:
            db[url_obj.short] = url_obj
            del(db[url_to_swap])
        else:
            print('invalid url')
        db.close()

swap('www.ooh.com')




def display():
    db = shelve.open('url.db','r') 
    print(list(db.items()))
    db.close()
display()


#print(self.long)

# def covert_to_small(url_list):
#     shorturllst = []
#     for i in url_list:
#         st = i[4:-4]
#         letter1 = random.choice(st)
#         letter2 = random.choice(st)
#         letter3 = random.choice(st)
#         shorturl = 'www.'+letter1+letter2+letter3+'.com'
#         shorturllst.append(shorturl)
#     return shorturllst

# def save(short_url_list,long_url_list):
#     db = shelve.open('url.db','c')
#     for i in long_url_list:
#         for x in short_url_list:
#             if x not in db:
#                 db[x] = i
#                 break
#             else:
#                 pass
#     db.close()
#
# def swap():
#     db = shelve.open('url.db','c')
#     for i in db:
#         db[db[i]] = i
#         del(db[i])
#     db.close()
#
# def save_short():
#     db = shelve.open('url.db','c')
#     for i in db:
#         db[db[i]] = i
#         del(db[i])
#     db.close()


# def test_save(short_url_list,long_url_list):
#     db = {}
#     for i in long_url_list:
#         for x in short_url_list:
#             if x not in db:
#                 db[x] = i
#                 break
#             else:
#                 pass
#     print(db)

# def delete():
#     db = shelve.open('url.db','c')
#     db.clear()
#     db.close()
# delete()

#short = covert_to_small(url)
#save(short,url)


# test = {'a':'b','c':'d'}
# test2 = {'b': 'a', 'd': 'c'}
# test3 = {}
# for i in test.keys():
#     test2[test[i]] = i
# print(test2)
# for i in test2.keys():
#     test3[test2[i]] = i
# print

