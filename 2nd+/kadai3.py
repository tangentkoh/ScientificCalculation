# kadai3.py(追加)
# バージョンは 3.11.9
import math
import numpy as np

def printMyfloat(r):
    w = str(r[1])
    x = int(w, 2)
    a = r[0] * (1 + x * math.pow(2, -24)) * math.pow(2, r[2])
    return a

def printthis(r): # 今回の浮動小数点数を表示
    w = str(r[1])
    x = int(w, 2)
    a2 = r[0] * (1 + x * math.pow(2, -24)) * math.pow(2, r[2]) # ここまで利用
    a2 = round(a2, 4)
    return a2

r = [1, 100110011001100110011001, -4] # 前問の結果(0.1)
print(printMyfloat(r))
print(printthis(r))
r2 = [1, 111101000000000000000011, 9] # 前問の結果(1000.0001)
print(printMyfloat(r2))
print(printthis(r2))
r3 = [1, 111011011101001011110001, 6] # 前問の結果(123.456)
print(printMyfloat(r3))
print(printthis(r3))