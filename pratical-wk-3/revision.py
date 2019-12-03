# class Player:
#     def __init__(self,player_name):
#         self.__player_name =player_name
#     def set_name(self,player_name):
#         self.__player_name =player_name
#     def get_name(self):
#         return self.__player_name

# class BasketballPlayer(Player):
#     positions = ['Guard','Forward','Center']
#     def __init__(self, name, position):
#         super().__init__(name)
#         self.__position = ''
#         self.set_pos(position)
#     def set_pos(self, position):
#         if position in self.__class__.positions:
#             self.__position = position
#         else:
#             return fal
#     def get_pos(self):
#         return self.__position


# plist = []
# for i in range(3):
#     player = input('enter playername')
#     pos = input(('enter player position'))
#     p = BasketballPlayer(player,pos)
#     plist.append(p)

# for i in plist:
#     print('{} is playing as {}'.format(i.get_name(),i.get_pos()))


