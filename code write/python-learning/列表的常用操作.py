"""
数据容器列表的常用操作
"""
my_list = ['itheima','itcast','python']
#查找某元素在列表内的下标索引， 语法：列表.index(元素)
index = my_list.index('itheima')
print(f"itheima的下标索引值是 {index}")
#修改特定位置的值 语法：列表【下标】=值
my_list[0]="传智教育"
print(my_list[0])
#插入元素语法：列表.insert(下标，元素)在指定的下标位置，插入指定的元素
my_list = [1,2,3]
my_list.insert(1,'itheima')
print(my_list)
#追加元素 语法：列表.append(元素）,将指定元素追加到列表的尾部
my_list.append("heima")
print(my_list)
#追加元素方法二：语法：列表extend(其他元素容器），将其它数据容器的内容取出，依次追加到列表的尾部
my_list = [1,2,3]
my_list.extend([3,4,5])
print(my_list)
#删除指定元素（两种方法）
my_list = ['itheima','itcast','python']
#法1；del列表（下标）
del my_list[2]
print(f"列表删除元素后结果是：{my_list}")
#法二：列表。pop(下标）
my_list = ['itheima','itcast','python']
elment = my_list.pop(2)
print(f"列表通过pop方法取出元素后结果是：{my_list}，取出的元素是{elment}")
#删除某元素在列表的第一个匹配项
#语法：列表.remove(元素）从头到尾搜索删除第一个
my_list = ['itheima','itheima','itcast','python']
my_list.remove("itheima")
print(f"通过remove方法移除的元素后，列表的结果是：{my_list}")
#清空列表
my_list.clear()
print(f"列表被清空了，结果是：{my_list}")
#统计某元素在列表中的数量
#语法：列表.count(元素）
my_list = ['itheima','itheima','itcast','python']
count = my_list.count("itheima")
print(f"列表中itheima的数量是：{count}")
#统计列表中全部的元素数量
#语法len（列表）
count = len(my_list)
print(f"列表的元素数量是{count}")


