# 通过占位形式完成字符串和变量的拼接
name = '黑马程序员'
message = '学IT来：%s' % name
print(message)
class_num = 57
avg_salary = 16875
message = 'python大数据学科北京%s期，平均工资%s' % (class_num, avg_salary)
print(message)

num1 = 11
num2 = 14.13
print('宽度控制在5，结果是:%5d' % num1)
name = '传智播客'
stock_price = 19.99
stock_code = 303032
stock_price_daliy_growth_factor = 1.2
growth_days = 7
print(f"公司：{name} 当前股价{stock_price} 股票代码{stock_code}")

