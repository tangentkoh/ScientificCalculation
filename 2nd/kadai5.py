# kadai5.py
# バージョンは 3.11.9
import math
true_f = math.exp(1)

def sigdigit(approx, true_value): # 5-1
    return abs((approx - true_value) / true_value)
f = 1.0
t = 1.0
for n in range(1, 21): # 99回だと多いので減少
    t = t / n
    f += t
    print("%.20e %f" % (f, sigdigit(f, true_f)))