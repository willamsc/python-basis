"""定义一个字典"""
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
#新增元素
my_dict["张信哲"] = 66
print(f"经过字典的的新增内容为{my_dict}")
#更改元素
my_dict["周杰伦"] = 33
print(f"经过改变字典内容为{my_dict}")
#删除元素
score = my_dict.pop("周杰伦")
print(f"字典经过删除后的结果是{my_dict}，删除的元素是{score}")
#清空元素
my_dict.clear()
print(f"字典被清空了结果是{my_dict}")
#获取全部的key
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict.keys()
print(f"字典的全部key是{keys}")
#遍历字典
#方式一：
for key in keys:
    print(f"key是{key}")
    print(f"value是{my_dict[key]}")
#方式二：
for key in my_dict:
    print(f"2key是{key}")
    print(f"2value是{my_dict[key]}")
#统计字典元素的数量
num = len(my_dict)
print(f"字典的元素数量是{num}")