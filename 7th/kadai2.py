# kadai2.py (バージョンは3.11.9想定)
import numpy as np
import matplotlib.pyplot as plt

def basis2(j, k, t, s): # ほぼそのまま利用
    if k == 0:
        if s[j] <= t < s[j+1]:
            return 1.0
        elif t == s[-1] and j == len(s) - 2:
            return 1.0
        else:
            return 0.0
    d1 = s[j+k] - s[j]
    t1 = 0.0
    if d1 != 0.0:
        t1 = ((t - s[j]) / d1) * basis2(j, k-1, t, s)
    d2 = s[j+k+1] - s[j+1]
    t2 = 0.0
    if d2 != 0.0:
        t2 = ((s[j+k+1] - t) / d2) * basis2(j+1, k-1, t, s)
    return t1 + t2

data = np.loadtxt("bikesharing.csv", delimiter=",", skiprows=1)
x = (data[:, 0] - 1) / (731 - 1)
y = data[:, 14]
ds = [2, 3] # 次数(2と3)
ss = [11, 21] # ノット数(11と12)
for k in ds:
    for m in ss: # ノット数より
        p = m - k - 1
        s = np.linspace(0, 1, m) # 先に作成
        n = len(x)
        A = np.zeros((n, p))
        for i in range(n): # Aを作成
            for j in range(p):
                A[i, j] = basis2(j, k, x[i], s)
        xp, _, _, _= np.linalg.lstsq(A, y, rcond=None) # 最小二乗法の計算
        ts2 = np.linspace(0, 1, 100)
        yp = np.zeros_like(ts2)
        for j in range(p): # スプライン近似
            yp += xp[j] * np.array([basis2(j, k, t, s) for t in ts2])
        plt.figure(figsize=(8, 4))
        plt.scatter(x, y, s=1, label="Data")
        plt.plot(ts2, yp, color='red', lw=2, label="B-spline")
        plt.title(f"{k}d-{m}")
        plt.legend()
        plt.grid(True)
        plt.show()