def user_info(name,age,gender):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")

user_info (name="zjl", age=32, gender="男")
user_info("小明", 20, "男")
# 关键字参数
user_info(name='小王', age=21, gender='女')
user_info(age=24, name="潇潇", gender="女")
user_info('甜甜', gender="女", age=32)

# 缺省参数（默认值）
def user_info(name, age, gender="男"):
    print(f"姓名是：{name}, 年龄是：{age},性别是：{gender}")
user_info("小天", 23)
# 不定长 - 位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args的参数类型是:{type(args)},内容是：{args}")
user_info(1, 2, 3, '小明', '男孩')

# 不定长 - 关键字不定长，**号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")
user_info(name='小王', age=11, gender='男')

