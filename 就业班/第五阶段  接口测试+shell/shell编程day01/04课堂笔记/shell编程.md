### 1、shell 概述

##### A、是什么?

<u>shell 是一门计算机语言</u>，和 python | Java  一样，都可以编写程序

A-1、shell字面意思: <u>壳</u>,核:指操作系统,shell 是保护操作系统的 

A-2、计算机操作系统只能识别 0 和 1  组成的机器码，现在我们是通过GUI|CLI 来间接操作操作系统

GUI(图形化界面) | CLI(命令行) 在用户与操作系统之间，相当于桥梁、中介的作用，结构上看，GUI和

CLI 保护操作系统 

A-3、GUI 与 CLI 就是通过 Shell 实现的 

##### B、为什么?

通过shell按照需求编写一些程序

##### C、怎么用?(linux)

C-1、分类

第一类:GUI样式的shell

第二类:CLI样式的shell

**<u>专指: Linux 下的 shell 编程</u>**		

C-2、流程

1)、创建一个文本文档,后缀名是 .sh

文档名要做到见名知意

2)、再在文本文件中录入一个命令

echo  "xxxx" 在命令行模式下直接输出数据

规范:第一行固定格式 #！/bin/bash

作用:指定脚本解析的解释器

3)、执行  .sh 文件(shell 脚本)

方式1: sh(bash) shell文件

方式2: 绝对路径(/xxx/yyy/abc.sh) 或 相对路径(./abc.sh),注意:权限 chmod 777 abc.sh

方式3: source abc.sh(source 相当于 ./)

D、练习

###### 练习1:在命令行输出当前所在目录



### 2、shell 语法: 注释

##### A、是什么?

注释是程序中非功能性说明文本

##### B、为什么?

增强程序的易读性，易维护性

##### C、怎么用?

<u>单行注释(常用):一次只注释一行</u>

格式: # 注释文本

<u>多行注释(了解，基本不用):一次可以注释多行</u>

:<<自定义的标记

​	第一行注释

​	第二行注释

​	.....

自定义标记

### 3、shell 语法: 变量

##### A、是什么?

程序=数据+数据操作

变量就是数据的载体,变量之所以称之为变量，是因为其中的值可以改变

##### B、为什么?

变量为数据设置一个引用，以后再使用这个数据时，可以通过引用获取数据

##### C、怎么用?(重点)

<u>变量创建:</u>

​	格式: 变量名=变量值

​	注意1:变量名

​	a)、不能数字开头

​	b)、变量名不能有空格这种特殊字符

​	c)、起名做到见名知意

​	d)、变量名不要使用关键字

​	注意2:赋值符号

​	**=左右两侧不要有空格**

​	注意3:变量值

​	a)、变量值可以不使用引号，但是如果有空格，必须使用 "" | ''

​	b)、"" 和 '' 的区别，变量之间赋值时，如果是  ""，那么赋的是变量的值

​	如果是 '' 只是赋值调用格式

<u>变量查询:</u>

​	格式:"${变量名}" -----  标准格式

​	注意:其他格式(不建议使用)

​		\${变量名} | \$变量名

<u>变量修改:</u>

​	格式:同增

<u>变量删除:</u>

​	格式:unset 变量名

##### D、变量分类

<u>D-1、本地(局部)变量</u>

只有当前 shell 可以使用的变量	 

<u>D-2、全局变量</u>(静态变量)(了解)

被多个 shell 共享的变量	 

需求:如何将本地变量转换成全局变量

思想:将本地变量设置为全局变量就是要将本地变量导出到共享空间

格式: export 局部变量 

查询全局变量: env

注意1:如果是全局变量，建议变量名所有字母都大写

注意2:全局变量要慎用

<u>D-3、内置变量(特殊变量)</u>

需求:编写shell动态获取某个目录下的子级(目录不一定)

实现流程:

​	1)、shell 调用时，可以传入要操作的目录

​	格式: sh abc.sh 某个目录

​	2)、shell 执行时，可以获取调用传入的目录

​	格式:ls  $1 (代表传入的第一个参数)	  

上述流程其实就是传参以及参数解析的过程，这个参数就可以称之为内部变量

语法总结:

应用场景，程序执行时有些数据是可变的，可以调用脚本时，传入这些可变数据，脚本中解析获取

调用格式: sh xxx.sh 参数1 参数2 参数3 .....

解析格式: $N 获取第 N 个参数

优        点: 动态传值，更灵活

<u>注	    意:</u> $N 获取第 N 个参数，但是 N 最大就到 9

​		  $0 获取脚本文件名

​		  $* 获取所有参数

​		  $# 获取参数个数



<u>D-4、扩展:读取键盘录入</u>

需求:编写shell动态获取某个目录下的子级(目录不一定,要让调用者指定)

格式: read	 -p	 "提示语句:"	 变量名 (注意:有空格!!!!)

作用:执行到此时，程序挂起，等待用户录入数据，录入数据后，回车，录入的数据会赋值给变量

优点:动态获取数据，更灵活!!!!!

##### E、变量特殊赋值（记住）

需求:将某个命令的结果赋值给一个变量

格式:变量名=\`命令\`

**F、练习**	

###### 练习1：使用shell脚本，输出当前所在的目录

知识点:将命令结果赋值给变量

###### 练习2：计算/etc目录下有多少个文件，用shell脚本实现

新知识点:获取某个目录下子级个数

​		固定格式:ls 目录 | wc -l

###### 练习3：实现统计任何指定目录下的文件个数，用 shell 脚本实现

知识点：怎么动态获取数据?

### 4、shell 语法: 运算符

##### A、是什么?

是变量执行运算时使用的一些特殊符号

##### B、为什么?

因为程序中频繁使用算数运算、逻辑运算、比较运算....等算法

##### C、怎么用?

<u>运算符分类</u>

C-1、算数运算符

格式: $((数学表达式))

运算符:	+ - * / % == 加减乘除取余

注意: 一般计算机语言中除法运算只取商

C-2、比较运算符:返回的是 boolean 值（<u>特殊: 0为true 1为false</u>）

格式: [ 表达式 ] ---- 注意:[] 中有两个空格，两个空格中添加表达式

查看结果: $? 

运算符: 不能直接使用 > < >= <= == != 

使用对应的参数  -gt(>) -lt(<) -ge(>=) -le(<=) -eq(==) -ne(!=) **记住**

g = greater

t = than

l = less

e = equals

n = not

C-3、逻辑运算符:返回 boolean 值（<u>特殊: 0为true 1为false</u>）

格式: [ 表达式 ]

<u>运算符: -a 与 		-o或 		！非</u>

C-4、字符串比较:返回 boolean 值

格式: [ 表达式 ]

运算符: == 判断两个字符串内容是不是一样

​	      != 判断两个字符串内容是不是不一样

​	      -z 判断单个字符串长度是不是0(判断字符串是不是空)

C-5、文件判断：返回 boolean 值

格式: [ 表达式 ]

运算符:  -d: 判断是不是文件夹

​	       -f: 判断是不是文件

​	       -e: 判断是不是存在

变体:

​	test -参数 路径 等价于 [ -参数 路径 ]

**D、练习**

###### 练习1：判断 /home/admin(/root)目录是否为空

思路：现获取目录子级文件个数，判断是否大于 0

###### 练习2：通过用户输入任意目录判断是否为空



### 5、shell 语法: 函数

##### A、是什么?



##### B、为什么?



##### C、怎么用?

**C-1、函数声明**



**C-2、函数调用**



**C-3: 注意**



**C-4、函数分类**



##### D、练习

###### 练习1：读取键盘录入，录入长方形的长和宽，编写求周长和面积的函数，调用并输出周长和面积的值



### 6、shell 语法: 流程控制

##### A、是什么?



##### B、为什么?



##### C、分类?



### 7、shell 语法:流程控制分支实现之 if

--------



##### A-1、格式1

**语法:**

​	

##### 	举例:

​	(需求: 录入年龄，判断是否成人，如果成人了输出"成年人")

---------



##### A-2、格式2

##### 语法:

​	

##### 	举例:

​	(需求: 录入年龄，判断是否成人，如果成人了输出"成年人",否则输出未成年)

----------



##### A-3、格式3

**语法:**

​	

##### 	举例: 

​	(需求: 录入年龄，判断是否成人，如果成人了输出"成年人",否则输出未成年)

----------

##### B、练习

###### 	练习1：判断用户输入的用户名和密码是否为admin 123456,如果是则提示登录成功，否则提示失败

###### 	练习2：输入数字，判断是否大于0，如果大于0则将该数字-1并输出，否则+1输出

###### 	练习3：判断用户输入的目录是否存在，如果存在则统计目录下的文件个数，否则提示用户该目录不存在

###### 	练习4：判断学生的成绩，大于90-100提示优秀，80-90之间提示良好,70-80之间则提示一般，60-70之间提示	及格。其他则提示不及格

###### 	练习5：判断用户输入的内容是否为空，为空则提示，不为空则判断是否为目录，不为目录则判断是否为文件，否则提示错误信息

### 8、shell 语法:流程控制分支实现之case

##### A、格式

**语法:**

​	

##### 	举例:

​	（需求:模拟游戏级别选择，读取键盘录入的数字，如果是数字1，那么输出简单，	如果是数字2，那么输出一般，如果是数字3输出困难，其他输出数据有误）

##### B、练习

###### 	练习1：输入一个序号，判断该用户选择哪款产品，A：笔记本 B：电饭煲 C：小台灯

###### 	练习2：请输入对客服的满意度，【0-3】不满意，【4-6】满意，【7-9】非常满意



### 9、shell 语法:流程控制循环实现之for

##### A、格式

**语法:**	

​	

##### 	举例:

​	(需求:遍历 1-10之间所有整数)

##### B、练习

​	求1-100之间的和



### 10、shell 语法:流程控制循环实现之while

##### A、格式

**语法:**	

​	

##### 	举例:

​	(需求:遍历 1-10之间所有整数)

##### B、练习

​	求1-100之间的和



### 11、shell 语法其他:重定向

##### A、是什么?



##### B、为什么?



##### C、怎么用?



### 12、shell 语法:补充2数组

##### A、是什么?



##### B、为什么?



##### C、怎么用?



##### D、应用



​	

----------------------

###### 综合练习:输入一个目录，判断目录是否存在，如果不存在则给出提示，如果存在则提示输入要创建的文件名，(前提:要先进入目录)判断创建的文件是否存在，如果不存在，则继续创建，否则提示该文件已经存在 



