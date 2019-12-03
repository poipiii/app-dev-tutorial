# count = int(input('How many number you want to capture?'))
# numList = []
# try:
#     for i in range(count):
#         msg = 'Enter number #' + str(i+1)
#         num = int(input(msg))
#
#
#     print('The lowest number in the list:', min(numList))
#     print('The highest number in the list:', max(numList))
#     print('The total of the number in the list:', sum(numList))
#     print('The average of the number in the list:',sum(numList)/len(numList))
#
# except ValueError:
#     print('value error')
# except ZeroDivisionError:
#     print('zerodiv error')
# except:
#     print('unknown error')


import random
class pokemon:
    def __init__(self,name,health,attack,defence):
        self.__name =  name
        self.__health = health
        self.__attack = attack
        self.__defence = defence
    def set_name(self,name):
        self.__name = name  
    def set_health(self,health):
        self.__health = health
    def set_attack(self,attack):
        self.__attack = attack 
    def set_defence(self,defence):
        self.__defence = defence

    def get_name (self):
        return self.__name
    def get_health (self):
        return self.__health
    def get_attack (self):
        return self.__attack
    def get_defence (self):
        return self.__defence

class Firetype(pokemon):
    def __init__(self):
        super().__init__('scorbunny',10,9,4)
        self.__type = 'Fire'
        #self.__name = 'firebug'
        #self.__health = 10
        #self.__attack = 9
        #self.__defence = 4
    def get_type(self):
        return self.__type
    
class Watertype(pokemon):
    def __init__(self):
        super().__init__('sobble',15,6,4)
        self.__type = 'Water'

    def get_type(self):
        return self.__type
        #self.__name = 'waterbird'
        #self.__health = 15
        #self.__attack = 6
        #self.__defence = 4 
class Grasstype(pokemon):
    def __init__(self):
        super().__init__('grookey',20,5,3,'Grass')
        self.__type = 'Grass'
    def get_type(self):
        return self.__type
        #self.__name = 'grasshoper'
        #self.__health = 20
        #self.__attack = 5


class pokemon_sns:
    def __init__(self,trainer_pokemon,num):
        self.trainer_pokemon = None
        self.Ai_pokemon = None
        self.player_pokemon(trainer_pokemon)
        self.com_pokemon(num)
    def player_pokemon(self,pokemon_type):
        if pokemon_type.lower() == 'f':
            self.trainer_pokemon = Firetype()
        elif pokemon_type.lower() == 'w':
            self.trainer_pokemon = Watertype()
        elif pokemon_type.lower() == 'g':
            self.trainer_pokemon = Grasstype()
        else:
            print('invalid typen try again')
            self.trainer_pokemon = False

    def com_pokemon(self,random_num):
        if random_num == 1:
            self.Ai_pokemon = Firetype()
        elif random_num == 2:
            self.Ai_pokemon = Watertype()
        elif random_num == 3:
            self.Ai_pokemon = Grasstype()
        else:
            print('out of range')
    def p_attack(self):
        dmg = self.trainer_pokemon.get_attack() - self.Ai_pokemon.get_defence()
        new_health = self.Ai_pokemon.get_health() - dmg
        self.Ai_pokemon.set_health(new_health)
    def c_attack(self):
        dmg = self.Ai_pokemon.get_attack() - self.trainer_pokemon.get_defence()
        new_health = self.trainer_pokemon.get_health() - dmg
        self.trainer_pokemon.set_health(new_health)





def display_info(pokemon_type):
    if isinstance(pokemon_type,pokemon):
        print('{} is a {} pokemon'.format(pokemon_type.get_name(),pokemon_type.get_type()))




    



