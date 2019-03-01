# <center>Xpath、CSS定位</center>

---		

## 目标
	
	1. 熟悉Xpath定位策略
	2. 熟悉CSS定位策略

---

# 为什么要学习Xpath、CSS定位？	

	1. 在实际项目中标签没有id、name、class属性
	2. id、name、class属性值为动态获取，随着刷新或加载而变化	

---

## 1. 什么是Xpath？
	
	1. XPath即为XML Path 的简称，它是一种用来确定XML文档中某部分位置的语言。
	2. HTML可以看做是XML的一种实现，所以Selenium用户可以使用这种强大的语言在Web应用中定位元素。

	XML：一种标记语言，用于数据的存储和传递。 后缀.xml结尾

	提示：Xpath为强大的语言，那是因为它有非常灵活定位策略；

### 思考
	Xpath有那些策略呢？

## 2. Xpath定位策略(方式)
	
	1. 路径-定位
		1). 绝对路径
		2). 相对路径 
	2. 利用元素属性-定位
	3. 层级与属性结合-定位
	4. 属性与逻辑结合-定位

### Xpath定位 方法
	driver.find_element_by_xpath()

### 2.1 路径(绝对路径、相对路径)

	绝对路径：从最外层元素到指定元素之间所有经过元素层级路径 ；如:/html/body/div/p[2]
			  提示：
			  	1). 绝对路径以/开始
			  	2). 使用Firebug可以快速生成，元素XPath绝对路径

	相对路径：从第一个符合条件元素开始(一般配合属性来区分)；如：//input[@id='userA']
			  提示：
			  	1). 相对路径以//开始
			  	2). 使用Friebug扩展插件FirePaht可快速生成，元素相对路径

	提示：为了方便练习Xpath，可以在FireBug内安装扩展插件-FireFinder插件；
		  1). 火狐浏览器-->组件管理器-->搜索FireFinder

### 使用Xpath实现 案例-1 
	需求：
		1). 使用绝对路径和相对路径分别实现，账号A：admin;密码A：123456；自动化脚本设计

### 2.2 利用元素属性
	说明：快速定位元素，利用元素唯一属性；
	示例：//*[@id='userA']	

### 2.3 层级与属性结合
	说明：要找的元素没有属性，但是它的父级有；
	示例：//*[@id='p1']/input

### 2.4 属性与逻辑结合
	说明：解决元素之间个相同属性重名问题
	示例：//*[@id='telA' and @class='telA']

### 2.5 Xpath-延伸

	//*[text()="xxx"]							文本内容是xxx的元素

	//*[starts-with(@attribute,'xxx')]				属性以xxx开头的元素

	//*[contains(@attribute,'Sxxx')]				属性中含有xxx的元素


### 2.6 Xpath-总结
	1. 如何通过Friebug快速生成绝对路径
	2. 如果通过Friebug快速生成相对路径
	3. Xpath策略有那些

---

## 3. CSS定位

### 3.1 什么是CSS？
	1. CSS（Cascading Style Sheets）是一种语言，它用来描述HTML和XML的元素显示样式；
	   (css语言书写两个格式：
	   						1. 写在HTML语言中<style type="text/css">...	
	   						2. 写在单独文件中 后缀.css
	   	)
	2. 而在CSS语言中有CSS选择器(不同的策略选择元素)，在Selenium中也可以使用这种选择器；
	提示：
		1. 在selenium中极力推荐CSS定位，因为它比XPath定位速度要快
		2. css选择器语法非常强大，在这里我们只学习在测试中常用的几个

#### CSS定位 方法
	driver.find_element_by_css_selector()

### 3.2 CSS定位常用策略 (方式)
	1. id选择器
	2. class选择器
	3. 元素选择器
	4. 属性选择器
	5. 层级选择器

#### id选择器
	说明：根据元素id属性来选择
	格式：#id 如：#userA <选择id属性值为userA的所有元素>

### 使用CSS实现 案例-2 
	需求：
		1). 使用CSSid定位实现，账号A：admin;密码A：123456；自动化脚本设计

#### class选择器
	说明：根据元素class属性来选择
	格式：.class 如：.telA <选择class属性值为telA的所有元素>

#### 元素选择器
	说明：根据元素的标签名选择
	格式：element 如：input <选择所有input元素>

#### 属性选择器
	说明：根据元素的属性名和值来选择
	格式：[attribute=value] 如：[type="password"] <选择所有type属性值为password的值>

#### 层级选择器
	说明：根据元素的父子关系来选择
	格式：element>element 如：p>input <返回所有p元素下所有的input元素>
	提示：> 可以用空格代替 如：p input 或者 p [type='password']

#### 3.3 CSS延伸
	1. input[type^='p'] 说明：type属性以p字母开头的元素
	2. input[type$='d'] 说明：type属性以d字母结束的元素
	3. input[type*='w'] 说明：type属性包含w字母的元素

### 3.4 CSS总结

选择器|例子|描述
-|--|---
#id|#userA|id选择器，选择id="userA"的所有元素
.class|.telA|class选择器，选择class="telA"的所有元素
element|input|选择所有input元素
[attribute=value]|[type="password"]|选择type="password"的所有元素
element>element|p>input|选择所有父元素为p元素的input元素
	
---
## 4. XPath与CSS类似功能对比
定位方式|XPath|CSS
---|---|---
元素名|//input|input
id|//input[@id='userA']|#userA
class|//*[@class='telA']|.telA
属性|1. //※[text()="xxx"]<br>2. //※[starts-with(@attribute,'xxx')]<br>3. //※[contains(@attribute,'xxx')]|1. input[type^='p']<br>2. input[type$='d']<br>3. input[type*='w']
	
	说明：由于显示排版原因以上所有(※)号代替(*)


## 5. 八种元素定位总结：

	1. id
	2. name
	3. class_name
	4. tag_name
	5. link_text
	6. partial_link_text
	7. Xpath
	8. Css

	说明：
		1). 元素定位我们就学到这里了
		2). WebDriver除了提供以上定位API方法(driver.find_element_by_xxx())
			外，还提供了另外一套写法；
	    3). 调用find_element()方法，通过By来声明定位的方法，并且传入对应的方法和参数（了解-熟悉即可）

---

## 6. 定位(另一种写法)-延伸【了解】
	说明：第二种方法使用By类的封装的方法,所以需要导入By类包

### 6.1 导入By类
	导包：from selenium.webdriver.common.by import By

### 6.2 By类的方法
	方法：find_element(By.ID,"userA") 
		  备注：需要两个参数，第一个参数为定位的类型由By提供，第二个参数为定位的具体方式
	示例：
		1. driver.find_element(By.CSS_SELECTOR,'#emailA').send_keys("123@126.com")
		2. driver.find_element(By.XPATH,'//*[@id="emailA"]').send_keys('234@qq.com')
		3. driver.find_element(By.ID,"userA").send_keys("admin")
		4. driver.find_element(By.NAME,"passwordA").send_keys("123456")
		5. driver.find_element(By.CLASS_NAME,"telA").send_keys("18611111111")
		6. driver.find_element(By.TAG_NAME,'input').send_keys("123")
		7. driver.find_element(By.LINK_TEXT,'访问 新浪 网站').click()
		8. driver.find_element(By.PARTIAL_LINK_TEXT,'访问').click()

### 6.3 find_element_by_xxx()和find_element() 区别
	说明：通过查看find_element_by_id底层实现方法，发现底层也是调用的By类方法进行的封装；

	    def find_element_by_id(self, id_):
        """Finds an element by id.

        :Args:
         - id\_ - The id of the element to be found.

        :Usage:
            driver.find_element_by_id('foo')
        """
        return self.find_element(by=By.ID, value=id_)

    总结：虽然方法一样，但WebDriver推荐 find_element_by_xxx()这种方法