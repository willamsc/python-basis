name_list = ['itheima','itcase','python']
print(name_list)
print(type(name_list))
my_list = ['itheima',666,True]
print(my_list)
print(type(my_list))
 #定义一个嵌套的列表
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))
#列表索引
my_list = ['Tom','lily','rose']
#列表【下标】，从前往后从0开始每次加一，从后往前从-1开始每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
#倒序索引
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
#嵌套的列表索引
my_list = [[1,2,3],[4,5,6]]
#语法：列表[外面的下标][里面的下标]
print(my_list[0][0])