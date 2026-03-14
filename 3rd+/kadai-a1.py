# kadai-a1.py
# バージョンは 3.11.9
import numpy as np

# 前回のガウス法(ピポッティング有り)
def gauss(A, b):
    n = A.shape[0]
    G = np.hstack((A, b.reshape(n, 1)))
    tol = 1e-9 # 誤差
    for k in range(0, n - 1):
        pr = k + np.argmax(np.abs(G[k:, k]))
        if abs(G[pr, k]) < tol:
            return 0 # 今回は0を返して終了
        if pr != k:
            G[[k, pr], :] = G[[pr, k], :]
        for j in range(k+1, n):
            if abs(G[k, k]) < tol:
                return 0 # 失敗
            m = G[j,k]/G[k,k]
            for p in range(k, n+1):
                G[j,p] = G[j,p] - m * G[k,p]
    if abs(G[n-1, n-1]) < tol:
        return 0 # 失敗
    x = np.zeros(n)
    if abs(G[n-1, n-1]) < tol:
        return 0 # 失敗
    else:
        x[n-1] = G[n-1, n] / G[n-1, n-1]
        for i in range(n-2, -1, -1):
            s = 0
            for j in range(i+1, n):
                s = s + G[i,j] * x[j]
            if abs(G[i, i]) < tol:
                return 0 # 失敗
            x[i] = (G[i,n] - s) / G[i,i]
    return x

# データの読み込み(埋立する)
data = np.genfromtxt('sample.csv', delimiter=',')
print("読み込んだデータ")
print(data)
print()
data = np.genfromtxt('sample.csv', delimiter=',', filling_values=0)

# データの分割と計算
for i in range(len(data)):
    x = data[i]
    y = 0 # 要素数の計測
    for j in range(len(x)):
        if x[j] == 0:
            break
        y += 1
    x = x[:y]
    c = 0
    d = 0
    for j in range(y): # 変形処理
        if y == j * (j+1):
            c = j
            d = j+1
            break
    x = np.reshape(x, (c, d))
    A = x[:, :c]
    b = x[:, c]
    print("入",x)
    print("解",gauss(A, b))
    print()