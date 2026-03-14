# kadai3.py (バージョンは3.11.9想定)
import numpy as np
import matplotlib.pyplot as plt

def basis3(j, k, t, s): # さらにそのまま利用
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
        t1 = ((t - s[j]) / d1) * basis3(j, k-1, t, s)
    d2 = s[j+k+1] - s[j+1]
    t2 = 0.0
    if d2 != 0.0:
        t2 = ((s[j+k+1] - t) / d2) * basis3(j+1, k-1, t, s)
    return t1 + t2

t = np.linspace(0, 2*np.pi, 100) # 元データの生成
x = np.cos(t)
y = np.sin(t)
ts = np.linspace(0, 1, 100)
ds = [1, 3] # 次数(1と3)
ss = [4, 8, 16] # ノット数(4, 8, 16)
for k in ds:
    for m in ss:
        s = np.linspace(0, 1, m)
        p = m - k - 1
        A = np.zeros((len(ts), p))
        for l in range(len(ts)): # Aを作成
            for i in range(p):
                A[l, i] = basis3(i, k, ts[l], s)
        px, _, _, _ = np.linalg.lstsq(A, x, rcond=None) # x方向について計算
        py, _, _, _ = np.linalg.lstsq(A, y, rcond=None) # y方向について計算
        xs = np.zeros_like(ts)
        ys = np.zeros_like(ts)
        for i in range(p): # スプライン近似
            v = np.array([basis3(i, k, t_val, s) for t_val in ts])
            xs += px[i] * v
            ys += py[i] * v
        plt.figure(figsize=(6, 6))
        plt.title(f"{k}d-{m}")
        plt.plot(xs, ys, color='red', label=f'B-Spline')
        plt.scatter(px, py, color='red', marker='x', label='P')
        plt.scatter(x, y, s=5, label='Data')
        plt.axis('equal')
        plt.legend()
        plt.grid(True)
        plt.show()