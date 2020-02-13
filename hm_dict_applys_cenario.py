# card_list = [
#     {"name": "张山", "qq": "8535", "phone": "188"},
#     {"name": "李四", "qq": "3585", "phone": "10086"}
# ]
# for info in card_list:
#     print(info)
#
# info_dict = {"name": "李四", "qq": "3585", "phone": "10086"}
# #变量k是每一次循环中，获取到的键值对的key
# for k in info: #
#     print("%s - %s" %(k, info_dict[k])

#1统计键值对的数量
mess_dict = {"name": "张山", "qq": "8535", "phone": "188"}
print(len(mess_dict))
#2合并字典
temp_dict = {"height": 175, "qq": "12345"}
mess_dict.update(temp_dict)
print(mess_dict)
#合并字典时，如果添加的字典里面有与被合并字典里面相似的内容会覆盖之前的内容
#3清空字典
mess_dict.clear()
print(mess_dict)

new_dict = {"name": "刘周"}
print(new_dict)
#1字典取值
print(new_dict["name"])
#print(new_dict["name12"])取值的时候，指定的key不存在会报错
#2增加/修改
new_dict["age"] = 25
new_dict["name"] = "小妹"
#如果key不存在，新增；如果存在key，则修改key的值
#3删除(pop)
new_dict.pop("name")
#new_dict.pop("name1")key错误会报错
print(new_dict)