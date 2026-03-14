# kadai.py (3.11.9) 今回はスクリプト1つで完結
import numpy as np
import matplotlib.pyplot as plt

# ----------課題0----------
data = np.loadtxt("bikesharing.csv", delimiter=",", skiprows=1)
times = data[:, 0] # 通し番号を時間として使用(そのまま)
ondo0 = data[:, 8] # 温度、湿度、体感温度、風速
situdo0 = data[:, 10]
tondo0 = data[:, 9]
husoku0 = data[:, 11]
mean = np.mean(ondo0) # 正規化(標準化)
std = np.std(ondo0)
ondo = (ondo0 - mean) / std
mean = np.mean(situdo0)
std = np.std(situdo0)
situdo = (situdo0 - mean) / std
mean = np.mean(tondo0)
std = np.std(tondo0)
tondo = (tondo0 - mean) / std
mean = np.mean(husoku0)
std = np.std(husoku0)
husoku = (husoku0 - mean) / std
c = np.column_stack((ondo, situdo, tondo, husoku)) # 結び付ける

# ----------課題1----------
ns = len(c)
S = (c.T @ c) / ns # 分散共分散行列
l, w = np.linalg.eig(S)
idx = l.argsort()[::-1] # 固有値順
l, w = l[idx], w[:, idx]
scores = c @ w
print("課題1") # 結果の表示
for i in range(3):
    ki = l[i] / np.sum(l)
    print(f"第{i+1}主成分(寄与率:{ki:.4f})")
    print(f"z{i+1} = {w[0,i]:.4f}x1 + {w[1,i]:.4f}x2 + {w[2,i]:.4f}x3 + {w[3,i]:.4f}x4")
plt.figure(figsize=(12, 6))
mean = np.mean(times)
std = np.std(times)
time = (times - mean) / std
for i in range(3):
    plt.plot(time, scores[:, i], label=f"Score{i+1}", alpha=0.8)
plt.title("score graph")
plt.xlabel("time")
plt.ylabel("score")
plt.legend()
plt.grid(True)
plt.show() # グラフを表示
print()

# ----------課題2----------
def get_polyfit(x, y, m): # m次な線形回帰関数
    m2 = m + 1 # 係数補正
    A = np.zeros((m2, m2))
    b = np.zeros(m2)
    for i in range(m2):
        for j in range(m2):
            A[i, j] = np.sum(x**(i+j))
        b[i] = np.sum(y * (x**i))
    c2 = np.linalg.solve(A, b)
    return c2

pep0 = data[:, 14] # 人数
mean = np.mean(pep0) # 一応正規化(標準化)
std = np.std(pep0)
pep = (pep0 - mean) / std
print("課題2")
for i in range(2): # 第1と第2
    for m in [1, 3]: # 1次と3次
        cc = get_polyfit(scores[:, i], pep, m)
        eq_str = " + ".join([f"{cc[j]:.4f}x^{j}" for j in range(m+1)])
        print(f"第{i+1}-{m}次")
        print(f"y = {eq_str}")
print()

# ----------課題3----------
def lagrange_polynomial(points, x3):
    y3 = np.zeros_like(x3)
    n = len(points)
    for k in range(n):
        xk, yk = points[k] # 標本点のy_kとx_k
        lk = np.ones_like(x3)
        for m in range(n):
            if k != m:
                xm = points[m][0]
                lk *= (x3 - xm) / (xk - xm)
        y3 += yk * lk
    return y3 # yだけを返す

def spline3(points, x3):
    points = points[points[:, 0].argsort()] # ソート
    n = len(points) - 1
    xs0 = points[:, 0]
    ys0 = points[:, 1]
    minx, maxx = xs0[0], xs0[-1] # 正規化
    xs = (xs0 - minx) / (maxx - minx)
    xe = (x3 - minx) / (maxx - minx)

    A = np.zeros((4*n, 4*n))
    b = np.zeros(4*n)
    row = 0
    for j in range(n):
        A[row, 4*j:4*j+4] = [xs[j]**3, xs[j]**2, xs[j], 1]
        b[row] = ys0[j]
        row += 1
        A[row, 4*j:4*j+4] = [xs[j+1]**3, xs[j+1]**2, xs[j+1], 1]
        b[row] = ys0[j+1]
        row += 1
    for j in range(n-1):
        x = xs[j+1]
        A[row, 4*j:4*j+4] = [3*x**2, 2*x, 1, 0]
        A[row, 4*(j+1):4*(j+1)+4] = [-3*x**2, -2*x, -1, 0]
        row += 1
        A[row, 4*j:4*j+4] = [6*x, 2, 0, 0]
        A[row, 4*(j+1):4*(j+1)+4] = [-6*x, -2, 0, 0]
        row += 1
    A[row, 0:4] = [6*xs[0], 2, 0, 0]
    row += 1
    A[row, 4*(n-1):4*(n-1)+4] = [6*xs[-1], 2, 0, 0]
    
    params = np.linalg.solve(A, b)
    y3 = np.zeros_like(x3)
    for j in range(n):
        aj, bj, cj, dj = params[4*j:4*j+4]
        dd = (xe >= xs[j]) & (xe <= xs[j+1] + 1e-9)
        xt = xe[dd]
        y3[dd] = aj*xt**3 + bj*xt**2 + cj*xt + dj
    return y3

print("課題3(グラフ表示のみ)")
xw = np.linspace(1, 731, 500) # 先にx方向の幅を指定
for npts in [5, 11]: # サンプリング数
    idx = np.linspace(0, ns - 1, npts).astype(int)
    pts = np.column_stack((times[idx], scores[idx, 0])) # 第1
    plt.figure(figsize=(10, 5))
    plt.plot(xw, lagrange_polynomial(pts, xw), color="blue", label="Lagrange")
    plt.plot(xw, spline3(pts, xw), color="red", label="Spline")
    plt.scatter(pts[:, 0], pts[:, 1], color="gray", label="Sample")
    plt.title(f"d1(n={npts})")
    plt.xlabel("time")
    plt.ylabel("score")
    plt.legend()
    plt.grid(True)
    plt.show() # グラフを重ねて表示
for npts in [5, 11]: # サンプリング数(もう一回)
    idx = np.linspace(0, ns - 1, npts).astype(int)
    pts = np.column_stack((times[idx], scores[idx, 1])) # 第2
    plt.figure(figsize=(10, 5))
    plt.plot(xw, lagrange_polynomial(pts, xw), color="blue", label="Lagrange")
    plt.plot(xw, spline3(pts, xw), color="red", label="Spline")
    plt.scatter(pts[:, 0], pts[:, 1], color="gray", label="Sample")
    plt.title(f"d2(n={npts})")
    plt.xlabel("time")
    plt.ylabel("score")
    plt.legend()
    plt.grid(True)
    plt.show() # グラフを重ねて表示
print()

# ----------課題4----------
def basis2(j, k, t, s):
    if k == 0:
        return 1.0 if s[j] <= t < s[j+1] else 0.0
    v1 = 0; d1 = s[j+k] - s[j]
    if d1 != 0: v1 = (t - s[j]) / d1 * basis2(j, k-1, t, s)
    v2 = 0; d2 = s[j+k+1] - s[j+1]
    if d2 != 0: v2 = (s[j+k+1] - t) / d2 * basis2(j+1, k-1, t, s)
    return v1 + v2

print("課題4(グラフ表示のみ)")
for ms in [7, 11]: # ノット数
    key = 3
    ps = ms - key - 1
    s = np.linspace(1, 731, ms)
    A2 = np.zeros((ns, ps)) # 基底関数行列
    for i in range(ns):
        for j in range(ps):
            A2[i, j] = basis2(j, key, times[i], s)
    xcs, _, _, _ = np.linalg.lstsq(A2, scores[:, 0], rcond=None) # 最小二乗法(第1)
    ybs = np.zeros_like(xw)
    for j in range(ps):
        ybs += xcs[j] * np.array([basis2(j, key, t, s) for t in xw])
    plt.figure(figsize=(10, 5))
    plt.scatter(times, scores[:, 0], s=1, color="gray", label="Data")
    plt.plot(xw, ybs, color="red", label=f"BSpline")
    plt.title(f"d1(m={ms})")
    plt.xlabel("Time")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)
    plt.show()
for ms in [7, 11]: # ノット数(もう一回)
    key = 3
    ps = ms - key - 1
    s = np.linspace(1, 731, ms)
    A2 = np.zeros((ns, ps)) # 基底関数行列
    for i in range(ns):
        for j in range(ps):
            A2[i, j] = basis2(j, key, times[i], s)
    xcs, _, _, _ = np.linalg.lstsq(A2, scores[:, 1], rcond=None) # 最小二乗法(第2)
    ybs = np.zeros_like(xw)
    for j in range(ps):
        ybs += xcs[j] * np.array([basis2(j, key, t, s) for t in xw])
    plt.figure(figsize=(10, 5))
    plt.scatter(times, scores[:, 1], s=1, color="gray", label="Data")
    plt.plot(xw, ybs, color="red", label=f"BSpline")
    plt.title(f"d2(m={ms})")
    plt.xlabel("Time")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)
    plt.show()
print()

# ----------課題5----------
# 未