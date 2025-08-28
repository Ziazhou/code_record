# 2025.08.26
# #python 数据模型

# region
# 1
# from collections import namedtuple

# Card = namedtuple('Card',['rank','suit'])

# class FrenchDeck:
    
#     ranks = [str(n) for n in range(2,11)] + list('JQKA')
#     suits = 's d c h'.split()
    
#     def __init__(self):
#         self._cards = [Card[x,y] for x in self.ranks
#                                 for y in self.suits]
    
#     def __len__(self):
#         return len(self._cards)
    
#     def __getitem__(self,position):
#         return self._cards[position]
    
# # beer_card = Card('7','diamonds')
# # print(beer_card)


# deck = FrenchDeck()
# # print(len(deck))

# # print(deck[0])
# # from random import choice
# # print(choice(deck))

# # for card in deck:
# #     print(card)

# #排序
# suit_values = dict(a=3,h=2,d=1,c=0)

# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]

# for card in sorted(deck, key = spades_high):
#     print(card)

# endregion

# region
# import math
# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f'Vector({self.x},{self.y})'
    
#     def __abs__(self):
#         return math.hypot(self.x,self.y)
    
#     def __bool__(self):
#         return bool(abs(self))
    
#     def __add__(self,other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x,y)
    
#     def __mul__(self,scalar):
#         return Vector(self.x * scalar, self.y * scalar)
# a = Vector(3,4)
# b = Vector(2,1)

# print(a+b)
# print(a*3)
# print(abs(a))

# endregion

# region

# __repr__
#给repr函数使用，可使用!r

#__str__
#给str函数使用，print函数调用

# endregion