import copy

# ͬʱ����2���汾python����ʹ��CMD���ò�ͬ�Ľ�����
python -2 #����python 2
python -3 #����python 3
# ʹ��pipΪ��ͬ�汾��python��װ
python -2 -m pip install xxx
python -3 -m pip install xxx

# ͬʱ����2���б�
for (i, j) in zip([1,2,3],['a','b','c']): # zip������б�����Ԫ���б�[(1, 'a'), (2, 'b'), (3, 'c')]
    print(str(j) + str(i))



# ���»���ǰ׺�����磺_foo�����ຯ������moduleʱ�����ʹ��from module import _foo���޷�������
# ǰ��˫Ϲ��Ǯ������:__init()__��ֻ��Ϊ������ϵͳ�������͵�ǰ�ű�������


# �����ǳ����
a=['a','b',1,[1,2,3]]
b = a                  # ����ֵ�����иĶ���������

a=['a','b',1,[1,2,3]]
b = copy.copy(a)       # ǳ���������õ�ַ�����ڿɱ���list��dict��ǳ�������ڴ����õ�ַ����

# 2���ֵ�ϲ�
dict(dic1, **dict2)   # ����һ���µ��ֵ�

################# �������������� ######################
# ������
# ��������һ�����Լ�ס������λ�õĶ��󡣵���������Ӽ��ϵĵ�һ��Ԫ�ؿ�ʼ���ʣ�ֱ�����е�Ԫ�ر������������������ֻ����ǰ������ˡ�
x = [1, 2, 3]  
y = iter(x)         # ����������
y.next(y)           # �ӵ�һ��Ԫ�ؿ�ʼ������ϵͳ�����ν�������ֵ�����ڴ�
                    # ����һ���Զ�ȡ��������ռ���ڴ棬�����������һ��Ԫ�ؼ��������ᱨ��

list=[1,2,3,4]
it = iter(list)    # ��������������
for x in it:
    print (x, end=" ")


# ������
# �ô�����ʹ�ô�������ʱ������List�ȣ�����һ����ռ�ô����ڴ档
def foo(max):
	while n < max:
		yield n         # ÿ��ֻ�赽yield���㷵��һ������ֵ���´μ�����yield��ִ��
		n = n+1         # �Ӷ�����һ�����ơ��жϡ�Ч��

for n in foo(10):   # �˴���û��foo��������������һ������������Ϊfoo�����ؼ���yield
	print(n)



################################# ���� ##################################
# ���������У�strings, tuples, �� numbers �ǲ��ɸ��ĵĶ��󣬼���������ֵ��
#             �� list,dict �ȴ���ȥ���൱��ָ�룬�ǿ��Զ�������޸ĵ�
a = 10
b = [1]
foo(a) # ���ܸ���a��ֵ
foo(b) # ���Ը���b��ֵ

# ָ�������ؼ���
foo(age= 20, name = 'jack')

# ���庯��Ĭ�ϲ���
def foo(age,name,id = 0)

# ���������
# �ں�����������ʱ��ͨ����ʹ��*args,**kwars��������
def fun(*args, **kwargs):         # *args��ʾ������������Ĳ���������������ɸ��ģ�������������Ԫ��
    print ('args = ', args)       
    print ('kwargs = ', kwargs)   # **kwargs��ʾÿ���������֡������ļ��ϣ���ָ�������Ļ����ֵ���ʽ��������������һ���ֵ�


# ��ģ���һ�����
if __name__ == '__main__':   # �ڱ�ģ����__name__ = "__name__",����ģ���໥���õ�ʱ��ģ���__name__ = "ģ����"
    foo(1,2,3,4)                              # args = (1,2,3,4)         kwargs = {}
    foo(a=1,b=2,c=3)                          # args = ()                kwargs = {'a': 1, 'c': 3, 'b': 2}  
    foo(1,2,3,4, a=1,b=2,c=3)                 # args = (1,2,3,4)         kwargs = {'a': 1, 'c': 3, 'b': 2}  
    foo('a', 1, None, a=1, b='2', c=3)        # args = ('a', 1, None)    kwargs = {'a': 1, 'c': 3, 'b': 2}  


# ����������С������
foo = lambda x:x+1  # lambda������return

# map����
>>> map(lambda x:x+2, [1, 2, 3])  # [list]��Ϊ�����������δ���function�У����������ӵ�һ���µ�list��
[3, 4, 5]
>>> map(lambda x,y:x+y, [1, 2], [1, 2])
[2, 4]


# filter����filter(function, itra)
>>> filter(lambda x:x%2==1, [1, 2, 3])  #[list��Ϊ�����������δ���function,��Ϊ�棬�򽫽����ӵ�һ���µ�list��
[1, 3]

# reduce����reduce(function, itra, init)
>>> reduce(lambda x, y:x+y, [1,2,3,4])      # �����ۼƣ����г�ʼֵyΪ0
10
>>> reduce(lambda x, y:x+y, [1,2,3,4], 10)  # �����ۼƣ����г�ʼֵyΪ10
20
>>> print("sum:", reduce(lambda x,y:x+y, range(1,101)))
sum:5050
# �ۼƶ����б��е�ֵ
>>reduce(lambda total, signal: total + int(signal.nBytes), self.signal, 0)


########################## �����  ##############################
%ȡ��
**ָ��
//ȡ��
^���
-ȡ��
<<����
>>����

�߼������
x and y # ���xΪfalse�򷵻�false�����򷵻�y�ļ���ֵ
x or  y # ���xΪTrue�򷵻�x�����򷵻�y�ļ���ֵ
not x   # ���xΪTrue������False�����xΪFalse���򷵻�True

��Ա�����
in      # ���x��y�У�����True
not in  # ���x����y�У�����True

��������
is      # ��ͬ��==
is not  # ��ͬ��!=


########################## ���ݽṹ  ##############################
����List�ǿɱ�ģ����ַ�����Ԫ�鲻���޸ģ�����list�ںܶ�ط����Ա��õ�
list.append() #���Ԫ�ص��б�ĩβ
list.insert(i,x) #��i������x
list.remove(x)   #ɾ��ָ��Ԫ��
list.pop([i])    #���б�ָ��λ��ɾ��Ԫ�أ������䷵�ء����û��ָ��λ�ã���Ĭ��ɾ�����һ��������Ԫ��
list.clear()     #���list
list.index(x)    #����Ԫ�ط�����list������λ��
list.sort()      #���б��������
list.count(x)    #ͳ��x��list���ֵĴ���
list.copy()      #�����б��ǳ����


list����ջ�ռ�ʹ��
stack = [1,2,3]
stack.append(4)
stack.append(5)  #��ʱstack = [1,2,3,4,5]
member = stack.pop()      #member = 5,��ʱstack = [1,2,3,4]

�б��Ƶ�ʽ
vec = [1,2,3]
[3*x for x in vec]  #����ȡ��vec�е�Ԫ�أ���ִ��3*x���������Ϊ[3,6,9]

�Ƶ�ʽ�ӹ�����
[3*x for x in vec if x>2] #���Ԫ��x>2��ִ��3*x

Ƕ���б�
>>> matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
	]
��4*3תΪ3*4
[[row[i] for row in matrix] for i in range(4)] #����i = 0,�ٽ�rowѭ��ִ��row[i] = row[0]

######################### װ���� ####################################
ʲô��װ������
-- �ڲ��ı�Դ����Ļ�������չ������װ��������Ҳ�Ǻ�����Ӧ�ø߽׺���ʵ��
-- �ѱ�װ�εĺ����ڴ��ַ����������װ���������壬ͨ���������ñ�װ�εĺ���
װ����ԭ��
-- ���ı�Դ����  
-- ��Ϊ���������������ط����ֵ��ã�һ�Ķ�ȫ��
-- ���ı�ԭ��������˳�� 
-- Դ�������Լ����߼�����
-- װ�����ֽ����﷨��

def total_time(func):                              # func = hell_word
    def wrapper():                                 # �ȼ���hell_word()
        start_time =time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)               # ��ӡͳ��ʱ��
    return wrapper
 
 
# ͨ��װ������hell_word����װ����ͳ��ʱ��Ĺ��ܣ������߼���װ������ʵ��
@total_time                                     
def hello_word():
    time.sleep(0.5)
    print('hello word')
     
if __name__ == '__main__':
    hello_word()

#�ڵ���hello_world()�ᷢ������һ��װ�������Ӷ��ȵ���total_time,����hello_world()�ĺ�����ַ���ݸ�total_time
��total_time���ֶ�����һ������wrapper����������ڲ��Ż�ȥִ�д���ġ�����������wrapper����ִ��returnʱִ��

########################## ���������ж� #############################
isinstance(object, classinfo)
����
    object -- ʵ������
    classinfo -- ������ֱ�ӻ����������������ͻ�����������ɵ�Ԫ�顣
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # ��Ԫ���е�һ������ True
True

########################## ����������  ##############################
������:
	�ֲ�������
	�հ�������ĺ�����
	ȫ��������
	�ڼ�������
���������ҹ���
	�ֲ�->�հ�->ȫ��->�ڽ�

x = int(2.9)  # �ڽ�������
 
g_count = 0  # ȫ�������� g_count��ȫ�ֿ���

def outer():
    o_count = 1  # �հ�������ĺ����У� 0_count�ڳ�inner��������Ч
    def inner():
        i_count = 2  # �ֲ�������,����innner��������Ч

Python ��ֻ��ģ�飨module�����ࣨclass���Լ�������def��lambda���Ż������µ�������
�����Ĵ���飨�� if/elif/else/��try/except��for/while�ȣ��ǲ��������µ�������ģ�
Ҳ����˵����Щ����ڶ���ı������ⲿҲ���Է��ʣ����´��룺

>>>if True:
		msg = 'I am from Runoob'   # msg���Ա����������ʣ���msg����ں����У����������޷�����

>>> msg
'I am from Runoob'

########################## ���ú��� ################################
a = 10

# ���
a.__add__(3) # �����13
# ȡ����ֵ
a.__abs__()  # �����10
# ������/����
a.__divmod__(3) # �����(3,1)
# ������
a.__floordiv__(3) # �����3
# �ж��Ƿ����
a.__eq__(7)
# �ж��Ƿ���ڵ���
a.__ge__(10)
# �ж��Ƿ����
a.__gt__(11)
# �ж��Ƿ�С��
a.__lt__(9)__



str1 = 'abcd'
str2 = 'A:bcb'

# �ұ����
str1.ljust(10, '@')     # ָ���ַ������ȣ�������@���룬�����abcd@@@@@@
str1.rjust(10,'@')      # �����@@@@@@abcd

# �ַ������У��������
str1.center('4', '@')  # �����@@abcd@@


# ����ĸ��д
str1.capitalize()

# ���ַ���תΪ��д
str1.upper()

# ���ַ���תΪСд
str1.lower()

# �ж��ַ����ǲ���ȫ��д
str1.isupper()

# �ж��ַ����ǲ���ȫСд
str1.islower()

# Ѱ���ַ����ַ������״γ��ֵ�λ��
str1.find('b')
str1.index('b')

# �ַ��滻
str1.replace('bc', '12')

# ȥ���������߿ո�
str1.strip()

# �����ַ����ִ���
str1.count('b')

# �ַ���Сд����
str1.swapcase()

# �ַ����ָ�õ�һ��list
str2.split(':')

# �ж��ַ���ʼ�ַ�
str1.startswith('A') #���: True

# �ж��ַ������ַ�
str1.endswith('e')   #���: Flase





mylist = [1,2]
newlist = [3,4]
# ����Ԫ��
mylist.append(3)

# ɾ��
mylist.remove(2)
mylist.clear()

# ��ʾָ��λ��Ԫ��
mylist.pop(0)

# ��չ�б�
mylist.extend(newlist)

# ����Ԫ�ظ���
mylist.count(2)

# Ѱ��Ԫ��λ��
mylist.index(3)

# �б�����
sortedList = mylist.sort()

# �޸��б�
mylist[1] = 0


mydict = {}
# �ֵ丳ֵ
mydict['1'] = 'a'

# �����ֵ�
mydict .fromkeys([1,2,3],'a')  # �����{'1':'a','2':'a','3':'a'}

# ɾ���ֵ�
mydict.clear()

# �����ֵ�
mydict.update(1:'aa',2,'bb')

# �޸��ֵ�
mydict.setdefault(2)
mydict.setdefault(3,'cc')

# ���ݼ�ֵ����
mydict[1]
mydict.get(2)

# �������м��Ķ���
mydict.keys()  # ���:[1,2,3]

# ��������ֵ�ö���
mydict.values() # �����['a','b','c']

# ���ɼ�ֵ��ϵ����
mydict.items()  # �����[(1,'a'), (2, 'b')]


# �ļ�����������

    r # ֻ��ģʽ��Ĭ��ģʽ���ļ�������ڣ����������׳��쳣��
    w # ֻдģʽ�����ɶ����������򴴽���������������ݡ�
    x # ֻдģʽ�����ɶ����������򴴽��������򱨴�
    a # ׷��ģʽ���ɶ���   �������򴴽���������ֻ׷�����ݡ�

# "+" ��ʾ����ͬʱ��дĳ���ļ�

    r+ # ��д���ɶ�����д��
    w+ # д�����ɶ�����д��
    x+ # д�����ɶ�����д��
    a+ # д�����ɶ�����д��

# "b"��ʾ���ֽڵķ�ʽ����

    rb  # �� r+b
    wb  # �� w+b
    xb  # �� w+b
    ab  # �� a+b

# ��ʽ���ַ���
print("I'm %s. I'm %d year old" % ('Vamei', 99))

# ���ĵ���
���ݽ���������������ǰ��'_'���ʾ˽�У������������ߺ��������ࣩ����ʹ��importʱ�޷�������


# �������
��Ա��������ͨ��˽��(��Ա��'__')����������Աǰ��'_'��
�������ԣ�
		������ԣ�__dict__
		����ĵ��ַ���:__doc__
		������__name__
		�ඨ������ģ�飺__module__
		������и��๹��Ԫ�أ�__bases__

�̳�д����
Class Parent:
	'����'
	_protectMember = 0 #��������,ֻ�����౾���������ʣ���������from module import *
	def __init__(self):
		print '���ø��๹�캯��' # �ڵ���������Ĺ��캯��ʱ�������Զ����ø���Ĺ��캯��
	def myMethod(self):   # ���������г�Ϊ��������
		print '���ø��෽��'

Class Child(Parent)��
	'����'
	def myMethod(self):
		print '�������෽��'  #������д����������ĺ���������ʱ��������д

Class Child(A, B)��           #��̳�
	__privateMember = 0 #˽�б�����ֻ���౾���ܷ���
	def __init__(self, a, b):
		self.a = a      #��������
		self.b = b

	def myMethod(self):
		print '�������෽��'  #������д����������ĺ���������ʱ��������д����Ϊpython�ȴ���������ң��Ҳ�����ȥ�����ң�
	def __del__(self):        #����������������ʹ�ö���ʱ���٣����ⲿ����del objʱ����
		class_name = self.__class__.__name__
		print class_name, '����'
	def __add__(self, other): #���������
		return Vector(self.a + other.a, self.b + other.b)
��������أ�����������л������㣬�����еĳ�Ա�������Ӧ�����㡣��ǰ�������������__add__�ķ������壩
����˽�б���������object._className__attrName
				����print _Chilc__privateMember