python基础
  (1) 数据类型和变量
    整数
      python可以处理任意大小的整数。有时使用十六进制，以0x开头前缀
    浮点数
      即小数
    字符串
      以单/双引号括起来的任意文本。
      转义字符 \ 简化转义：r'~'
      换行\n可以用'''...'''的格式    
    布尔值
      True/False直接表示布尔值注意大小写
      and/or/not
    空值
      None表示
    变量
      变量名不以数字开头
    常量

  (2) 字符串和编码
    字符编码：
      ASCII GB2312 Unicode UTF-8
    字符串:
      字符以Unicode编码，也就是说python字符串支持多语言
      ord()命函数获取字符的正数表示，chr()函数将编码转换为对应字符
      字符串类型：str文本 bytes二进制(使用带前缀b的单/双引号表示)
      区分：'ABC' b'ABC'
      转换格式：'str'.encode('bytes')/b'bytes'.decode('str')
      len()函数计算str字符，bytes字节数
      应坚持使用UTF-8对str/bytes转换
      文前：
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
    格式化
      使用%格式化字符串
        常见占位符：%d %f %s %x
        若%是普通字符，%%

  (3) list和tuple
    list
      一种有序的集合
      追加元素：list append('str') 插入指定位置：list insert(i,'str') 删除末尾:list.pop() 'str' 删除指定：list.pop(i)  'str' 替换 list[i]='str'
      list中元素数据类型可以不同，可以是另一个list
    tuple
      一旦初始化不能修改
      代码更安全。尽量使用tuple
      tuple陷阱 tuple只有一个元素时，需要加',',否则会歧义
      tuple的不变是指向不变，比如tuple的一个元素list类型，其中元素改变会是的tuple改变

  (4) 条件循环
    条件判断
      if语句
      >>>age = 20
        if age >= 18:
            print('your age is', age)
            print('adult')
        elif age>=6:
            print('teenager')
        else:
            print('kid')

    input
    >>>s = input('birth: ')      #input返回数据类型str，不能很整数比较
      birth = int(s)            #所以使用一次数据转换/
      if birth < 2000:
          print('00前')
      else:
          print('00后')

  (5) 循环
    for...in循环
    >>>names = ['Michael', 'Bob', 'Tracy']
      for name in names:
          print(name)
          sum = 0
      for x in range(101):
          sum = sum + x
          print(sum)

    while循环
    >>>sum = 0
      n = 99
      while n > 0:
          sum = sum + n
          n = n - 2
      print(sum)

    break
    可以提前退出循环。
    >>>n = 1
      while n <= 100:
          if n > 10: # 当n = 11时，条件满足，执行break语句
              break # break语句会结束当前循环
          print(n)
          n = n + 1
      print('END')

    continue
    跳过当前循环进入下一次
    >>>n = 0
      while n < 10:
          n = n + 1
          if n % 2 == 0:  # 如果n是偶数，执行continue语句
              continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
          print(n)

  (6) 使用dict和set(key-value存储结构)
    dict
      python内置了字典：dict的支持，dictionary使用键值存储
      >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
      >>> d['Michael']
      95

      通过key将数据放入dict、key的覆盖：
      >>> d['Jack'] = 90
      >>> d['Jack']
      90
      >>> d['Jack'] = 88
      >>> d['Jack']
      88

      如果key不存在，dict就会报错：
      >>> d['Thomas']
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      KeyError: 'Thomas'

      避免key不存在的错误两种方法：
      >>> 'Thomas' in d
      False
      >>> d.get('Thomas')
      >>> d.get('Thomas', -1)
      -1

      删除key使用pop(key)
      >>> d.pop('Bob')
      75
      >>> d
      {'Michael': 95, 'Tracy': 85}

      dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
      >>> key = [1, 2, 3]
      >>> d[key] = 'a list'
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      TypeError: unhashable type: 'list'

    set
      set也是一组key的集合，但不存储value
      没有重复的key
      set.add(key)/set.remove(key)
      s1&s2,s1|s2
