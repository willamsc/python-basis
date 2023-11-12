#使用range循环获取从一到num的整数判断有多少个偶数
num = 0
for x in range(1, 101):
    if x % 2 ==0:
        num = num+1
print(num)
