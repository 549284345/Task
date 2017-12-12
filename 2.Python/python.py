import copy

# 同时存在2个版本python，可使用CMD调用不同的解释器
python -2 #启动python 2
python -3 #启动python 3
# 使用pip为不同版本的python安装
python -2 -m pip install xxx
python -3 -m pip install xxx

# 同时遍历2个列表
for (i, j) in zip([1,2,3],['a','b','c']): # zip将多个列表打包成元组列表[(1, 'a'), (2, 'b'), (3, 'c')]
    print(str(j) + str(i))



# 单下划线前缀，比如：_foo，这类函数当做module时，如果使用from module import _foo将无法被导入
# 前后双瞎花钱，比如:__init()__，只是为了区分系统函数名和当前脚本函数名


# 深拷贝，浅拷贝
a=['a','b',1,[1,2,3]]
b = a                  # 对象赋值，所有改动都会联动

a=['a','b',1,[1,2,3]]
b = copy.copy(a)       # 浅拷贝，引用地址，对于可变量list、dict，浅拷贝后内存引用地址不变

# 2个字典合并
dict(dic1, **dict2)   # 返回一个新的字典

################# 迭代器和生成器 ######################
# 迭代器
# 迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
x = [1, 2, 3]  
y = iter(x)         # 创建迭代器
y.next(y)           # 从第一个元素开始迭代，系统会依次将迭代的值读入内存
                    # 避免一次性读取大量数据占用内存，当迭代到最后一个元素继续迭代会报错

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")


# 生成器
# 好处：在使用大量数据时，比如List等，不用一次性占用大量内存。
def foo(max):
	while n < max:
		yield n         # 每次只需到yield处便返回一个迭代值，下次继续从yield下执行
		n = n+1         # 从而产生一个类似“中断”效果

for n in foo(10):   # 此处并没将foo当做函数，而是一个迭代对象，因为foo包含关键字yield
	print(n)



################################# 函数 ##################################
# 函数参数中：strings, tuples, 和 numbers 是不可更改的对象，即传进的是值；
#             而 list,dict 等传进去的相当于指针，是可以对其进行修改的
a = 10
b = [1]
foo(a) # 不能更改a的值
foo(b) # 可以更改b的值

# 指定参数关键字
foo(age= 20, name = 'jack')

# 定义函数默认参数
def foo(age,name,id = 0)

# 多参数函数
# 在函数参数过多时，通常会使用*args,**kwars这种类型
def fun(*args, **kwargs):         # *args表示多个“无名”的参数，因其参数不可更改，所以其类型是元组
    print ('args = ', args)       
    print ('kwargs = ', kwargs)   # **kwargs表示每个“有名字”参数的集合，即指定参数的会以字典形式，所以其类型是一个字典


# 本模块的一个入口
if __name__ == '__main__':   # 在本模块内__name__ = "__name__",而当模块相互调用的时候本模块的__name__ = "模块名"
    foo(1,2,3,4)                              # args = (1,2,3,4)         kwargs = {}
    foo(a=1,b=2,c=3)                          # args = ()                kwargs = {'a': 1, 'c': 3, 'b': 2}  
    foo(1,2,3,4, a=1,b=2,c=3)                 # args = (1,2,3,4)         kwargs = {'a': 1, 'c': 3, 'b': 2}  
    foo('a', 1, None, a=1, b='2', c=3)        # args = ('a', 1, None)    kwargs = {'a': 1, 'c': 3, 'b': 2}  


# 匿名函数（小函数）
foo = lambda x:x+1  # lambda隐藏了return

# map函数
>>> map(lambda x:x+2, [1, 2, 3])  # [list]作为迭代器，依次传入function中，并将结果添加到一个新的list中
[3, 4, 5]
>>> map(lambda x,y:x+y, [1, 2], [1, 2])
[2, 4]


# filter函数filter(function, itra)
>>> filter(lambda x:x%2==1, [1, 2, 3])  #[list作为迭代器。依次传入function,当为真，则将结果添加到一个新的list中
[1, 3]

# reduce函数reduce(function, itra, init)
>>> reduce(lambda x, y:x+y, [1,2,3,4])      # 依次累计，其中初始值y为0
10
>>> reduce(lambda x, y:x+y, [1,2,3,4], 10)  # 依次累计，其中初始值y为10
20
>>> print("sum:", reduce(lambda x,y:x+y, range(1,101)))
sum:5050
# 累计对象列表中的值
>>reduce(lambda total, signal: total + int(signal.nBytes), self.signal, 0)


########################## 运算符  ##############################
%取余
**指数
//取整
^异或
-取反
<<左移
>>右移

逻辑运算符
x and y # 如果x为false则返回false，否则返回y的计算值
x or  y # 如果x为True则返回x，否则返回y的计算值
not x   # 如果x为True，返回False了如果x为False，则返回True

成员运算符
in      # 如果x在y中，返回True
not in  # 如果x不在y中，返回True

身份运算符
is      # 等同于==
is not  # 等同于!=


########################## 数据结构  ##############################
由于List是可变的，而字符串和元组不能修改，所以list在很多地方可以被用到
list.append() #添加元素到列表末尾
list.insert(i,x) #在i处插入x
list.remove(x)   #删除指定元素
list.pop([i])    #从列表指定位置删除元素，并将其返回。如果没有指定位置，则默认删除最后一个并返回元素
list.clear()     #清空list
list.index(x)    #根据元素返回其list的所在位置
list.sort()      #对列表进行排序
list.count(x)    #统计x在list出现的次数
list.copy()      #返回列表的浅拷贝


list当做栈空间使用
stack = [1,2,3]
stack.append(4)
stack.append(5)  #此时stack = [1,2,3,4,5]
member = stack.pop()      #member = 5,此时stack = [1,2,3,4]

列表推导式
vec = [1,2,3]
[3*x for x in vec]  #依次取出vec中的元素，并执行3*x操作，结果为[3,6,9]

推导式加过滤器
[3*x for x in vec if x>2] #如果元素x>2才执行3*x

嵌套列表
>>> matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
	]
将4*3转为3*4
[[row[i] for row in matrix] for i in range(4)] #首先i = 0,再将row循环执行row[i] = row[0]

######################### 装饰器 ####################################
什么是装饰器？
-- 在不改变源代码的基础上扩展新需求，装饰器本身也是函数，应用高阶函数实现
-- 把被装饰的函数内存地址当参数传入装饰器函数体，通过参数调用被装饰的函数
装饰器原则：
-- 不改变源代码  
-- 因为函数可能在其他地方各种调用，一改动全身
-- 不改变原函数调用顺序 
-- 源代码有自己的逻辑处理
-- 装饰器又叫做语法糖

def total_time(func):                              # func = hell_word
    def wrapper():                                 # 等价于hell_word()
        start_time =time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)               # 打印统计时间
    return wrapper
 
 
# 通过装饰器给hell_word函数装上了统计时间的功能，功能逻辑在装饰器中实现
@total_time                                     
def hello_word():
    time.sleep(0.5)
    print('hello word')
     
if __name__ == '__main__':
    hello_word()

#在调用hello_world()会发现这是一个装饰器，从而先调用total_time,并将hello_world()的函数地址传递给total_time
而total_time中又定义了一个函数wrapper，这个函数内部才会去执行传入的“函数”，而wrapper会在执行return时执行

########################## 数据类型判断 #############################
isinstance(object, classinfo)
参数
    object -- 实例对象。
    classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True

########################## 变量作用域  ##############################
作用域:
	局部作用域
	闭包函数外的函数中
	全局作用域
	内间作用域
解释器查找规则：
	局部->闭包->全局->内建

x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域， g_count在全局可用

def outer():
    o_count = 1  # 闭包函数外的函数中， 0_count在除inner函数外有效
    def inner():
        i_count = 2  # 局部作用域,还在innner函数中有效

Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这这些语句内定义的变量，外部也可以访问，如下代码：

>>>if True:
		msg = 'I am from Runoob'   # msg可以被其他语句访问，但msg如果在函数中，则其他人无法访问

>>> msg
'I am from Runoob'

########################## 内置函数 ################################
a = 10

# 相加
a.__add__(3) # 结果：13
# 取绝对值
a.__abs__()  # 结果：10
# 计算商/余数
a.__divmod__(3) # 结果：(3,1)
# 计算商
a.__floordiv__(3) # 结果：3
# 判断是否相等
a.__eq__(7)
# 判断是否大于等于
a.__ge__(10)
# 判断是否大于
a.__gt__(11)
# 判断是否小于
a.__lt__(9)__



str1 = 'abcd'
str2 = 'A:bcb'

# 右边填充
str1.ljust(10, '@')     # 指定字符串长度，不足用@补齐，结果：abcd@@@@@@
str1.rjust(10,'@')      # 结果：@@@@@@abcd

# 字符串居中，左右填充
str1.center('4', '@')  # 结果：@@abcd@@


# 首字母大写
str1.capitalize()

# 将字符串转为大写
str1.upper()

# 将字符串转为小写
str1.lower()

# 判断字符串是不是全大写
str1.isupper()

# 判断字符串是不是全小写
str1.islower()

# 寻找字符在字符串中首次出现的位置
str1.find('b')
str1.index('b')

# 字符替换
str1.replace('bc', '12')

# 去掉左右两边空格
str1.strip()

# 计算字符出现次数
str1.count('b')

# 字符大小写交换
str1.swapcase()

# 字符串分割，得到一个list
str2.split(':')

# 判断字符起始字符
str1.startswith('A') #结果: True

# 判断字符结束字符
str1.endswith('e')   #结果: Flase





mylist = [1,2]
newlist = [3,4]
# 增加元素
mylist.append(3)

# 删除
mylist.remove(2)
mylist.clear()

# 显示指定位置元素
mylist.pop(0)

# 扩展列表
mylist.extend(newlist)

# 计算元素个数
mylist.count(2)

# 寻找元素位置
mylist.index(3)

# 列表排序
sortedList = mylist.sort()

# 修改列表
mylist[1] = 0


mydict = {}
# 字典赋值
mydict['1'] = 'a'

# 生成字典
mydict .fromkeys([1,2,3],'a')  # 结果：{'1':'a','2':'a','3':'a'}

# 删除字典
mydict.clear()

# 更新字典
mydict.update(1:'aa',2,'bb')

# 修改字典
mydict.setdefault(2)
mydict.setdefault(3,'cc')

# 根据键值查找
mydict[1]
mydict.get(2)

# 生成所有键的对象
mydict.keys()  # 结果:[1,2,3]

# 生成所有值得对象
mydict.values() # 结果：['a','b','c']

# 生成键值关系对象
mydict.items()  # 结果：[(1,'a'), (2, 'b')]


# 文件操作，参数

    r # 只读模式【默认模式，文件必须存在，不存在则抛出异常】
    w # 只写模式【不可读；不存在则创建；存在则清空内容】
    x # 只写模式【不可读；不存在则创建，存在则报错】
    a # 追加模式【可读；   不存在则创建；存在则只追加内容】

# "+" 表示可以同时读写某个文件

    r+ # 读写【可读，可写】
    w+ # 写读【可读，可写】
    x+ # 写读【可读，可写】
    a+ # 写读【可读，可写】

# "b"表示以字节的方式操作

    rb  # 或 r+b
    wb  # 或 w+b
    xb  # 或 w+b
    ab  # 或 a+b

# 格式化字符串
print("I'm %s. I'm %d year old" % ('Vamei', 99))

# 包的导入
根据解释器规则，在名称前加'_'则表示私有（包括变量或者函数或者类），在使用import时无法被导入


# 面向对象
成员变量：普通、私有(成员加'__')、保护（成员前加'_'）
内置属性：
		类的属性：__dict__
		类的文档字符串:__doc__
		类名：__name__
		类定义所在模块：__module__
		类的所有父类构成元素：__bases__

继承写法：
Class Parent:
	'基类'
	_protectMember = 0 #保护变量,只允许类本身和子类访问，不能用于from module import *
	def __init__(self):
		print '调用父类构造函数' # 在调用派生类的构造函数时，不会自动调用父类的构造函数
	def myMethod(self):   # 函数在类中称为‘方法’
		print '调用父类方法'

Class Child(Parent)：
	'子类'
	def myMethod(self):
		print '调用子类方法'  #方法重写，即当父类的函数不满足时，可以重写

Class Child(A, B)：           #多继承
	__privateMember = 0 #私有变量，只有类本身能访问
	def __init__(self, a, b):
		self.a = a      #公开变量
		self.b = b

	def myMethod(self):
		print '调用子类方法'  #方法重写，即当父类的函数不满足时，可以重写（因为python先从派生类查找，找不到再去基类找）
	def __del__(self):        #析构函数，当不再使用对象时销毁，即外部调用del obj时销毁
		class_name = self.__class__.__name__
		print class_name, '销毁'
	def __add__(self, other): #运算符重载
		return Vector(self.a + other.a, self.b + other.b)
运算符重载：两个对象进行基本运算，对象中的成员会进行相应的运算。（前提对象中有类似__add__的方法定义）
访问私有变量方法：object._className__attrName
				即：print _Chilc__privateMember