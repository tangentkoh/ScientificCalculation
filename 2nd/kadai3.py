# kadai3.py
# バージョンは 3.11.9
import math

def sigdigit(x, approx): # 3-1
    if x == approx: # 完全に一致する場合inf
        return "inf"
    else:
        return -math.log10(abs(x - approx)/abs(x))
a = 39.13
b = 0.3913e2 # 課題2の結果を利用
print(sigdigit(a, b))
a = -375.461
b = -0.3755e3
print(sigdigit(a, b))
a = 0.0006324612
b = 0.6325e-3
print(sigdigit(a, b))
a = -3843.87
b = -0.3844e4
print(sigdigit(a, b))