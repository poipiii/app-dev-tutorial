# class Animal:
#     def __init__(self,species):
#         self.species = species
#     def make_sound(self):
#          print('grrrrrrrr')
#     def __str__(self):
#         return 'i am a {}'.format(self.species)
#
# class Cat(Animal):
#     def __init__(self,food):
#         super().__init__('cat')
#         self.food = food
#     def make_sound(self):
#         print('meow')
#     def __str__(self):
#         return 'i am a {} my favorite food is {}'.format(self.species,self.food)
#
# class Pig(Animal):
#     def __init__(self):
#         super().__init__('pig')
#     def make_sound(self):
#         print('oink')
#
#
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
#
#     return ani_list
#
# ani_list = to_list()
# for i in ani_list:
#     print(i)

# a = Animal('dog')
# # print(a)
# # a.make_sound()
# #
# # c = Cat('fish')
# # print(c)
# # c.make_sound()
# #
# # p = Pig()
# # print(p)
# # p.make_sound()

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