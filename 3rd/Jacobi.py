# Jacobi.py
# バージョンは 3.11.9
import numpy as np

# 問題の設定
A = np.array([[5., -4.],[-1., 2.]]) # ここを変えてテスト
b = np.array([4., 1.])
n = A.shape[0]

# 解ベクトルを用意 初期値を設定
xc = np.array([0.0] * n)
xn = np.array([0.0] * n)

eps = 0.0001

# 設定確認のため出力
print("A  = ", A)
print("b  = ", b)
print("x0 = ", xc)
print()

# カウンタを初期化
count = 0
d = 100 # 最初の差分

# 行列 A, b を対角成分が1になるよう変形
# 対角成分の逆数からなる行列を作成
Di = np.diag(1.0 / np.diag(A))
Ap = Di @ A # 先に乗算しておく
bp = Di @ b

I = np.identity(A.shape[0])
M = I - Ap

print(f"k={count:02d}: x={xc}, d=-")

# メインループ。差分が eps を下回るか count が 100 を超えたらループ終了
while (count < 100):

    # ヤコビ法の更新式、行列計算を1回で行う
    xn = bp + M @ xc

    # x_m と x_(m+1) の差分を計算
    d = np.max(np.abs(xn - xc))

    # count をインクリメント
    count += 1

    # 結果を出力
    print(f"k={count:02d}: x={xn}, d={d:.6f}")

    # 差分が eps を下回ればループを抜ける
    if d < eps:
        break

    # 次のループのために更新
    xc = np.copy(xn)

# ループから抜けたら、解・最終差分・ループカウントを出力して終了
print()
print("x = ", xn)
print(f"d = {d:.6f}")
print(f"count = {count}")