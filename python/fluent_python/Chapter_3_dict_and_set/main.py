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



# 3.4/3,5 mapping api 处理缺失的key
#region
####Study####
'''
1. collections.abc中 Mapping和MutableMapping描述dict和类似类型接口
2. collection是基础，mapping继承collection，MutableMapping继承mapping
3. 可哈希：在一个对象的生命周期内 永不改变（__hash__()）,且可与其他对象比较（__eq__()）
4. 数值类型 不可变的扁平类型str和bytes.frozenset对象也是可hash,当所有项都是可hash的,tuple对象才是可哈希的
5. setdefalt('attr',data) 找不到参数 自动生成参数
6. 搜索key失败的解决办法：1.defaultdict()，2. 实现__missing__
7. 遇到找不到的key,defaultdict的工作流:创建参数，插入参数，返回参数的应用
8. 如果dict含有__missing__,当dict.__getitem__找不到参数的时候，将调用__missing__,不抛出keyerror
'''

#############

# from collections.abc import Mapping,MutableMapping 
# test = {}
# isinstance(test,MutableMapping)
# isinstance(test,Mapping)


# 当a中没有name属性的时候，自动创建['a']
# a = {}
# a.setdefault('name',['a']).append('b')
# if 'name' not in a:
#     a['name'] = ['a']
# a['name'].append('b')

# __missing__
# class StrkeyDict(dict):
#     def __missing__(self,key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str[key]]
    
#     def get(self, key, default = None):
#         try:
#             return self[key]
#         except KeyError:
#             return default
    
#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()
    
# d = StrkeyDict([('2','two'),('3','three')])

# d['2']

# __getitem__(self, key)
# 作用：当使用 obj[key] 语法访问对象时，Python 会自动调用此方法。
# value = my_dict["key"]  # 触发 my_dict.__getitem__("key")

# 默认行为（在 dict 中）：
# 如果 key 存在 → 返回对应的值
# 如果 key 不存在 → 抛出 KeyError

# 2. __missing__(self, key)
# 作用：仅当 __getitem__ 找不到 key 时，作为后备逻辑被调用。
# 关键前提：
# 必须在继承自 dict 的子类中定义此方法，否则无效。
# __getitem__ 的默认实现（来自 dict）会检查是否存在 __missing__，若存在则调用它。
# class MyDict(dict):
#     def __missing__(self, key):
#         return "默认值"  # 自定义逻辑

# d = MyDict()
# print(d["不存在的键"])  # 触发 __missing__("不存在的键")


# 调用 d[key]
#         ↓
# 触发 d.__getitem__(key)
#         ↓
#     key 是否存在？
#      ↙      ↘
#    是        否
#    ↓          ↓
# 返回值     是否定义了 __missing__?
#               ↙      ↘
#             是        否
#             ↓          ↓
#     调用 __missing__(key)  抛出 KeyError

# __getitem__ 是键访问的入口方法，__missing__ 是它的错误处理扩展。
# 二者配合可实现更智能的字典行为（如自动初始化、默认值、动态计算）。
# 实际开发中，优先考虑 defaultdict 或 setdefault，复杂场景再用 __missing__
# #endregion



# 3.6 dict的变体
# 3.7 不可变映射
#region
####Study####
'''
1. collections.OrderedDict
2. collections.ChainMap
3. collections.Counter

4. mappingProxy 创建不可变映射
'''

#############

# Counter
# from collections import Counter

# ct = Counter('ewfhuinvgbiw')
# ct.update('aaas')
# ct.most_common(3)

# from types import MappingProxyType as mp
# d = {'a':'test'}

# d_proxy = mp(d)
# d_proxy['b'] = 'test2' # 'mappingproxy' object does not support item assignment

#endregion



# 3.9 dict的影响
#region
####Study####
'''
1. 不要在__init__ 外创建实例属性， python默认使用__dict__属性存储实例属性
'''
#############

#endregion



# 3.10 set 
#region
####Study####
'''
1. 去重:set, dict
2. set类型不可hash,不可以set嵌套set;fozenset可hash
'''
#############

# l = {'spam','spam','eggs','bacon','eggs','apple'}
# set(l)
# list(dict.fromkeys(l).keys()) 


#endregion
