# MIT6.0001-Introduction to CS and Programming in Python Notes?

<br>

# Preface

&emsp;&emsp;下面包含的部分将是笔记，总结和Pset的思路分析。目录如下所示：
- [MIT6.0001-Introduction to CS and Programming in Python Notes?](#mit60001-introduction-to-cs-and-programming-in-python-notes-)
- [Preface](#preface)
- [Notes](#notes)
  * [1.What is Programming](#1what-is-programming)
    + [1.1类与对象](#11----)
    + [1.2表达式和操作符](#12-------)
    + [1.3变量命名](#13----)
  * [2.Branching and Iteration](#2branching-and-iteration)
    + [2.1缩进](#21--)
    + [2.2String](#22string)
    + [2.3input/output](#23input-output)
    + [2.4while和for循环](#24while-for--)
  * [3.String Manipulation, Guess and Check, Approximations, Bisection](#3string-manipulation--guess-and-check--approximations--bisection)
    + [3.1 二分法查找(重点)](#31----------)
    + [3.2牛顿-拉夫逊方法（了解）](#32------------)
  * [4.Decomposition, Abstractions, Functions](#4decomposition--abstractions--functions)
    + [4.1分解与抽象](#41-----)
    + [4.2函数语法和文档说明](#42---------)
      - [4.2.1基础语法](#421----)
      - [4.2.2文档说明](#422----)
      - [4.2.3位置参数和关键词参数](#423----------)
      - [4.2.4默认参数](#424----)
    + [4.3作用范围（重点）](#43--------)
  * [5.Tuples, Lists, Aliasing, Mutability, Cloning](#5tuples--lists--aliasing--mutability--cloning)
    + [5.1元组](#51--)
    + [5.2列表](#52--)
  * [6.Recursion, Dictionaries](#6recursion--dictionaries)
    + [6.1递归（重点）](#61------)
    + [6.2字典](#62--)
  * [7.Testing, Debugging, Exceptions, Assertions](#7testing--debugging--exceptions--assertions)
    + [7.1测试基本概念](#71------)
      - [7.1.1测试分类](#711----)
      - [7.1.2测试方法](#712----)
    + [7.2异常处理](#72----)
      - [7.2.1.try-except-else-finally](#721try-except-else-finally)
      - [7.2.2异常处理策略](#722------)
    + [7.3关于Debug](#73--debug)
  * [8.Object Oriented Programming](#8object-oriented-programming)
    + [1.What is OOP?](#1what-is-oop-)
    + [2.Why OOP?](#2why-oop-)
    + [3.How OOP?](#3how-oop-)
  * [9.Python Classes and Inheritance](#9python-classes-and-inheritance)
    + [9.1get 和 set方法](#91get---set--)
    + [9.2继承](#92--)
    + [9.3重写](#93--)
  * [10 & 11.Understanding Program Efficiency](#10---11understanding-program-efficiency)
    + [10.1如何测量不同算法的优劣？](#101------------)
    + [10.2Big O表示法](#102big-o---)
    + [10.3常见的算法复杂度](#103--------)
    + [11.1常见的复杂度代表](#111--------)
      - [11.1.1 O(1)](#1111-o-1-)
      - [11.1.2 O(logn)](#1112-o-logn-)
      - [11.1.3 O(n)](#1113-o-n-)
      - [11.1.4 O(nlogn)](#1114-o-nlogn-)
      - [11.1.5 O(n^c)](#1115-o-n-c-)
      - [11.1.6 O(c^n)](#1116-o-c-n-)
  * [12.Searching and Sorting algorithms](#12searching-and-sorting-algorithms)
    + [12.1查找算法](#121----)
    + [12.2排序算法](#122----)
- [Summary](#summary)
- [Psets](#psets)
  * [Pset0](#pset0)
  * [Pset1](#pset1)
  * [Pset2](#pset2)
  * [Pset3](#pset3)
  * [Pset4](#pset4)
  * [Pset5](#pset5)
- [Reference](#reference)

<br><br>

# Notes

## 1.What is Programming

### 1.1类与对象

&emsp;&emsp;在Python中，类可以分为基本数据类型和复杂数据类型，他们的区别是类是否可以再分。典型的基本数据类型是int、float、bool、NoneType。

1. int代表整型。比如-1,1等等。
2. float是浮点数。浮点数指的是**一个数字的近似表示，所以在用浮点数作比较等运算的时候需要格外注意**。
3. bool只有两个值，True和False，注意一定是**大写字母开头**。
4. NoneType只有一个值，即None，当一个函数没有返回值或是仅仅是`return`时，函数返回一个None值。

<br>

&emsp;&emsp;在python中，每一个对象都有自己的类型，可以通过`type()`函数来进行查看。比如:

```python
type(0.01)
<class 'float'>
type(None)
<class 'NoneType'>
type(1)
<class 'int'>
type(True)
<class 'bool'>
```

<br>

不同类型之间可以进行转换，比如float()和int()能把语法正确的参数分别转为float和int。比如:

```python
int(3.12) # 截断，而不是四舍五入
3
float(3)
3.0
```

<br>

### 1.2表达式和操作符

&emsp;&emsp;一个简单的表达式为`<object> <opertor> <object>`.比如 `a + b`。

**算术运算符**：

**1.产生结果**

- i {+ - *} j 。如果i和j中至少有一个是float，那么结果就是float。如果都是int，那么结果就是int。
- i / j。结果必为浮点数。
- i {// %}j。// 表示求商，%表示求余。i和j最好都是整数，要不然没什么意义。
- i \*\* j。\*\*表示以i为底，以j为指数的乘方运算。如果i和j中至少有一个是float，那么结果就是float。如果都是int，那么结果就是int。

<br>

**2.优先级**

（） \> \*\*\> \* / \> + - >从左到右依次运算

<br>

**逻辑运算符:**

not \> and \> or

<br>

如果不知道优先级，用（）来解决。

<br>

### 1.3变量命名

&emsp;&emsp;字母数字下划线的组合。数字不能作为首个单词出现，推荐命名时用下划线命名法。应保证可读性好，比如`my_book`。python的关键字如int float等不能作为变量的名称。还需要知道的是常量用大写，并用下划线分隔。类名可以采用驼峰命名法。

<br><br>

## 2.Branching and Iteration

### 2.1缩进

&emsp;&emsp;在Python中，缩进在语义和语法上都很重要。一方面，合理的缩进可以使得代码可读性更好；另一方面，Python会通过缩进来判定代码是不是属于同一个语句块。比如：

```python
if <expression1> :
    code fragements
    
elif <expression2>:
    code fragements
    
    if <expression21>:
        code fragements
    else:
        code fragements
else:
    code fragements
```

<br>

### 2.2String

&emsp;&emsp;String是**不可变量**，也就是**说不能对string的组成部分进行修改**。

比如：

```python
s = "abc"
# 报错，“abc”是不变量，不能修改其成分
# s[0] = f

#  正确，s只是指向了一个新的值
s ="cba"
```

<br>

&emsp;&emsp;在Python中，没有char这种说法；既可以用单引号也可以用双引号来表示String。有时候需要灵活使用，比如：`introduction = " 鲁迅曾经说过，'我家门前有两棵树'"`。

<br>

&emsp;&emsp;在Python中，string支持  + \* 运算，案例如下：

```python
name = "jack"
3*name
'jackjackjack'
name + name
'jackjack'
```

<br>

&emsp;&emsp;string还有其他的用法，len()函数可以查看字符串的长度。

```python
len('abc')
3
```

<br>

&emsp;&emsp;通过索引可以截取字符串的某个字符。默认从0开始，最大不能超过字符串的长度-1。负数表示反着来数，-1表示倒数第一个。可按照如下关系类推：假如a为负数，那么a的索引等价于 `len(字符串) - abs(a)`的索引。

```python
'abc'[0]
'a'
'abc'[1]
'b'
'abc'[2]
'c'
'abc'[-1]
'c'
'abc'[-2]
'b'
'abc'[-3]
'a'
```

<br>

&emsp;&emsp;可以通过切片来截取字符串的子串。比如 `var_str[start:end]`表示取变量var_str的索引从start到end-1的子串。start默认是0，end默认是len(var_str)。当然，也存在`var_str[start:end:step​]`这种用法,step默认为1。

```python
'abcdefg'[0:5:2]
'ace'
'abcdefg'[0:5]
'abcde'
# 去除最后一个字符
'abcdefg'[:-1]
'abcdef'
# 去除第一个字符
'abcdefg'[1:]
'bcdefg'
# 复制一个字符串
'abcdefg'[:]
'abcdefg'
```

<br>

string常用的方法如下:

![image-20210315091932339](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210315091932339.png)

<br>

### 2.3input/output

&emsp;&emsp;input('提示语')函数将接收用户输入并产生一个string。

&emsp;&emsp;print("xxx")函数则是输出字符串到控制台。

<br>

### 2.4while和for循环

while循环和for循环的明显差别是不是知道循环的次数。

常见的for循环是

```python
for i in range(x)：
    code fragments
```

<br>

&emsp;&emsp;这个range函数可依次传入3个参数，start，end，step。start默认是0，step默认是1。假如step是正数，那么循环继续条件是start + step*n \< end。假如是负数，那么循环继续条件是 start + step * n > end 。一句话，不要等于或超过end。

<br>

还有需要知道的是类似于这种情况的存在：

```python
for i in range(x):
    修改x
```

**循环一旦接收x参数开始之后，不会因为修改x，而改变循环的进程**。

<br>

事实上，还可以针对字符串，元组，列表进行循环，以字符串为例：

```python
total = 0
for i in '123456789':
    total +=  int(i)
print(total)
45
```

<br><br>

## 3.String Manipulation, Guess and Check, Approximations, Bisection

### 3.1 二分法查找(重点)

&emsp;&emsp;现实生活中，二分法查找的一个很典型的例子是查字典。每次翻一半书，检查是否和我们查看的首字母匹配，如果不匹配，那么考虑当前页的字母是大了还是小了。如果是大了，那么就翻前半本书；如果小了，那么就翻后半本书。显然，这个比从头开始一页一页查找，要快多了。

demo(猜1到100之内的数字)

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/8

"""
import random

"""
   随机生成1到100的数字,然后由用户输入数字进行猜测,根据用户猜测提醒是否大于随机生成的数字。
"""
# ######################## 手动猜测 ############################
# num = random.randint(1, 100)
# print("Welcome to Guess Number Between 1 and 100 Game!")
# guess = int(input("Please enter your number (between 1  and 100):"))
# guess_num = 1

#  # manually
# while guess != num:
#     guess_num += 1
#     if guess > num:
#         guess = int(input("Oops! your guess  " + str(guess) + " is HIGHER than the answer,try another one:"))
#     else:
#         guess = int(input("Oops! your guess  " + str(guess) + " is LOWER than the answer,try another one:"))
# print("Nice guess,you've guessed for " + str(guess_num) + " times")
# ######################## 手动猜测 ############################

# ######################## 分别用普通的方法(每次在原基础上+1或-1)和二分法猜测 ############################
# from 0  to 100 one by one
num = random.randint(1, 100)
print("Welcome to Guess Number Between 1 and 100 Game!")
print("Try UNUSUAL method!")
# temp用保存guess，方便采用二分法的时候再用
temp = guess = int(input("Please enter your number (between 1  and 100):"))
guess_num = 1

while guess != num:
    guess_num += 1
    if guess > num:

        print("Oops! your guess  " + str(guess) + " is HIGHER than the answer,try another one:" + str(guess - 1))
        guess -= 1
    else:

        print("Oops! your guess  " + str(guess) + " is LOWER than the answer,try another one:" + str(guess + 1))
        guess += 1

print("Nice guess,you've guessed " + str(num) + " for " + str(guess_num) + " times by unusual method ")

print("-------------")
print("Try BISEARCH method!")
# bisearch
guess = temp
guess_num = 1
begin = 0
end = 100
while guess != num:
    guess_num += 1
    if guess > num:
        end = guess - 1
        print(
            "Oops! your guess  " + str(guess) + " is HIGHER than the answer,try another one:" + str((begin + end) // 2))

    else:
        begin = guess + 1
        print(
            "Oops! your guess  " + str(guess) + " is LOWER than the answer,try another one:" + str((begin + end) // 2))
    guess = (begin + end) // 2

print("Nice guess,you've guessed " + str(num) + " for " + str(guess_num) + " times by bisearch method ")

```

<br>

&emsp;&emsp;这部分的典型案例还可以参照MIT6.0001 pset1的第3题，链接地址<a href="https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf" target="_blank">Pset1</a>。

<br>

### 3.2牛顿-拉夫逊方法（了解）

&emsp;&emsp;它是牛顿在17世纪提出的一种在实数域和域上近似求解方程的方法。详情可参照百度百科<a href="https://baike.baidu.com/item/%E7%89%9B%E9%A1%BF%E8%BF%AD%E4%BB%A3%E6%B3%95/10887580" target="_blank">牛顿-拉夫逊方法</a>。

<br><br>

## 4.Decomposition, Abstractions, Functions

### 4.1分解与抽象

&emsp;&emsp;分解的目的是为了让代码易于重用，相互独立，协同工作。明显的就是将很长的代码分解为各个独立的函数。老师在课上的例子非常易懂。奥运会的投影工作不是由一个巨大的投影仪完成的，而是由若干个小投影仪完成的，它们完成的工作各不相同，共同完成整个奥运会的投影工作。这么做的原因是：首先巨大的投影仪造价大，设计麻烦，不利于重用，其实这个就对应了又长又臭的主函数。其次，不同的工作人员可以管理不同的投影仪，如果某个部分出问题，可以方便快速定位解决，这其实就是对应于谁设计的函数由谁负责。

&emsp;&emsp;抽象的目的是为了隐藏不必要的细节。买电脑的用户大概率不想知道电脑是怎样组装的，这就是隐藏细节。

<br>

### 4.2函数语法和文档说明

&emsp;&emsp;首先需要声明的是，在python中，**函数也可以当做是变量**，而每个函数都要有返回值，如果没有显式地写 `return 值`，或是 仅仅写`return`，那么返回的值是None，类型为NoneType。

```python
def ok():
    return
type(ok())
<class 'NoneType'>
type(ok)
<class 'function'>
```

<br>

#### 4.2.1基础语法

```python
def functionname(参数列表):
    函数体

# e.g 
def greeting(name)：
    return "hello"+str(name)
```

<br>

#### 4.2.2文档说明

&emsp;&emsp;为了让别人知道函数该怎么用，应该给函数写注释，比如函数是干啥的，参数是什么类型的，返回的值是怎么样的。**像python这种非强类型的语言，这么做就相当有必要**。

具体案例如下所示：

```python
def greeting(name):
    """ 给人打招呼
    :param name:名称，推荐是string
    :return : 招呼语
    """
    return "hello"+str(name)
```

当你的python代码已经运行了之后，可以在python控制台输入`help(greeting)`,会出现

>  给人打招呼
>
>  :param name:名称，推荐是string
>
>  :return : 招呼语

<br>

#### 4.2.3位置参数和关键词参数

```python
def marriage(bridegroom,bride):
    return str(bridegroom)+"和"+str(bride)+"结婚"
```

&emsp;&emsp;像上面这种函数，我们如果这样传参`marriage("jack","rose")`，就是位置参数传参。当然也可以这样传参`marriage(bridge="rose",bridegroom="jack")`，即关键词参数传参，这样传参的好处是不受位置影响，可读性更好。当然，当参数多了以后，这样做也可能显得复杂。

&emsp;&emsp;还有一种就是两种方式混合使用，在这种情况下，要求**关键词参数的后面不能出现位置参数**。也就是`marriage("jack",bride="rose")`**可以**，而`marriage(bridegroom="jack","rose")`**不行**。

<br>

#### 4.2.4默认参数

&emsp;&emsp;函数声明的时候可以给形式参数设置默认值，要求是**设置了默认值的形式参数不能排在未设置形式参数的前面**。比如：

```python
def marriage(bridegroom,bride="beauty"):
    return str(bridegroom)+"和"+str(bride)+"结婚"
```

我们调用的时候，可以`marriage("jack")`,在这种情况下，bride默认是beauty。当然也可以像正常那样调用`marriage("jack","rose")`。

<br>

### 4.3作用范围（重点）

&emsp;&emsp;再次说明，函数也可以当做是变量。如果想知道变量的作用范围，那么就需要知道**栈帧**。简单来说，栈帧会存储属于**同一个函数作用域**的变量。当一个函数被调用时，就会创建一个栈帧，栈帧里面的变量可以是传给函数的形参，也可以是函数内部自己声明的局部变量。当访问一个变量时，会在本栈帧寻找变量，如果没找到，那么会在创建该栈帧的上一个栈帧寻找。

&emsp;&emsp;这一部分，没什么好说的，将老师在课上提到的例子，如

```python
# e.g1
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f( x )

# e.g2
def func_a():
    print ('inside func_a') 
    
def func_b(y):
    print ('inside func_b')
    return y

def func_c(z):
    print ('inside func_c')
    return z()

print (func_a())
print (5 + func_b(2))
print (func_c(func_a))

#e.g3
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

x = 3
z = g(x)
```

在  <a href="http://www.pythontutor.com/" target="_blank">pythontutor</a>里面跑一跑，加深印象。

再三说明，函数可以当做是变量，当函数没有带()号的时候，就可以当做是变量使用，带()的时候，就当做是函数使用。

有一个错误的例子，其实是告诉我们，要好好设计变量的作用域：

```python
def h(y):
      x += 1
        
x = 5
h(x)
print(x)
```

这个例子会报错的原因 先到主栈帧访问x，之后却又到h栈帧声明一个x的变量。至于为什么报错，不知道。

<br>

**特别注意，在python中，变量作用范围是看是否处于一个栈帧，简单来说是不是在一个函数内，这与java的语句块的局部变量不能在语句块访问完全不一样**。

<br><br>

## 5.Tuples, Lists, Aliasing, Mutability, Cloning

&emsp;&emsp;这个部分重点介绍元组（Tuple）和列表（List）这两个复杂类型以及通过List来讲别名，可变性和克隆。

<br>

### 5.1元组

&emsp;&emsp;一个元组就是一条数据，**由于元组是不可变量，所以无法对元组内部的数据进行修改**。元组有分号进行分隔，然后用圆括号包裹。比如：

```python
# 空元组
t1 = ()

# 只有一个元素的元组,注意必须要有逗号，因为这是为了 和 "jack"这种字符串区分
t2 = ("jack",)

t3 = ("jack",13)

# 不打圆括号也是可以的,但是传参的时候需要注意
t4 = "jack",13
```

<br>

和string类似，元组也可以进行\*,拼接，索引，切片和取长度。

```python
t1  = (1, "two", 3)
t2 = (t1,3.25)
print(3*t1)
(1, 'two', 3, 1, 'two', 3, 1, 'two', 3)
print(t1+t2)
(1, 'two', 3, (1, 'two', 3), 3.25)
print((t1+t2)[3])
(1, 'two', 3)
print((t1+t2)[2:5])
(3, (1, 'two', 3), 3.25)
print(len(t1+t2))
5
```

<br>

和string类似，元组也可以被用来迭代。

```python
def intersect(t1,t2):
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

print(intersect((1,3,5),(3,6,9)))
(3,)
```

<br>

&emsp;&emsp;元组很常见的用法一是针对一种运算，该运算的输入的所有参数名和输出的参数名是一模一样的；而输出的参数在计算的过程中对输入的参数产生了依赖。比如：

![image-20210308153353323](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308153353323.png)

&emsp;&emsp;像上面这种案例，如果直接用python代码像盒子那样写的话是不行的，因为z的结果是不正确的。而利用元组这可以很好的完成这个任务`x , y , z = y , z , x`。

&emsp;&emsp;元组还有一种用法就是返回一条数据，比如：

```python
def findExtremeDivisor(n1, n2):
    """
    找到n1和n2的最小公因子 和 最大公因子，如果不存在则返回(None,None)
    最小公因子不包括1
    """
    min_divisor, max_divisor = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if min_divisor is None:
                min_divisor = i
            max_divisor = i

    #  元组可以不用打括号
    return min_divisor, max_divisor
```

<br>

### 5.2列表

&emsp;&emsp;列表也支持，* ，拼接，索引，切片和取长度和用来迭代。最重要的是列表是**可变的**，这就意味着可以对列表的元素进行修改,比如：

```python
L2 = [1,2,3]
L2[0] = 0
# 此时 L2 = [0,2,3]
# 而 其他不可变的复杂类型比如String,元组则不能这样做
```

列表的常见用法：

append

```python
L1 = [1,2,3]
L2 = [4,5,6]
L1.append(L2)
print(L1)
[1, 2, 3, [4, 5, 6]]
```

extend

```python
L1 = [1,2,3]
L2 = [4,5,6]
L1.extend(L2)
print(L1)
[1, 2, 3, 4, 5, 6]
```

remove（e）和 del(L(index)) 和 pop

```python
L = [1,1,3,4]
L.remove(1) # 删除列表中第一个元素为1的元素
print(L)
[1,3,4]
del(L[1]) # 删除列表索引为1的元素
print(L)
[1,4]
last_one = L.pop() # 删除列表最后一个元素，并返回它
print(last_one)
4
print(L)
[1]
```

<br>

列表一些其他用法如下所示：

![image-20210308160758985](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308160758985.png)

<br>

&emsp;&emsp;list，string，tuple这三个很像的相同点是都支持\*，+（拼接），索引，切片，用len求长度，和用于for循环。但是string的元素是一个个单字符，是不可变的，tuple更像是一条数据，而且它也是不可变的，list最大的特点是它是可变的，而且通常而言，它的元素都是一个类型。

![image-20210315091428768](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210315091428768.png)

<br>

list和string之间存在一定的转化，比如：

```python
list("ab c") #将字符串 ”ab c"转为 ['a', 'b', ' ', 'c']
"abc cba".split(' ') # 根据split输入的实参对字符串进行分割，并返回分割后的列表 ['abc', 'cba']。默认为所有的空白符，包括空格、换行(\n)、制表符(\t)等。

"".join(["a","b","c"]) # 'abc'
"_".join(["a","b","c"]) # 'a_b_c'

```

<br>

最后说一下别名和克隆：

```python
list1 = ["a","b","c"]
# list1的别名 list2
list2 = list1
# 通过切片或是 list方法来克隆
list3 = list1[:]
list4 = list(list1)
```

区别就是下面这个区别：

![image-20210308163333036](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308163333036.png)

<br>

下面是深克隆和浅克隆的区别：

```python
import copy
list1 =[1,2,3,4]
list2 = [5,6,7,8]
list3 = [list1,list2]
list4 = list3[:]  #浅克隆
list5 = copy.deepcopy(list3) #深克隆
```

![image-20210308175059237](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308175059237.png)

<br>

&emsp;&emsp;还有一点，在对列表进行迭代的时候，不要试图增加或删除的列表的元素，因为这可能导致一些比较奇葩的结果。究其根本是因为进行for循环后，会有一个计数器记录循环次数（也即下次访问索引），初始为0，每循环一次，就会加1，而循环终止的条件是**计数器的记录的次数大于等于当前列表的长度**。比如:

```python
list1 = [1,2,3]
for ele in list1:
    print(ele)
    if ele ==1 :
        list1.remove(1)
 
# 结果为
# 1
# 3
# 而不是
# 1
# 2
# 3
# 是因为删掉1 之后，索引变为1，而当前列表为[2,3],长度为1.所以当打印1之后，将打印list1[1],即3。
```

<br><br>

## 6.Recursion, Dictionaries

### 6.1递归（重点）

&emsp;&emsp;递归的基本思想是针对一个问题，把它划分为若干更小规模的相同性质的问题，如此往复下去，直到问题规模小到可以直接解决。常见的诸如n的阶乘，斐波拉契数列，汉罗塔，字符串回文问题。递归的伪代码如下：

```python

def recursion_pseudo_code( ...parameters...,size,...parameters...) #其中至少有一个参数必与问题规模有关
    if base_case ： # 问题规模小到可以直接解决时，称该问题为 base case
       do something
    else：
        ....recursion_pseudo_code( ...parameters...,size-x1,...parameters...)....
        ....recursion_pseudo_code( ...parameters...,size-x2,...parameters...)....
        ....recursion_pseudo_code( ...parameters...,size-xn,...parameters...)....
   
```

<br>

n的阶层

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/8

"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))

```

<br>

汉罗塔

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/7

"""

"""
   汉罗塔问题
              假设有三根柱子,根据位置命名为 1,2,3
              初始情况:所有的圆盘都在第1根柱子上,每个圆盘的大小不同,小的圆盘都在较大的圆盘上。
              
              要求：将所有的圆盘都移动到第3根柱子上,而且在移动期间，只能是小的圆盘在大的圆盘上面。
              
             
              
              解决思路： 递归解决
                根据递归思想,1是将问题变成更小的相同问题,2找到最平凡的情况（base case）
              1. 假设现在有n个圆盘所处的位置叫做from_position,
                 那么将n-1个圆盘从from_position移动到空闲spare_position的柱子上，
                 然后将最大的第n个圆盘从from_position移动到目标to_position的柱子上,
                 最后将n-1个圆盘从spare_position移动到目标to_position的柱子上
                  
              2.base case 当圆盘的个数为1个时(from_position)，直接将圆盘移动到目标(to_position)位置上。
              
              从中可以看到，至少需要4个参数,n表示圆盘的个数,其他三个是方位，即n个圆盘from_position哪里移动到(to_position)哪里，spare_position表是空闲的位置。
              
"""


def hanoi(n, from_position, spare_position, to_position):
    """
    :param n:   n表示盘子的数量
    :param from_position: n个盘子的初始位置
    :param spare_position: 空闲的柱子位置
    :param to_position: n个盘子将要移动到那个位置
    """
    if n == 1:
        print("将盘子从柱子" + str(from_position) + "移动到" + str(to_position))
    else:
        hanoi(n - 1, from_position, to_position, spare_position)
        hanoi(1, from_position, spare_position, to_position)
        hanoi(n - 1, spare_position, from_position, to_position)


# 在原有的基础上,增加形式参数：已有的移动步数,并返回执行一个hanoi_with_usability之后已有的移动步数
def hanoi_with_usability(n, from_position, spare_position, to_position, move_num):
    if n == 1:
        move_num = move_num + 1
        print("第" + str(move_num) + "步:将盘子从柱子" + str(from_position) + "移动到" + str(to_position))
        return move_num
    else:
        move_num = hanoi_with_usability(n - 1, from_position, to_position, spare_position, move_num)
        move_num = hanoi_with_usability(1, from_position, spare_position, to_position, move_num)
        move_num = hanoi_with_usability(n - 1, spare_position, from_position, to_position, move_num)
        return move_num


if __name__ == '__main__':
    # hanoi(5, 1, 2, 3)
    hanoi_with_usability(5, 1, 2, 3, 0)

```

<br>

字符串回文

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/7

"""

"""
   忽略大小写,空格,标点符号。检查是否是回文
"""


def is_palindrome(s):
    def to_chars(s):
        s = s.lower()  # 忽略大小写
        letters = ""
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz": # 忽略符号,空格符等
                letters += char

        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


if __name__ == '__main__':
    print(is_palindrome("dogGOD"))
    print(is_palindrome("dogOOD"))
    print(is_palindrome("Able	was	I,	ere	I	saw	Elba"))
    print(is_palindrome("Are	we	not	drawn	onward,	we	few,	drawn	onward	to	new	era?"))

```

<br><br>

&emsp;&emsp;这里需要提一句，如果一个问题能够分别用迭代和递归来解决，那么从可读性上，通常是递归更好。而从效率上，可能是迭代更好，当然，可能存在通过修改递归的代码，也可以保证效率。比如斐波拉契数列问题，如果直接用递归来解决，那么当问题规模很大的时候，效率将非常低，究其原因是用递归的时候重复解决了相同的问题。一种解决方法是，利用字典（6.2节）来记录结果，避免相同的问题再次计算。具体案例如下：

斐波拉契数列（兔子数列）

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/7

"""
import time

"""
   问题描述:  
   有一对一公一母的兔子被投放到野外。这些兔子一个月成熟，永远不会死。雌兔第1个月底成熟后，第2个月初怀孕，第3月初产下
   一对新的一公一母的兔子。此后，该雌兔将在第4月初，5月初...n月初都产下一对一公一母的兔子。由该雌兔生下的雌兔后代和该雌兔是
   一模一样的成熟，分娩，再分娩。
   问：6个月结束后的7月初有多少只雌兔          

"""


def recursive_fibonacci_number(n):
    """

    :param n: n表示  第n月初
    :return:  n月初的雌兔
    """
    # 第1月初 和 第2月初,最初的雌兔并未产生小兔,所以雌兔只有它自己
    if n == 1 or n == 2:
        return 1

    #   n月初的雌兔   = n - 1 月初的雌兔 + n月初生下的新兔
    #   而 n月初生下的新兔 = n-1月初怀孕的雌兔 = n-2月初的雌兔
    #   因此  n月初的雌兔  = n - 1 月初的雌兔 +  n-2月初的雌兔
    return recursive_fibonacci_number(n - 1) + recursive_fibonacci_number(n - 2)


def iterative__fibonacci_number(n):
    """
       :param n: n表示  第n月初
       :return:  n月初的雌兔
    """

    #  n月初的雌兔  = n - 1 月初的雌兔 +  n-2月初的雌兔
    result_n = 1  # n月初的雌兔
    result_n_1 = 1  # n-1月初的雌兔
    result_n_2 = 1  # n-2月初的雌兔
    count = 1  # 第count月初
    temp = 0  # 可以理解temp 是记录 result_n_2 的上上月初的兔子 。当n == 3时， 0月初时，temp只是一个占位符，即0
    while count <= n:
        if count == 1:
            result_n = 1
        elif count == 2:
            result_n_1 = 1
            result_n = 1
        elif count == 3:
            temp = 0  # 这里起占位符的作用，当count大于3的时候，result_n_2需要这个temp
            result_n_2 = 1
            result_n_1 = 1
            result_n = result_n_1 + result_n_2
        else:
            result_n = result_n + result_n_1
            result_n_1 = result_n_1 + result_n_2
            result_n_2, temp = result_n_2 + temp, result_n_2

        count += 1

    return result_n


# dictionary 用于记录 fib(x) ,初始值为 {1:1,,2:1}
def recursive_fibonacci_number_efficient(n, dictionary):
    if n in dictionary:
        return dictionary[n]
    else:
        ans = recursive_fibonacci_number_efficient(n - 1, dictionary) + recursive_fibonacci_number_efficient(n - 2,
                                                                                                             dictionary)
        dictionary[n] = ans
        return ans


if __name__ == '__main__':
    # print(recursive_fibonacci_number(1))
    # print(iterative__fibonacci_number(1))
    #
    # print(recursive_fibonacci_number(2))
    # print(iterative__fibonacci_number(2))
    #
    # print(recursive_fibonacci_number(7))  # 13
    # print(iterative__fibonacci_number(7))  # 13

    time_start = int(time.time() * 1000)
    print(recursive_fibonacci_number(30))
    time_end = int(time.time() * 1000)
    print('recursive:totally cost', time_end - time_start, "ms")

    time_start = int(time.time() * 1000)
    print(iterative__fibonacci_number(30))
    time_end = int(time.time() * 1000)
    print('iterative:totally cost', time_end - time_start, "ms")

    time_start = int(time.time() * 1000)
    dictionary = {1: 1, 2: 1}
    print(recursive_fibonacci_number_efficient(30, dictionary))
    time_end = int(time.time() * 1000)
    print('recursive_efficient:totally cost', time_end - time_start, "ms")
```

当问题规模为30时，会发现普通的递归方法，比优化后的递归方法和迭代法效率要低得多。

![image-20210308173846061](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308173846061.png)

因为普通的递归方法，花在解决已经解决过的相同问题上的时间是额外的支出。比如

![image-20210308174110008](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308174110008.png)

<br>

### 6.2字典

&emsp;&emsp;字典，简单来说就是一个存储KV对的一个可变的数据结构。要求Key必须是hashtable，至于什么是hashtable，这个暂时不管。不过需要知道的是，所有python内置的不可变的类型均为hashtable，比如int，float，string，tuple；所有python内置的可变的类型均不是hashtable，比如list。再补充一点，我们自己写的类都是hashable的。

&emsp;&emsp;慎用float来当做key。tuple来当做key是很常见的东西，因为tuple本身是有个复杂类型，可以包含很多信息，这些信息综合来当做key。

&emsp;&emsp;显然，key是不能重复的，而value可能是重复的。

&emsp;&emsp;字典是可变类型，也可以对字典进行迭代（其实是对字典的keys进行迭代），不过迭代的顺序与存储元素的顺序不一定是一致的，而且字典也没有索引这一说。`if k in dic`和`for k in dic`都指的是key。

这部分常见的方法如下：

![image-20210308182726740](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210308182726740.png)

<br><br>

## 7.Testing, Debugging, Exceptions, Assertions

&emsp;&emsp;这个部分简单阐述测试的一些基本概念，然后讲述异常的处理，如try-except 和 assert。

### 7.1测试基本概念

#### 7.1.1测试分类

&emsp;&emsp;测试可以分为三类，即单元测试，回归测试，集成测试。

1. 单元测试：针对代码的最小单元进行测试，确保它能正常工作。所谓的最小单元通常指的是一个函数或是一个类。
2. 回归测试：当bug修复以后，要对之前已经测试过的单元进行重测，避免因为bug的修复而导致其他bug的产生进而破坏之前已经验证通过的代码的正常运行。
3. 集成测试：当单元测试通过后，需要对整个程序进行测试，如果验证不通过，那么显然需要找到产生问题的单元，再次进行测试。

这三部分主要是有个印象，毕竟测试真的要拿出来讲的话，那就得讲很多节课了，应该避免知识的黑洞。

<br>

#### 7.1.2测试方法

&emsp;&emsp;测试的方法可以分为白盒测试和黑盒测试。

1. 白盒测试：准确知道代码的具体结构，测试代码的所有路径是否像预期那样正常工作。白盒测试是早期的测试工作，比如在单元测试的时候进行，而且执行这部分测试的人多为代码程序的开发者。这部分测试常见的方法有基本路径覆盖法和逻辑覆盖法。
2. 黑盒测试：与白盒测试的不同，黑盒测试是不需要知道代码的具体信息的，这个部分主要是根据需求规格说明书进行测试。黑盒测试是后期的测试工作，执行这部分测试的人则通常是有专门的测试人员进行测试。这部分测试常见的方法有等价划分法，边界值划分法，因果图法等等。

一句话，记住黑白盒测试的基本概念就行了，避免知识的无限黑洞，抓住主要问题，忽略次要矛盾。

<br>

### 7.2异常处理

#### 7.2.1.try-except-else-finally

&emsp;&emsp;这是最标准的处理异常的结构，伪代码如下:

```python
try:
#  将会出现异常的代码
except ErrorType1:
# 当碰到异常类型  ErrorType1时的处理操作
except ErrorType2:
# 当碰到异常类型  ErrorType2时的处理操作    
# ......
except ErrorTypen:
# 当碰到异常类型  ErrorTypen时的处理操作  
except:
# 其他异常的处理操作
else:
# 代码正常运行时，将会执行else的代码
finally:
# 无论是否发生异常，都将执行finally里面的代码，这类操作常针对文件I/O等消耗资源的工作
```

&emsp;&emsp;这个部分我觉得比较鸡肋的是else语句，该else的语句设计的初衷是如果将这部分代码放在try里面，然后就因为这部分代码报错就不好了。嗯，反正我是觉得如果自己对代码有把握，直接写到try里面就好了。

&emsp;&emsp;还有就是except是捕捉错误的，这类错误是我们预期的错误，比如整数除法的时候，参数为0的情况，那么我们就应该针对这种`ZeroDivisionError`进行处理，还有就是参数如果不是数字，比如说是字符串，那么我们就应该针对这种`ValueError`进行处理。而那些不是我们预期的，影响了程序正常运行的错误，反而不对其进行处理较好，在发生错误之后进行代码修复即可。

<br>

#### 7.2.2异常处理策略

&emsp;&emsp;7.2.1节已经稍微谈到异常处理了，这里展开来讲。首选需要知道，异常的常见种类有：


- NameError：访问未声明的变量所致的异常。
- ValueError：参数类型正确，但是参数不符合要求的异常。比如只有非负数才能进行开方。
- TypeError:  参数类型不满足需求的异常。
- ZeroDivisionError：除数为0时导致的异常。
- AssertionError ：当预期结果和实际结果不符，将抛出此类异常。
- AttributeError:访问对象的不存在的属性，将抛出此类异常。

<br>

**方式1：**

认真写方法的文档，标注参数的输入类型和限制，返回的类型等等。**这个非常重要**，特别是对于Python这种弱类型以及解释性语言来说。像java者这种编译型的强类型语言，如果传参的参数类型不对，在编译阶段就会报错的。

**方式2：**

在自己预期范围的错误，就自己处理。不是自己预期的错误，不如让它直接报错，然后修复代码。不建议，用打印语句来处理错误。针对那种有返回值的函数，打印语句的话，其实就是返回了一个None。而如果返回一个特殊值，可以是可以，但是这样的话，代码的调用方要做特殊处理，比较麻烦。这种处理的方式可以采用一种`raise`语句，即**显式抛出一种我们决定的异常**。

**方式3：**

采用Assert语句。该语句主要检查输入是否和预期的一样，比如类型，长度等等。该语句也可以在测试的时候验证实际输出结果和预期结果是否一致。

<br>

### 7.3关于Debug

1. 建议写一部分，测一部分。
2. 出现bug，如果急躁，就去冷静冷静。
3. 使用debug工具，打断点。
4. 查看stackoverflow等论坛。
5. 放一放，明天再看。
6. 问问其他人。

<br><br>

## 8.Object Oriented Programming

### 1.What is OOP?

&emsp;&emsp;OOP就是面向对象编程，在python中处处皆为对象，比如已经学到的简单数据类型（int，float)和复杂的数据类型，如string，list，tuple，dictionary都是对象。

<br>

### 2.Why OOP?

&emsp;&emsp;为什么要面向对象编程呢？首先这符合人类对事物的认知，著名香港电影《大话西游》有句台词叫做,"那个人好像一条狗哦"，里面就涉及到了两个对象：人和狗。一个思想如果能够普世，才有了发展的基础。

&emsp;&emsp;当然，OOP除了符合人们的认知以外，必然还有其它优越性，才能促进其发展。在我看来，优越性体现在OOP是Decomposition 和 Abstraction的体现。所谓分解，就是将万事万物分门别类，比如官僚结构的划分，只有这样才能更好的组织代码和分配职责。所谓抽象，就是将一群具有相同特点的对象抽象成一个东西。为什么要抽象呢？抽象之后，人们只面对一种类别进行工作，这更加方便，其次，抽象也是将信息进行了隐藏，避免人们陷入无尽的知识黑洞。（2021年3月14日09:42:02记，随着以后的深入了解，可能会更改）

<br>

### 3.How OOP?

&emsp;&emsp;在python中，任意对象都是有类别的，所以面向对象编程，我们就要知道怎么写类。类里面主要包含方法和属性（当然方法也可以当做是特殊的属性），方法主要分为构造方法和普通方法。一般情况下，所有类型都有一个父类，即object。所以，基本的类声明，如下所示：

```python
class ClassName(superclassName(often object)):
    #类变量 可以直接 ClassName.y1 来访问或是修改
    y1 = ？
    y2 = ？
    
    # 构造方法,第一个参数self，代表自己（默认这样写，其他参数则是自定义的参数
    def __init__(self, x1, x2,.....xn):
        # 实例变量
        self.x1 = x1
        self.x2 = x2
        ......
        self.xn = xn
        
    # 普通方法，第一个参数self，代表自己（默认这样写，其他参数则是自定义参数)
    def method(self, a,b,....n):
        .......
     
    # 这种带__ 的方法是重写继承自object的方法，关于继承的知识见第9节）
    def __str__(self):
        """
           
        """
        return "diy"
        
```

&emsp;&emsp;进一步说明，python中的变量有类变量和实例变量的一说，实例变量是对象所特有的，类变量是所有对象都特有的，也就是类所特有的变量。说白了就是java中的静态变量和实例变量的区别。

<br>

&emsp;&emsp;创建对象和调用方法（见下面例子就明白了）：

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/9

"""


class Coordinate(object):
    """
        坐标 ： 两个属性 x ,y ,类型均为float
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
            other 和 self 都是Coordinate对象，此方法返回两点之间的距离
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        """
             当print(Coordinate)对象时，返回此方法的string
        """
        return "<" + str(self.x) + "," + str(self.y) + ">"


if __name__ == '__main__':
    # 创建对象 。python中会创建对象之后，会调用__init__方法进行初始化赋值，__init__的第一个参数，无需自己赋值。
    a = Coordinate(3, 4)
    b = Coordinate(0, 0)
    print(a.distance(b))  # 调用distance的方法，第一个参数self无需自己赋值
    print(Coordinate.distance(a, b))  # 这样做并不常见，类似于java的静态方法调用

    print(a) # <3,4>
    print(type(a)) # <class '__main__.Coordinate'>
    print(Coordinate) # <class '__main__.Coordinate'>
    print(type(Coordinate)) # <class 'type'> .即每一个类都是一个type类型的变量

```

<br><br>

## 9.Python Classes and Inheritance

### 9.1get 和 set方法

&emsp;&emsp;get和set方法提供一组对对象属性访问的接口，这样做的目的是信息隐藏。实例如下

```python
class A(object):
    def __init__(self,x):
        self.x = x
    def get_x(self):
        return self.x
    def set_x(self):
        return self.x
a = A(3)
print(a.get_x())
3
print(a.x)
3
```

&emsp;&emsp;但实际上，python做的信息隐藏并不好，在java中有访问控制权限即private，public等，一个属性是私有的，那么不能在类的外部直接通过对象.属性的方法对属性进行访问，但是在python中，没控制权限这一说，所以上面的get和set方法更是一种规范，并不能真正地做到信息隐藏。甚至来说，你还可以为一个对象随时随地创建新的属性，我个人觉得是不太好的，因为类的本身就是对对象的抽象，那么由类创建的对象就不应该有那些特有的属性，当然至少在python世界应该是这样的。然而能随时随地地为一个对象添加属性表明，它并不是。

<br>

### 9.2继承

&emsp;&emsp;继承的目的是为了更好的扩展。父类规定了一些属性和方法，然后子类就可以在此基础上添加自己的属性和方法，并根据实际情况对父类的方法进行重写。

&emsp;&emsp;这一部分没有多说的，课本上的例子已经很翔实了，这里要注意一点，就是子类在构造方法中，如果需要对继承自父类的属性进行赋值时，可以采用父类.构造方法进行初始赋值，比如。

```python
class A(object):
    def __init__(self,x):
        self.x = x
    def get_x(self):
        return self.x
    def set_x(self):
        return self.x

class B(A):
    def __init__(self,x,y):
        A.__init__(self,x)  #调用父类的方法,对x进行赋值
        self.y = y
    def get_y(self):
        return self.y
    def set_y(self):
        return self.y
    def __str__(self):
        return "x:"+str(self.x) +",y:"+str(self.y)
    
b = B(3,4)
print(b)
x:3,y:4

```

<br>

### 9.3重写

&emsp;&emsp;如果父类的方法不适合或是必须要求子类重写方法的时候，子类就应该重写方法。比如object的如下方法：

1. \_\_str\_\_
2. \_\_eq\_\_(对==的重写)
3. \_\_gt\_\_(对\>的重写)

.......  那么子类可以选择重写。

<br>

还比如如果父类写了这样的方法，那就是希望子类重写的:

```python
class MySupClass(object):
    def __init__(self):
        pass

    def method_to_be_implemented(self):
        raise NotImplementedError
```

<br>

当然，子类不重写这个方法，也不会报错，但是调用这个方法，就会报错。完整代码如下:

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/15

"""


class MySupClass(object):
    def __init__(self):
        pass

    def method_to_be_implemented(self):
        raise NotImplementedError


class Offspring(MySupClass):
    def method_to_be_implemented(self):
        pass

    def special_method(self):
        pass


if __name__ == '__main__':
    son = Offspring()

```

<br><br>

## 10 & 11.Understanding Program Efficiency

&emsp;&emsp;下面都是对时间复杂度的讨论。空间复杂度也重要，但是不在讨论范围内。

### 10.1如何测量不同算法的优劣？

1. **测量时间**

   测量时间受到不同机器，算法的不同实现（while或for loop,递归还是循环），小输入量不稳定的条件限制，虽然不同算法时间有差距，但是难以用公式表示 输入的大小与算法的耗时之间的关系。所以测量时间不可取。

2. **测量步骤**

   测量步骤不受不同机器的影响，也可以公式表示输入的大小与算法耗时之间的关系，但是同一个算法的实现不同（while或是for loop，递归或是循环），哪些步骤（算法指令，比如比较，赋值等等）该算入在内是不明确的，所以这个方法也不可取。

3. **测量算法上界**

   一个算法的执行情况分为worst_case,best_case,average_case。好比你从54张扑克牌中以不放回的方式抽取黑桃A，best_case是1次抽中，worst_case是54次抽中，average_case是27次抽中。而测量算法上界就是测量随着输入的变化，算法在worst_case情况下，运行时间（仍然是步骤为指标）的变化情况。这种表示方法叫做BIg O表示法，注意这里和测量步骤都是以步骤为依据，但是前者会关注一些核心影响因子，具体见BIg O表示法。

<br>

### 10.2Big O表示法

&emsp;&emsp;Big O 表示法 表示的是，在worst_case情况下，算法的运行时间和算法输入之间的变化情况，首先需要说明的是，算法运行时间仍以步骤（也即是算法指令，如赋值，比较等）为指标，但是我们会忽略掉一些无关紧要的因素，着重核心,也就是说我们更看重的是一个趋势，而不是准确值，所以一个算法的不同实现是没有区别的。还需要知道的是算法的运行时间和算法输入之间的变化情况涉及到了一个概念是 **渐进上界**，渐进上界简单来说就是天花板，好比100分的卷子的渐进上界是100;而120,130是上界。

<br>

![image-20210314110825556](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210314110825556.png)

从上面可以看出，所谓BIg O表示法简单来说就是忽略影响较小项并且忽略常数乘法因子。为什么要忽略他们呢？因为BIg O探究的是在worst_case下，较大的输入带来算法的影响，所以会忽略掉一些影响小的项。当然，这里需要注意所谓的输入，可以是显式的，比如list的大小，也可以是隐式的，比如整数的大小。

<br>

除此以外，Big O还满足如下公式：

![image-20210314111258313](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210314111258313.png)

<br>

![image-20210314111320494](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210314111320494.png)

<br>

### 10.3常见的算法复杂度

采用Big O表示法表示的常见算法复杂度如下所示：

![image-20210314111953085](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210314111953085.png)

像一些指令，比如赋值，比较等等，算法复杂度是O（1），一层循环是O（n）,两层嵌套循环是O（n2）。

<br>

### 11.1常见的复杂度代表

#### 11.1.1 O(1)

&emsp;&emsp;这种级别的算法很少，因为与输入的大小无关。

<br>

#### 11.1.2 O(logn)

&emsp;&emsp;常见的便是二分查找，注意，底数是多少并没有关系，因为假设y为常数，存在下面公式:
$$
O(log_2x) = O(log_2y * log_yx) = O(log_yx)
$$
二分查找代码如下：

```python
def binary_search2(L, e):
    """
    算法复杂度分析，worst_case下，递归logn次。  每次都有比较,赋值等判断，那么算法复杂度即为O(logn)。
    完毕
    """

    def binary_search2_helper(L, low, high, e):
        if low > high:
            return False
        if low == high:
            return L[low] == e
        mid = (high + low) // 2
        if L[mid] == e:
            return True
        else:
            if L[mid] > e:
                high = mid - 1
                return binary_search2_helper(L, low, high, e)
            else:
                low = mid + 1
                return binary_search2_helper(L, low, high, e)

    return binary_search2_helper(L, 0, len(L) - 1, e)
```

<br>

还有另外一个Demo如下所示:

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def int_to_str(i):
    """

    :param i: Assume i is a non-negative integer
    :return: return i in the format of string
    算法复杂度分析 ，输入规模即为i （注意：算法规模既可以是显式的，比如list的大小，也可以是隐式的，比如这个demo
    当算法规模为n的时候，while循环会执行 logn次。所以 O(logn)
    """
    result = ""
    if i == 0:
        return '0'
    else:
        while i != 0:
            result += str(i % 10)
            i = i // 10
        return result


if __name__ == '__main__':
    print(int_to_str(666))
    print(int_to_str(0))
    print(type(int_to_str(0)))
```

<br>

#### 11.1.3 O(n)

&emsp;&emsp;常见的循环以及遍历元素。下面仍然摘抄两个Demo:

带copy的二分查找:

```python
def binary_search1(L, e):
    """

    :param L:  A ordered list(Assume its elements are integers)
    :param e:  Assume it's an integer
    :return:   Return True if e  is an element of L ,otherwise False

    将L对折x次之后的元素为1个，那么 2^x = len(L),  也就是说 x = log(len(L))。将len(L)看做是n。那么就是logn次
    在worst_case情况下，每次都会递归复制传入实际参数L的一半。那么等价于 复杂度为 1/2 n + 1/4 n + .....(加法项数为 logn次）
    那么根据 等比数列的求和公式，可以估计 为 O（n) 。 当然，这仅仅是拷贝带来的复杂度，其他常数操作是O（1）,总共logn次，那么还有一项
    是O（logn）  。  O（n) + O(logn)  = O(n)
    即这种带copy的二分查找复杂度是 O(n)
    """
    if len(L) == 0:
        return False

    if len(L) == 1:
        return L[0] == e

    mid = len(L) // 2  # mid是坐标
    if L[mid] == e:
        return True
    elif L[mid] > e:
        return binary_search1(L[:mid], e)
    else:
        return binary_search1(L[mid:], e)
```

<br>

n！

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def fact_iter(n):
    """

    :param n:  Assume n is a positive integer
    :return: n!
    算法复杂度分析  循环执行n次  ，故O（n)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fact_recur(n):
    """
       算法复杂度也为n
    """
    if n == 1:
        return n
    else:
        return n * fact_recur(n - 1)


if __name__ == '__main__':
    print(fact_iter(5))
    print(fact_recur(5))
```

<br>

#### 11.1.4 O(nlogn)

&emsp;&emsp;大多数具有实践意义的算法都是这个复杂度，比如归并排序，可以详见12.2节的归并排序。

<br>

#### 11.1.5 O(n^c)

&emsp;&emsp;多项式复杂度，c常常取2.常见的就是两层嵌套的算法。这部分可以查看12.2节的冒泡排序和选择排序。

<br>

#### 11.1.6 O(c^n)

指数式复杂度，这种级别的算法的代价将是极高的。比如汉罗塔问题。

![image-20210314151802274](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210314151802274.png)

<br>

获取子集问题

![image-20210315165907990](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210315165907990.png)

<br>

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def get_subset(L):
    """

    :param L:  List (can assume its elements are integers)
    :return: L's subset ,e.g   [1,2,3]   ---> [ [] ,[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3] ]

    观察得到 [1,2,3]   --->[] ,[1],[2] [1,2]  + [3],[1,3],[2,3],[1,2,3]

    算法复杂度分析: 参考MIT lecture
    tn     =  tn-1   +  2^n-1  +  c
         =  tn-2   +  2^n-2  +  c  +  2^n-1  +  c
          =  tn-k   +  2^n-k  +  …  +  2^n-1  +  kc
         =  t0 +  2^0    +  ...    +  2^n-1  +  nc
         =  1  +  2^n       +  nc
    """
    if len(L) == 0:
        return [[]]

    list_exclude_last_elt = get_subset(L[:-1])  # L [1,2,3] ,list_exclude_last_elt = [ [] ,[1],[2] [1,2]  ]
    last_elt = L[-1:]  # [3]
    result = []
    for elt in list_exclude_last_elt:  # sn-1
        result.append(elt + last_elt)

    return list_exclude_last_elt + result


if __name__ == '__main__':
    print(get_subset([1, 2, 3]))
```

<br>

分析一个算法的复杂度，可以采取递推公式或画图分析（如斐波拉契数列）或步骤分析。

下面是常见的python函数的算法复杂度

![image-20210315170720177](MIT6.0001-Introduction%20to%20CS%20and%20Programming%20in%20Python%20Notes.assets/image-20210315170720177.png)

<br><br>

## 12.Searching and Sorting algorithms

### 12.1查找算法

1. 暴力查找

   很明显算法复杂度为O(n)

2. 二分查找

   如果list是有序的，那么算法复杂度为O(logn)

&emsp;&emsp;假如list不是有序的，暴力查找和二分查找那个效率高呢，即O(sort) + O(logn) 和 O（n)的比较。事实上，肯定是后者更小，因为排序的基础是访问每一个元素，也就意味着O(sort) 至少是O（n)级别的。

&emsp;&emsp;那么对于无序的列表来说，排序就一定用没有了吗？那也不是，通常情况下一次排序可以多次查找。假设查找K次，那么现在的比较是 O（sort） + kO(logn)  和k O(n)的比较。进而转为 O（sort） 与 kO（n） - kO(logn)的比较，进而是 有没有排序算法的复杂度是小于 kO（n)的。事实上，肯定是存在这样的算法的。

<br>

### 12.2排序算法

&emsp;&emsp;下面包含冒泡排序，选择排序，归并排序，直观的图解可以参看<a href="https://visualgo.net/en/sorting">visual_sorting</a>。

```python
"""
@Author  : Lord_Bao
@Date    : 2021/3/14

"""


def bubble_sort(L):
    """
    基本思想：  对L进行一次遍历，如果前面的元素比后面的元素大，那么进行一次交换，一次迭代后。数组最后的元素是最大的。
                这种排序就很像 是冒泡。

    """
    #  ########### 下面这种方法不管是 worst_case,best_case,average_case都是 O（n^2） #########
    # for i in range(len(L)):
    #     for j in range(len(L)-1):
    #         if L[j] > L[j + 1]:
    #             L[j], L[j + 1] = L[j + 1], L[j]
    # return L
    # ##################################################################

    # #############下面这种情况 best_case即顺序的时候 为O(1),worst_case即倒序的时候 为O（n^2)#############
    # 设置一个swap, 在循环中设置为False,如果产生一次swap，那么就设置swap为True。如果为False，
    # 那么表示 第1个元素 比 第2个元素,第2个元素比第3个元素小,如此类推,即表明列表元素已经有序，退出循环。
    swap = True
    while swap:
        swap = False
        for index in range(1, len(L)):
            if L[index - 1] > L[index]:
                L[index - 1], L[index] = L[index], L[index - 1]
                swap = True
    return L


def selection_sort(L):
    """
    选择排序 每次从list挑选最小的元素放在最前面，然后从子list再挑选最小的元素。
    算法复杂度 O（n^2）  best_case avg_case,worst_case都是O(n^2)
    """

    for i in range(len(L)):

        small_index = i
        for j in range(i, len(L)):
            if L[j] < L[small_index]:
                small_index = j
        L[i], L[small_index] = L[small_index], L[i]
    return L


def merge_sort(L):
    """
           规定排序的基本思想是将L拆分为两半，然后分别对两半进行排序，然后再对两半进行归并。
           base_case 为 当一个L的大小为1或0时，直接返回。

           算法分析， 一个size为n的列表。那么将会分为logn层。最坏的情况是，处于同一级的left_part和 right_part将在
           merge中执行 len(right_part) + len(left_part) 操作。 也就是说在每一层都是 执行 O(n)次操作。那么总的是
           O(n) * O(logn) = O(nlogn)
    """

    def merge(left_part, right_part):
        i = 0
        j = 0
        result = []

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                result.append(left_part[i])
                i += 1
            else:
                result.append(right_part[j])
                j += 1

        if i < len(left_part):
            for elt in left_part[i:]:
                result.append(elt)
        if j < len(right_part):
            for elt in right_part[j:]:
                result.append(elt)
        return result

    if len(L) < 2:  # base_case
        return L[:]
    else:
        mid = len(L) // 2
        left_part = merge_sort(L[:mid])
        right_part = merge_sort(L[mid:])
        return merge(left_part, right_part)


if __name__ == '__main__':
    list1 = [9, 6, 7, 5, 4]

    print(bubble_sort(list1[:]))
    print(selection_sort(list1[:]))
    print(merge_sort(list1[:]))
```

<br><br>

# Summary

&emsp;&emsp;整个课程介绍了

1. python的基本知识
2. for和while循环。
3. 两种不可变类型如tuple和string，可变类型list，三者都支持 + ，\*，索引，切片，迭代。
4. 字典
5. 函数和对象
6. 测试
7. 算法复杂度和常见的查找和排序算法。

并提供了6个Pset，注重从解决实际问题中提高专业水平。

<br>

&emsp;&emsp;我在学习这门课程之前，有一定的java经验，所以感觉还好。整个学习阶段经历了13天，即从2021/3/2 -- 2021/3/15。中间休息了1.5天左右。开始的时候，由于是全英文字幕，不太适应，但是后面渐渐就熟悉了。除了这个问题以外，还有其他问题值得我注意。首先就是写代码的时候务必认真写注释，做好文档工作，再三强调，做好文档工作；其次是学习不应该突进，我在第8节，即面向对象开始，笔记就开始落下了，结果导致从昨天（2021/3/14）到现在(2021/3/15)一直在整理笔记，当然，还好我学习周期短，这些知识还记得住，要不然就真是白费力气了。

&emsp;&emsp;差不多了，相约6.0002吧！！！

<br><br>

# Psets

&emsp;&emsp;这部分可参见GitHub上的具体代码实现。MIT在每一个Pset上都有很详尽的指导，所以我只列举一些容易出错的地方和一些重要点。

## Pset0

&emsp;&emsp;略

<br>

## Pset1

&emsp;&emsp;ps1a和ps1b的基本思路是一样的，即当累积存款大于首付的时候的累积月份即为所求，具体参见代码即可。而ps1c的问题是找到最好的portion_saved，使得36个月的存款刚好超过down_payment，而starting_salary是用户输入的变量。这道题基本思路是二分法，因为题目已经提示在0到10000个数字中猜测对应的portion_saved是否满足要求。

&emsp;&emsp;ps1c需要注意两个问题：

**问题1**是可以在代码开始的时候，判断portion_saved为1的时候，36个月之后存款是否达到down_payment，这样可以在一定程度提高效率。

**问题2**是当用户输入的starting_salary比较大的时候，即使在portion_saved为0.000情况下，savings仍然会超过down_payment+100。又或是刚好在某portion_saved下，savings小于down_payment，而portion_saved+0.0001下，savings大于down_payment+100。所以在这种情况下，要特殊对待。具体的处理方案已经放到代码中。

<br>

## Pset2

&emsp;&emsp;Pset2是一个关于HangMan的游戏，简单来说就是猜单词。每次用户在26个字母中选择一个字母，如果目标单词含有此字母，那么游戏继续，如果目标单词不含此字母，扣掉一次猜测机会。当猜测机会用完或是猜测出单词，游戏结束。具体规则可以百度或是Google。

&emsp;&emsp;第1个Part，是写三个helper_function,即

1. `is_word_guessed(secret_word, letters_guessed)`,
2. `get_guessed_word(secret_word, letters_guessed)`,
3. `get_available_letters(letters_guessed)`

这三个方法的意思可以参考Pset2的文档，不再详述。

&emsp;&emsp;第2个Part，也就是处理没有提示的hangman，按照说明书照着写就行了，这个部分我感受到的就是太多情况要处理了，很容易让人搞晕，建议做一部分，测一部分。

&emsp;&emsp;第3个Part，也就是处理有提示的hangman，其实这部分主要是写下面两个函数，即

1. `match_with_gaps(my_word, other_word)`
2. `show_possible_matches(my_word)`

第2个方法其实就是循环 + 第1个方法检验。第1个方法也没有特别难的，就是注意到案例上有这样一个情况

> \>>> match_with_gaps("a_ ple", "apple") 
>
> False 

也就是match_with_gaps不能只是：先判断长度是否相同，然后碰到字母就进行检验是否相同，碰到_就跳过。因为“a\_ple"这种情况说明了下划线不可能是aple这四个字母，所以需要将这四个字母存储起来，然后检验下划线对应另外一个单词的字母（这里是p）是否出现这四个字母里，如果出现了那么就是FALSE。上面的”a\_ple"可能是"ample"。

<br>

## Pset3

&emsp;&emsp;Pset3是一个关于Srabble的游戏，简单来说就是一个填词游戏。每次自己手上有`Hand_Size`大小数量的字母，然后根据这些字母组成单词。分数计算规则是两个部分的乘积，第一个部分是单词的大小`word_len`，第二个部分是`max(1,word_len * 7 - 3 * (hand_size -word_len))`。

&emsp;&emsp;**Problem1 Word_scores**

这个部分简单，照着说明书做就行。

&emsp;&emsp;**Problem2 Dealing with hands**

这个部分就是写一个函数`update_hand(hand, word)`,hand指的是自己的手牌，以字典形式保存。而word是你本次拼的单词。这个方法将会返回之后的手牌。好比你斗地主开头17张，然后你第一把打了个王炸，下把牌就是15张了。举个具体的例子，比如我本次的hand是{‘a’:2,'p':2,'l':1,'e':1,'m':1},假如我拼写的单词是apple。那么下一把的hand就是{‘m’：1}。当然题目也支持这种格式:{‘a’:0,'p':0,'l':0,'e':0,'m':1}。当然，如果你拼了个appple。那么p代表的还是0，不应该是负数。简单来说，这个部分就是叫你写更新后的hand。

&emsp;&emsp;**Problem3 Valid Words**

这个部分就是写一个函数`is_valid_word(word, hand, word_list)`,简单来说就是判断你拼写的单词是否合法。合法有两个意思，首先你拼写的单词的字母必须是你的hand有的字母，其次你拼写的单词还必须在word_list里面。

&emsp;&emsp;**Problem4 Wildcards**

这个部分就是添加了一个\*当做元音的随做，它对应的分是0.然后修改Problem2和3的两个函数。

&emsp;&emsp;**Problem5 Playing a hand**

这个部分没有什么难的，就是if else 和while比较麻烦。

&emsp;&emsp;**Problem6 Playing a game**

这个部分会写一个`substitute_hand(hand, letter)`函数，也就是用户可以更换一个字母，并返回新的hand。然后这部分需要考虑一个问题的处理，即要用若干变量存储上一局的hand和score，因为用户可能下一局的时候可能会重玩。

总体来说，Pset3没有太难的，就是最后的格式呈现问题和考虑的情况比较多的问题会比较烦而已。

<br>

## Pset4

**PartA:**

PartA就是取一个字符串的重排情况。简单。

**PartB:**

就是写一个凯撒加密的算法，假设凯撒加密的shift是x，那么解密的方法就是将加密的方法传的参数变为26-shift。因为负数求余可能是不对的，所以加上26。比如字符串’z‘，shift=1，加密后为’a‘.那么解密的话就是 26-1，即shift为25，还原为’z'。

当然如果解密的时候不知道shift的话，那么就需要尝试26种不同的shift，并计算解密后的单词有效数。通过单词有效数最高的shift，可猜测加密前的shift为  26-shift。

**PartC:**

这也是一种加密算法，简单来说元音字符串为“aeiou",那么将元音字符串随机重排获得新的序列，比如”eioua，。那么加密就是将”a“替换为”e“，”e“替换为”i“,如此类推。而解密的过程，就是将5！种排列顺序反复实验，计算解密后的单词有效数。最高的单词有效数代表的一种映射即是加解密的密码本。

<br>

## Pset5

这个部分就是通过各种Trigger从网上提取信息。然后呈现在GUI上。这个题没有过多难的，但是有些问题需要注意。

**问题1：TimeTrigger**

```python
class TimeTrigger(Trigger):
    def __init__(self, date_string):
        """
        :param time: time in EST as a string in the format of "3 Oct 2016 17:00:10"
                      也就是说3 Oct 2016 17:00:10 是一个EST格式的String

        """
        #  下面的time是  offset-aware datetimes 类型，即有时区， 这个是通过replace指定的
        self.time = datetime.strptime(date_string, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
```

datetime可以分为offset-aware类型和offset-naive类型，简单来说前者是带时区，后者没带时区，二者无法比较。根据题目应该是说将datetime转为一个EST，也就是美国东部时间。如果不带时区的话，可以将上面的`tzinfo=None`。出现这个问题的原因是test_case有两种，分别是针对有时区和无时区的，所以一开始我无论怎么设置总是报错。

<br>

**问题2：GUI始终出不来信息**

这个问题其实是Trigger的设置以及间隔时间SLEEPTIME的设置问题。可以设置多个Trigger和将SLEEPTIME设置小一点。

<br>

**问题3：object has no attribute 'description'**

如果出现这个问题，也会导致GUI出不来信息。我猜测原因可能是`stories.extend(process("http://news.yahoo.com/rss/topstories"))`

这行代码的问题。

也就是Yahoo的Rss对应的xml和NewsStory在description属性上不匹配的问题。简单点，注释掉这行代码。

<br><br>

# Reference

1.list,string,dictionary等的方法总结图片参考的是书籍*Introduction to Computation and Programming Using Python: With Application to Understanding Data Second Edition*。

2.算法复杂度的比较等图片参考的是MIT6.0001提供的PDF。

3.python涉及到的栈帧等图片是参考的网站<a href="http://www.pythontutor.com/">pythontutor</a>。

