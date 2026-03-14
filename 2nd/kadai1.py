# kadai1.py
# バージョンは 3.11.9
import math

n = int(input("Enter an integer: ")) # 1-1
for i in range(2, 8):
    x = math.pow(n, 1/i) # math関数を利用
    if x.is_integer(): # 整数の判定
        print(str(i) + "th root of " + str(n) + " is " + str(int(x)))
    else:
        print(str(i) + "th root of " + str(n) + " does not exist")