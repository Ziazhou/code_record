



# Python Effective Record

## Day1 2025.03.22

1. PEP8

   - 每⾏不超过79个字符

   - 对于占据多⾏的长表达式来说，除了⾸⾏之外的其余各⾏，都应该在通常的缩进级别之上再加4个空格 

   - 在同⼀份⽂件中，函数与类之间⽤两个空⾏隔开

   - 在同⼀个类中，⽅法与⽅法之间⽤⼀个空⾏隔开

   - 使⽤字典时，键与冒号之间不加空格，写在同⼀⾏的冒号和值之间应该加⼀个空格

   - 给变量的类型做注解（annotation）时，不要把变量名和冒号隔开，但在类型信息前应该有⼀个空格

   - 不要通过长度判断容器或序列是不是空的

     ``` python
     if not text:  			#yes
     if len(text) == 0	  #no
     ```

     

   - 采⽤⾏内否定，即把否定词直接写在要否定的内容前⾯，⽽不要放在整个表达式的前⾯

     ``` python
     if a is not b # yes
     if not a is b # no
     ```
     
   - 避循DRY原则，也就是不要重复⾃⼰写过的代码（Don't Repeat Yourself)

1. 把数据结构直接拆分到多个变量⾥，不要专门通过下标访问 --Unpacking

   ```python
   #升序算法--传统
   a = ['k','d','c','g']
   for _ in range(len(a)):
     for i in range(1,len(a)):
       if a[i]<a[i-1]:
         temp = a[i]
         a[i] = a[i-1]
         a[i-1] = temp
   print(a)
   #升序算法--Unpacking
   for j in range(len(a)):
       for i in range(1,len(a)):
           if a[i] <a[i-1]:
               a[i-1],a[i] = a[i],a[i-1]
   print(a)
   
   #  not Unpacking
   snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
   for i in range(len(snacks)):
       item = snacks[i]
       name = item[0]
       calories = item[1]
       print(f'#{i+1}: (name) has {calories}calories')
   # Unpacking 
   for rank,(name,calories) in enumerate(snacks,1):
       print(f'#{rank}: {name} has {calories} calories')
       
   ```

1. 尽量⽤enumerate取代range

   - enumerate--能够把任何⼀种迭代器（iterator）封装成惰性⽣成器

     ```python
     # sequence -- 一个序列、迭代器或其他支持迭代对象。
     # start -- 下标起始位置的值。
     enumerate(sequence, [start=0])
     flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
     ut = enumerate(flavor_list)
     print(next(ut))
     print(next(ut))
     print(next(ut))
     ```
     

1. ⽤zip函数同时遍历两个迭代器

   1. 介绍

      能把两个或更多的iterator封装成惰性⽣成器（lazy generator）。

      每次循环时，它会分别从这些迭代器⾥获取各⾃的下⼀个元素，并把这些值放在⼀个元组⾥⾯。

      ⽽这个元组可以拆分到for语句⾥的那些变量之中

      每次只从它封装的那些迭代器⾥⾯各⾃取出⼀个元素，所以即便源列表很长，程序会因为占⽤内存过多⽽崩溃。

      只要其中任何⼀个迭代器处理完毕，它就不再往下⾛了。于是，循环的次数实际上等于最短的那份列表所具备的长度。

      长度相同使用zip，长度不同使用itertools.zip_longest

   

   1. 会根据某份列表中的对象创建许多与这份列表有关的新列

      - 取出最长名字的字符串

      ```python
      names = ['Cecilia', 'Lise', 'Marie']
      counts = [len(n) for n in names]
      logest_name = None
      max_count = 0
      # first 
      for i in range(len(names)):
          count = counts[i]
          if count > max_count:
              logest_name = names[i]
              max_count = count
      print(logest_name)
      
      # second
      for i,name in enumerate(names):
          count = counts[i]
          if count > max_count:
              logest_name = name
              max_count = count
      print(logest_name)
      
      # third
      for name,count in zip(names,counts):
          if count > max_count:
              longest_name = name
              max_count = count
      print(longest_name)
      ```

1. ⽤赋值表达式减少重复代码

   1. 先获取该值，再判断，使用海象运算符号:=

      ``` PYTHON
      #old
      count = fresh.get('lemon',0)
      	if count:
              make_lemonada(count)
          else:
              out_of_stovk()
      #new
      	if count :=fresh.get('lemon',0):
           	make_lemonada(count)
          else:
              out_of_stock()
              
          if(count := fresh.get('apple',0)) >=4:
              make_cider(count)
          else:
              out_of_stock()
      
      
      ```

 ## Day2 2025.03.23 --Chapter2 list and dict

1. 学会对list切片
   1. 含有`__getitem__`，`__setitem__` 都可以切割
2. text





1.  感觉遇到一个懂自己的女生真的很难
2. 对的人一定会出现你的前程里，
3. 不要满足于当下
