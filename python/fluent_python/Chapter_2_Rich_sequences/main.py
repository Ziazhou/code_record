
# 序列
# region
# 任何python对象在相爱内存中都有一个包含元数据的标头
# 序列类型：
#     容器序列 存放对象的引用 list,tuple,collections.deque
#     扁平序列 存放对象的数值 str,bytes,array.array
    # or
    #   可变序列 list bytearray....
    #   不可变序列 str,tuple,bytes
    #   可变序列继承不可变序列所有方法
# endregion

# 列表推导式
# region

# 1. 一行循环使用列表推导式,多行循环请分开写。或者使用for
# 2. python会忽略list，tuple，dict内部换行，无须使用 ‘\’
# 3. 海象运算符 会影响作用域，在列表推导式里
# 4. 列表推导式生成list，生成器表达式生成其他序列类型

# colors = ['black','white']
# sizes = ['S','M','L']
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)

# for color in colors:
#     for size in sizes:
#         print((color,size))
#endregion


# 生成器表达式
# region

##### Study ####
'''
1. 当表达式是函数唯一参数，可以不适应圆括号，见 45 行
'''
#########
# symbols = 'AbcDF'
# tuple(ord(symbol) for symbol in symbols)

# from array import array
# array('I',(ord(symbol) for symbol in symbols))

# colors = ['black','white']
# sizes = ['S','M','L']
# for tshirt in (f'{c} {s}' for c in colors for s in sizes):
#     print(tshirt)
#endregion

# tuple
# region

##### Study ####
'''
1. 特点：不可变列表 用作没有字段名称的记录
2. 使用 _ 表示虚拟变量， 在match/case中 是通配符，匹配值 不绑定数值
3. tuple 长度固定，内存比list少，
4.只有值永不可变的对象才是可哈希的，not hash的tuple 不可以作为 dict's key,不可以做set's element
5. tuple 不涉及增删项的list method
'''
#########
# tuple unpacking 元祖拆包
# iterable unpacking 可迭代对象拆包 3132
city, year, pop, chg, area = ('Tokyo','2003','32_450',0.66, 8014)


#endregion


# tuple and iterable unpacking
# region

##### Study ####
'''
1. 并行拆包 paralled unpacking
2. *  tuple unpacking
3. ** dict unpacking
4. *args 捕获剩余任意数目的参数, type(args) == list
5. os.path.split('filepath') -> (path, last_part)
'''
#########

# paralled unpacking
test = (3,4)
x,y = test

# 对调参数
x,y = y,x

# *
t = (20,8)
divmod(*t)


a, b, *args =  range(10)

a, *args, b=  range(10)

quotient, remainer = divmod(*t)



import os
tet, filename = os.path.split('/Users/swcm/Desktop/git_code/python/main.py')
#endregion



# match/case -python .10 - PEP 634
# Structural pattern Matching
# region

##### Study ####
'''
1. python 3.10 以上版本支持
2. 解构嵌套元祖,
3. 一个case子句由两部分组成，模式+卫语句 guard clause（可选）
4. 模式里不区分[],()
5. 与拆包的区别， 不解构序列之外的可迭代对象 es:迭代器
6. 可检查类型，匹配参数，不是转换参数， case [name,_,_,(float(x),float(y))]
7. *_: 匹配任意数量的项，*extra:匹配的多项，将绑定到extra上

'''
#########

# metro_area = [('a', 'b', 3, (3,4)),]
# def main():
#     for record in metro_area:
#         match record:
#             # case [name, _, _, (x, y)] if y < 5:
#             case (name, _, _, (x, y)) if y < 5:
#                 print('test1')
# main()


#endregion



# 切片
# region

##### Study ####
'''
1. 序列类型都支持
2. 为啥切片和区间排除最后一行
    a. 仅指定停止区域时候，容易判断长度，range(3),a[:3]
    b. 起始和停止都指定的时候，容易计算长度,stop - start
    c. 拆分区间 不重复，a[:x]和a[x:]
3. 切片对象  a = slice(2,6); s[a]
4. 如果赋值对象是一个切片，右边必须是iterable

'''
#########

s = 'abcdef'
# s[::3] # 'ad'
# s[::-1]  # 'fedcba'
# s[::-2] # 'fdb'

# slice(0,3)

# l =  list(range(10))
# l[2:5] = [20,30]
# del l[5:7]
# l[3::2] = [11,99]
# # l[2:5] = 100 Fail
# l[2:5] = [100]
# l

#endregion



# use to '+' and '*'
# region

##### Study ####
'''
1. '+' and '*' 返回新对象 不改变对象本身
2. += and '*=' 不返回新对象 改变对象本身
3. += 是调用 __iadd__ 就地相加，如果没有，调用__add__
4. *= 是调用 __imul__ 就地相乘
5. 不要对不可变序列 重复拼接，效率低，除了str
6. 都不是原子性操作

'''
#########

# l = [1, 2, 3,]

# l * 5

# board = [['_']*3 for _ in range(3)]
# board[1][2] = '3' # [['_', '_', '_'], ['_', '_', '3'], ['_', '_', '_']]
# print(board)

# weird_board = [['_'] * 3] * 3
# weird_board[1][2] = '3' # [['_', '_', '3'], ['_', '_', '3'], ['_', '_', '3']]
# print(weird_board)


#endregion



# use sort or sorted
# region

##### Study ####
'''
1. python APi约定，就地改变对象的函数 返回None
2. sort 就地排序 返回None
3. sorted 非就地排序 返回副本
4. 都接受两个参数:
    reverse: True 降序; False 升序 default
    key: 接收一个参数的函数，es: key = len
5. 相同条件 保持原有顺序
'''
#########


#endregion



# list is not ok
# region

##### Study ####
'''
1. 
'''
#########


#endregion