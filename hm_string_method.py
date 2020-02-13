#一、判断类型
#1、是否是空白
#space_str = "   \t\n\r "#制表符属于空白字符
#print(space_str.isspace()

#2、判断字符串中是否只包含数字
#都不能判断小数

#num_str = "1.1"
#num_str = "(1)"#unicode 字符串
#num_str = "一千零一"#可以判断中文数字
#print(num_str)
#print(num_str.isdecimal())#主要使用decimal
#print(num_str.isdigit())
#print(num_str.isnumeric())


helo_str = "hello world"
#二、查找和替换
#1、判断是否可以指定字符串开始
print(helo_str.startswith("he"))
print(helo_str.startswith("He"))
#2、判断是否指定字符串结束
print(helo_str.endswith("d"))
print(helo_str.endswith("D"))
#3查找指定字符串
print(helo_str.find("o"))#查找字符的索引号
print(helo_str.find("ad"))#指定的字符不存在返回值-1 index报错
#4替换字符串
print(helo_str.replace("h","H"))#replace方法执行完成后会返回一个新的字符，但是不会修改原字符串的值
print(helo_str)

#三、文本对齐
#要求居中对齐
poem = ["\t\n登黄鹤楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

#for poem_str in poem:
   # print("| %s |" % poem_str.rjust(10, " "))

#四、去除空白字符
for poem_str in poem:
    print("| %s |" % poem_str.strip().center(10, " "))

#五、拆分和拼接
