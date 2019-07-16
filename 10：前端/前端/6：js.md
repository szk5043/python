## 六、JavaScript

### 1、概述

JavaScript是属于网络的脚本语言 , 是因特网上最流行的脚本语言

JavaScript被数百万计的网页用来改进设计 , 验证表单 , 检测浏览器 , 创建cookies , 以及更多的应用

浏览器内置了JavaScript语言的解释器 , 所以浏览器上按照JavaScript的规则编写相应代码 , 浏览器可以解释并作出相应的处理

完整的JavaScript实现是由一下三个不同部分组成的 : 

- 核心 , ECMAScript
- 文档对象模型 (DOM) , Document Object Model (整合JS , CSS , HTML)
- 浏览器对象模型 (BOM) , Broswer Object Model (整合JS和浏览器)

### 2、JS如何引入

- HTML的head中

- HTMLbody之后(推荐,)

- 引入js文件(推荐)

  > 由于HTML代码是从上到下执行的 , 如果Head中的JS代码耗时严重 , 会导致用户长时间无法看到页面 , 所以将JS代码防止HTML的body代码块底部是最好的 , 因为不会影响用户看到页面效果 , 只是JS实现特效慢而已

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script></script>    <!--head标签中-->
  </head>
  <body></body>
  <script></script>    <!--body标签后-->
  <script type='text/javascript' src='/path/to/js文件'></script>   <!--引入js文件-->
  </html>
  ```

### 3、注释

单行注释 : //

多行注释 : `/* ... */` , (CSS注释也是如此)

### 4、变量

在JavaScript中 , 变量的声明默认表示声明的全局变量 , 局部变量必须以`var`开头

生命周期 : 

- JavaScript变量的声明周期从它们被声明的时间开始
- 局部变量会在函数运行以后被删除
- 全局变量会在页面关闭后被删除

```javascript
<script type="text/javascript">
    // 全局变量
    name = 'Lyon';
    function func(){
        // 局部变量
        var age = 18;
        // 全局变量
        gender = "男"
    }
</script>
```

**注意 : JavaScript中严格区分大小写 , 并且以 ";" 号结束** 

### 5、数据类型

- 字符串str：`var name='Wesley'`
- 整型int：`var age = 26`
- 浮点型float：`var salary = 3.14`
- 布尔值bool： `var b = true/false`
- 数组array：`var arr = ['Wesley',18]`,等同于Python中的列表
- 对象json：`var d = {'name':'Wesley','age':18}`,等同于Python中的字典

### 6、运算符

①、算术运算符：`+   -    *    /     %       ++        —`

②、比较运算符：`>   >=   <    <=    !=    ==    ===   !==`

③、逻辑运算符：`&&   ||   ！`

④、赋值运算符：`=  +=   -=  *=   /=`

### 7、流程控制

①、顺序

②、分支：`if else if` 

③、循环：`for`

