# 20250826



# 3.2 字典的现代句法
#region
####Study####
'''
1. 3.9 引入'|'; 3,10引入 match/case
2.字典推导式
3. 合并映射 '|' ,后覆盖前 非就地修改
4. 就地合并映射 '|='
'''

#############


# dial_codes = [
#     (1,'a'),
#     (2,'b'),
#     (3,'c'),
#     (4,'d'),
# ]
# test = {dial: string for dial,string in dial_codes} #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# # unpacking
# def dump(**kwargs):
#     return kwargs
# dump(**{'x':1},y=2,**{'z':3}) #{'x': 1, 'y': 2, 'z': 3}

d1 = {'a':3,'b':4}
d2 = {'a':2,'b':4,'c':5}
c = d1|d2 # {'a': 2, 'b': 4, 'c': 5}

d1 = {'a':3,'b':4}
d2 = {'a':2,'b':4,'c':5}
d1|=d2
d1 # {'a': 2, 'b': 4, 'c': 5}





#endregion