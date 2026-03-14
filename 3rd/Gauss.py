# Gauss.py
# バージョンは 3.11.9
import numpy as np
import sys

# 係数行列と右辺ベクトルを定義
A = np.array([[4., 1., -1],[8., 2., 3],[1., 3., 4.]]) # ここを変えてテスト
b = np.array([1., 12., 6.])

# 係数行列の大きさを取得
n = A.shape[0]

# 拡大行列 G = [A, b] を作る
G = np.hstack((A, b.reshape(n, 1)))

# 確認用：拡大行列を出力
print("初期値(2)")
print(G)
print()

tol = 1e-9

# 前進消去
for k in range(0, n - 1):
    print("k = ", k, ", pivot = " , G[k, k])

    # 部分ピボッティングをここに実装
    pr = k + np.argmax(np.abs(G[k:, k]))

    # ピボット要素がゼロに近い場合、一意解は存在しないとして終了
    if abs(G[pr, k]) < tol:
        print("ピボット要素がゼロに近いので、一意解は存在しない")
        sys.exit(0)

    if pr != k: # 入れ替え
        G[[k, pr], :] = G[[pr, k], :]

    # 前進消去を行う
    for j in range(k+1, n):
        # G[k,k] がゼロに近い場合はエラー処理
        if abs(G[k, k]) < tol:
            print("G[k,k] がゼロに近すぎる")
            sys.exit(0)

        m = G[j,k]/G[k,k]
        for p in range(k, n+1):
            G[j,p] = G[j,p] - m * G[k,p]

    # 確認用
    print(G)
    print()

# 対角要素の確認
if abs(G[n-1, n-1]) < tol:
    print("対角要素に問題があるため、一意解は存在しない")
    sys.exit(0)

# 解を格納する行列を宣言
x = np.zeros(n)

# 後退代入を行う
x[n-1] = G[n-1, n] / G[n-1, n-1]

for i in range(n-2, -1, -1): # n-2 から 0 まで逆順
    s = 0
    for j in range(i+1, n): # シグマ計算
        s = s + G[i,j] * x[j]

    # G[i,i] がゼロに近い場合は後退代入不可
    if abs(G[i, i]) < tol:
        print("後進代入できない")
        sys.exit()
    x[i] = (G[i,n] - s) / G[i,i] # 解の計算

# 解を出力
print("解 x = ", x)