# time: 20250901
# Chapter 5 Data Class Constructors

# collections.namedtuple python2.6
# typing.NameTuple python3.5
# @dataclass.dataclass python3.7


#
# region

##### Study ####
'''
1. collections.namedtuple 和 typing.NameTuple 都是tuple的子类，可使用issubclass check
2. namedtuple 不可定义class
3. NameTuple 和 dataclass 都有__annotations__属性
4. 
'''
#########

#普通class定义
# class Coordinate:
#     def __init__(self,lat ,lon):
#         self.lat = lat
#         self.lon = lon

# moscow = Coordinate(55, 37)
# print(moscow) # <__main__.Coordinate object at 0x110657830>,__repr__ 没有意义
# print(id(moscow)) # 4570052656
# location = Coordinate(55, 37)
# print(id(location)) # 4573535776
# print(location == moscow) #False ==没有意义， __eq__比较的是ID参数

# collectios.namedtuple 不可构造class
# from collections import namedtuple
# Coordinate = namedtuple('Coordinate', 'lat lon')
# issubclass(Coordinate,tuple) # true

# moscow = Coordinate(55, 66)

# moscow == Coordinate(55, 66) # True


# typing.NameTuple
# from typing import NamedTuple,get_type_hints
# Coordinate = NamedTuple('Coordinate', [('lat', int),('lon', int)])
# Coordinate = NamedTuple('Coordinate', lat=int, lon=int)
# class Coordinate(NamedTuple):
#     lat: int
#     lon: int
    
#     def __str__(self):
#         ns = "N" if self.lat >= 0 else 'S'
#         we = "E" if self.lon >= 0 else 'W'
#         return f'{abs(self.lat)}'
# issubclass(Coordinate,tuple) # True
# get_type_hints(Coordinate) # {'lat': int, 'lon': int}

# from dataclasses import dataclass
# @dataclass(frozen=True)
# class Coordinate():
#     lat: int
#     lon: int
    
#     def __str__(self):
#         ns = "N" if self.lat >= 0 else 'S'
#         we = "E" if self.lon >= 0 else 'W'
#         return f'{abs(self.lat)}'
# issubclass(Coordinate,tuple) # False
#endregion