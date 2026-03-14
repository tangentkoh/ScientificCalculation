# kadai-a2.py
# バージョンは 3.11.9
import numpy as np
import time
import matplotlib.pyplot as plt

# 対角優位な行列を作成
def diagdominantMat(rows):
    A = np.random.rand(rows,rows)
    for i in range(rows):
        sum = 0
        for j in range(rows):
            sum += abs(A[i,j])
        A[i,i] = sum
    return A

def dMat2(rows):
    b = np.random.rand(rows)
    return b

# ガウス(ピポ有)
# 対角優位が保証されているので(公平性からも)エラー処理は省略
def gauss(A, b):
    n = A.shape[0]
    G = np.hstack((A, b.reshape(n, 1)))
    tol = 1e-9 # 誤差
    for k in range(0, n - 1):
        pr = k + np.argmax(np.abs(G[k:, k]))
        if pr != k:
            G[[k, pr], :] = G[[pr, k], :]
        for j in range(k+1, n):
            m = G[j,k]/G[k,k]
            for p in range(k, n+1):
                G[j,p] = G[j,p] - m * G[k,p]
    x = np.zeros(n)
    x[n-1] = G[n-1, n] / G[n-1, n-1]
    for i in range(n-2, -1, -1):
        s = 0
        for j in range(i+1, n):
            s = s + G[i,j] * x[j]
        x[i] = (G[i,n] - s) / G[i,i]
    return x

# ガウザイ
# 対角優位が保証されているので(公平性からも)エラー処理は省略
def zidel(A, b):
    n = A.shape[0]
    x = np.array([0.0] * n)
    xo = np.array([0.0] * n)
    eps = 0.0001
    count = 0
    d = 1000
    Ap = np.copy(A)
    bp = np.copy(b)
    for i in range(n):
        div = Ap[i, i]
        Ap[i, :] /= div
        bp[i] /= div
    while (count < 1000):
        xo = np.copy(x)
        for i in range(n):
            s = 0.0
            for j in range(n):
                if i != j:
                     s += Ap[i, j] * x[j]
            x[i] = bp[i] - s
        d = np.max(np.abs(x - xo))
        count += 1
        if d < eps:
            break
    return x

# 計算時間の比較
rows = 2
gm = [] # 平均
zm = []
gv = [] # 分散
zv = []
ge = [] # 誤差
ze = []
while(rows <= 20):
    g = [0.0] * 100
    z = [0.0] * 100
    for i in range(100):
        A = diagdominantMat(rows)
        b = dMat2(rows)
        start = time.perf_counter() # ガウス法
        gauss(A, b)
        end = time.perf_counter()
        diff = end - start
        g[i] = diff
        # print("ガウス Act",i+1)
        # print(f"{diff*1000:.4f}","ms")
        start2 = time.perf_counter() # ガウザイ法
        zidel(A, b)
        end2 = time.perf_counter()
        diff2 = end2 - start2
        z[i] = diff2
        # print("ガウザイ Act",i+1)
        # print(f"{diff2*1000:.4f}","ms")
    gm.append(np.mean(g))
    zm.append(np.mean(z))
    gv.append(np.var(g))
    zv.append(np.var(z))
    ge.append(np.sqrt(np.var(g)) / np.sqrt(100))
    ze.append(np.sqrt(np.var(z)) / np.sqrt(100))
    rows += 2
print(gm)
print(zm)
print(gv)
print(zv)
print(ge)
print(ze)
x = np.arange(2, 22, 2)
y = gm
er = ge
plt.errorbar(x, y, yerr=er, label = 'Gauss')
x = np.arange(2, 22, 2)
y = zm
er = ze
plt.errorbar(x, y, yerr=er, label = 'Zidel')
plt.legend()
plt.savefig('my_graph.png')