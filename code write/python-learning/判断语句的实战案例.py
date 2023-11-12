import random
num = random.randint(1, 10)
guess_num = eval(input("请输入你猜测的数字"))
if num == guess_num:
    print("第一次就猜中了")
else:
    if num > guess_num:
        print("大了")
    else:
        print("小了")
    guess_num = eval(input("再次请输入你猜测的数字"))
    if guess_num == num:
        print("恭喜你猜对了")
    else:
        print("不好意思又错了")
        if guess_num >num:
            print("大了")
        else:
            print("小了")

