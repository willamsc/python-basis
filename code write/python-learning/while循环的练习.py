import random
num = random.randint(1, 100)
count = 0

flag = True
while flag:
    count += 1
    guess_num = eval(input("请输入你猜测的数字"))
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")

print(count)
