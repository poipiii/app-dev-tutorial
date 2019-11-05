import random
class Monster:
    def __init__(self,name,health,attack,defence,element):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence
        self.__element = element   
    def set_name(self,name):
        self.__name = name
    def set_health(self,health):
        self.__health = health
    def set_attack(self,attack):
        self.__attack = attack
    def set_defence(self,defence):
        self.__defence = defence
    def set_element(self,element):
        self.__element = element
    def get_name(self):
        return self.__name 
    def get_health(self):
        return self.__health 
    def get_attack(self):
        return self.__attack 
    def get_defence(self):
        return self.__defence 
    def get_element(self):
        return self.__element

class FireMonster(Monster):
    def __init__(self):
        super().__init__('firebug',10,9,4,'Fire')

        #self.__name = 'firebug'
        #self.__health = 10
        #self.__attack = 9
        #self.__defence = 4
    
class WaterMonster(Monster):
    def __init__(self):
        super().__init__('waterbird',15,6,4,'Water')
        #self.__name = 'waterbird'
        #self.__health = 15
        #self.__attack = 6
        #self.__defence = 4 
class GrassMonster(Monster):
    def __init__(self):
        super().__init__('grasshopper',20,5,3,'Grass')
        #self.__name = 'grasshoper'
        #self.__health = 20
        #self.__attack = 5
        #self.__defence = 3

class Monster_game:
    p_mon = None
    c_mon = None
    def __init__(self):
        self.choose_monster()
        self.generate_monster()
       
    def choose_monster(self):
        player_monster = input('choose your monster (F,W OR G)')
        self.set_p_monster(player_monster)
         #player_monster = self.choose_monster()
         #return player_monster
    def generate_monster(self):
        compurer_monster = random.randint(1,3)
        self.set_c_monster(compurer_monster)

    def set_p_monster(self,p_monster):
        if p_monster == 'F':
            self.__class__ .p_mon = FireMonster()
        elif p_monster == 'W':
            self.__class__ .p_mon = WaterMonster()
        elif p_monster == 'G':
            self.__class__ .p_mon = GrassMonster()

    def set_c_monster(self,c_num):
        if c_num == 1:
            self.__class__.c_mon = FireMonster()
        elif c_num == 2:
            self.__class__.c_mon =  WaterMonster()
        elif c_num == 3:
            self.__class__.c_mon = GrassMonster()
    def get_c_mon(self):
        return self.__class__.c_mon 
    def get_p_mon(self):
        return self.__class__.p_mon

        
game = Monster_game()
         
def displayinfo(monster,dmg):
    if isinstance(monster,Monster):
        print(monster.get_name(),'suffers',dmg,'damage, the health is now',monster.get_health())

def minushealth_c(player,computer):
    dmg = computer.get_defence() - player.get_attack()
    health = computer.get_health() - dmg
    print(health)
    computer.set_health(health)
    displayinfo(computer,dmg)

def minushealth_p(computer,player):
    dmg = player.get_defence() - computer.get_attack()
    health = player.get_health() - dmg
    player.set_health(health)
    displayinfo(player,dmg)

for i in range(3):
    minushealth_c(game.get_p_mon(),game.get_c_mon())
    minushealth_p(game.get_c_mon(),game.get_p_mon())
    if game.get_c_mon().get_health() <= 0:
        print('you win')
        break
    elif game.get_p_mon().get_health() <= 0:
        print('you lose')
        break

