# lagrange.py (3.11.9)
import numpy as np
import matplotlib.pyplot as plt

# 課題１：ラグランジュの補間多項式に従い補間した(x,y)を返す
# 引数：points: 標本点のリスト [[x0, y0], [x1, y1], ...]
# 返値：x座標とy座標の np.array 配列
def lagrange_polynomial(points):
    # x を [-1..1] の 0.01 刻みの配列として初期化。これに対応する配列 y を求めていく
    x = np.arange(-1,1,0.01)
    # y を x と同じ大きさのゼロの配列として初期化しておく
    y = np.zeros(len(x))

    # 乗算用の関数
    def l(k, val):
        re = 1.0
        xj = points[k][0]
        for m in range(len(points)):
            if k != m:
                xm = points[m][0]
                re *= (val - xm) / (xj - xm)
        return re

    # ラグランジュ補間式に従って x から y を計算する
    # なお、標本点の x_n は points[n][0], y_n は points[n][1] としてとれる
    for k in range(len(points)):
        yk = points[k][1] # 標本点の y_k
        xk = points[k][0] # 標本点の x_k
        f = l(k, x)
        v = l(k, xk)
        y += f * yk / v

    return(x, y)

# メイン
# テスト用の標本点
test_samples = [
    [-0.6, -0.3],
    [-0.1, 0.5],
    [0.5, 0.1]]

# 課題用の標本点
# 課題ごとに x 座標あるいは y 座標を以下から適当にずらして使うこと
# 以下y座標をずらした
eval_samples = [
    [-0.8, -0.3],
    [-0.4, 0.4],
    [0.0, 0.4],
    [0.3, -0.2],
    [0.9, -0.1]]

# 描画用のキャンパスを用意
fig = plt.figure()
ax=fig.add_subplot(1,1,1)
# 軸が自動的に調整されるのを防ぐため、グラフのX軸とY軸の値域をそれぞれ [-1, 1] に固定
plt.xlim([-1,1])
plt.ylim([-1,1])

### データを生成
# ラグランジュ補間多項式
#x, y = lagrange_polynomial(test_samples)
x, y = lagrange_polynomial(eval_samples)

# グラフを表示
plt.plot(x,y)
#plt.scatter([p[0] for p in test_samples], [p[1] for p in test_samples]) # サンプル
plt.scatter([p[0] for p in eval_samples], [p[1] for p in eval_samples])
plt.show()