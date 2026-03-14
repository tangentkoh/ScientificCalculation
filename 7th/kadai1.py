# kadai1.py (バージョンは3.11.9想定)
import numpy as np
import matplotlib.pyplot as plt

def basis(j, k, t):
    s = np.linspace(0, 1, 11) # 0から1までの配列
    if k == 0: # 0次の計算
        if s[j] <= t < s[j+1]:
            return 1.0
        elif t == s[-1] and j == len(s) - 2:
            return 1.0
        else:
            return 0.0
    d1 = s[j+k] - s[j] # 0で割ることの防止
    t1 = 0.0
    if d1 != 0.0: # 1項目の計算
        t1 = ((t - s[j]) / d1) * basis(j, k-1, t)
    d2 = s[j+k+1] - s[j+1]
    t2 = 0.0
    if d2 != 0.0: # 2項目
        t2 = ((s[j+k+1] - t) / d2) * basis(j+1, k-1, t)
    return t1 + t2

ts = np.linspace(0, 1, 101) # 101個に区切る
ds = [0, 1, 2, 3, 4] # 0次から4次指定
for k in ds:
    plt.figure(figsize=(8, 4))
    mj = 11 - k - 1 # 各次数kに対して
    for j in range(mj):
        y = [basis(j, k, t) for t in ts]
        plt.plot(ts, y, label="d")
    plt.title(f"{k}d-Bspline")
    plt.grid(True) # グリッド線追加
    plt.show() # 次数ごとで