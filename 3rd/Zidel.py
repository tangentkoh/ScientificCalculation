# Zidel.py
# バージョンは 3.11.9
import numpy as np

# 問題の設定
A = np.array([[4.1, 1.4],[8.2, 3.8]]) # ここを変えてテスト
b = np.array([11.77, 28.14])
n = A.shape[0]

# 解ベクトルを用意 初期値を設定
x = np.array([0.0] * n)
x_old = np.array([0.0] * n)

eps = 0.0001

# 設定確認のため出力
print("A  = ", A)
print("b  = ", b)
print("x0 = ", x)
print()

# カウンタを初期化
count = 0
d = 100000 # 最初の差分を大きな値に設定

# 行列 A, b を対角成分が1になるよう変形
# 各行を対角成分で割る
Ap = np.copy(A)
bp = np.copy(b)
for i in range(n):
    # 各行を対角成分 a_ii で割る
    div = Ap[i, i]
    Ap[i, :] /= div
    bp[i] /= div
print(f"k={count:02d}: x={x}, d=-")

# メインループ。差分が eps を下回るか count が 100 を超えたらループ終了
while (count < 100):
    x_old = np.copy(x)

    # ガウス・ザイデル法で x を更新する
    for i in range(n):
        s = 0.0
        for j in range(n):
            if i != j:
                s += Ap[i, j] * x[j]

        # 更新し、直ちに上書き
        x[i] = bp[i] - s

    # x_m と x_(m+1) の差分を計算
    d = np.max(np.abs(x - x_old))

    # count をインクリメント
    count += 1

    # 結果を出力
    print(f"k={count:02d}: x={x}, d={d:.6f}")

    # 差分が eps を下回ればループを抜ける
    if d < eps:
        break

# ループから抜けたら、解・最終差分・ループカウントを出力して終了
print()
print("x = ", x)
print(f"d = {d:.6f}")
print(f"count = {count}")