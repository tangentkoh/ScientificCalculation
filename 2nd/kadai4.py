# kadai4.py
# バージョンは 3.11.9
import math

a = 1 # 4-2
b = 3
c = 2
D = b**2 - 4*a*c
if D < 0: # 実数解の判定
    print("実数解を持たない")
else:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    if x1 > x2:
        x1, x2 = x2, x1 # 入れ替え
    print(f"解: {x1}, {x2}")
    print("x1のとき " + str(a*x1*x1 + b*x1 + c)) # 4-3
    print("x2のとき " + str(a*x2*x2 + b*x2 + c))