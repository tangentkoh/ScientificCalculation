# spline3.py (3.11.9)
import numpy as np
import matplotlib.pyplot as plt

# 課題３：スプライン補間に従い補間した(x,y)を返す
# 引数：points: 標本点のリスト [[x0, y0], [x1, y1], ...]
# 返値：x座標とy座標の np.array 配列
def spline3(points):
    # 標本点 points を x 座標の順でソートしておく
    points.sort()
    # 標本点の数 len(points) に対して、求める区間数 n をセット
    n = len(points) - 1
    if (n <= 0):
        return 0, 0
    # (4n, 4n) の係数行列を確保。デフォルト値を 0 で埋める
    A = np.zeros((4 * n, 4 * n))
    b = np.zeros(4 * n)
    row = 0
    # スプライン補間の条件に従い、標本点リストから計算して上記の A, b に値を埋めていく。
    for j in range(n):
        xj = points[j][0]
        yj = points[j][1]
        xj1 = points[j+1][0]
        yj1 = points[j+1][1]
        A[row, 4*j:4*j+4] = [xj**3, xj**2, xj, 1]
        b[row] = yj
        row += 1
        A[row, 4*j:4*j+4] = [xj1**3, xj1**2, xj1, 1]
        b[row] = yj1
        row += 1

    for j in range(n-1):
        x = points[j+1][0]
        A[row, 4*j:4*j+4] = [3*x**2, 2*x, 1, 0]
        A[row, 4*(j+1):4*(j+1)+4] = [-3*x**2, -2*x, -1, 0]
        b[row] = 0
        row += 1

    for j in range(n-1):
        x = points[j+1][0]
        A[row, 4*j:4*j+4] = [6*x, 2, 0, 0]
        A[row, 4*(j+1):4*(j+1)+4] = [-6*x, -2, 0, 0]
        b[row] = 0
        row += 1

    x0 = points[0][0]
    xn = points[n][0]
    A[row, 0:4] = [6*x0, 2, 0, 0]
    b[row] = 0
    row += 1
    A[row, 4*(n-1):4*(n-1)+4] = [6*xn, 2, 0, 0]
    b[row] = 0
    row += 1

    # 上記の連立一次方程式を解く。結果は長さ 4n の配列
    params = np.linalg.solve(A, b)

    x = []
    y = []
    xp = np.arange(-1, 1, 0.01) # 刻み

    for j in range(n):
        aj, bj, cj, dj = params[4*j:4*j+4]
        x0 = points[j][0]
        x1 = points[j+1][0]
        xs = xp[(xp >= x0) & (xp <= x1)]
        ys = aj*xs**3 + bj*xs**2 + cj*xs + dj
        x.extend(xs)
        y.extend(ys)

    return(np.array(x), np.array(y)) # ここで変換

# メイン
# テスト用の標本点
test_samples = [
    [-0.6, -0.3],
    [-0.1, 0.5],
    [0.5, 0.1]]

# 課題用の標本点
# 課題ごとに x 座標あるいは y 座標を以下から適当にずらして使うこと
# y座標をずらした
eval_samples = [
    [-0.8, -0.3],
    [-0.4, 0.1],
    [0.0, 0.3],
    [0.3, -0.1],
    [0.9, 0.5]]

# 描画用のキャンパスを用意
fig = plt.figure()
ax=fig.add_subplot(1,1,1)
# 軸が自動的に調整されるのを防ぐため、グラフのX軸とY軸の値域をそれぞれ [-1, 1] に固定
plt.xlim([-1,1])
plt.ylim([-1,1])

### データを生成
# スプライン補間
# x, y = spline3(test_samples)
x, y = spline3(eval_samples)

# グラフを表示
plt.plot(x,y)
# plt.scatter([p[0] for p in test_samples], [p[1] for p in test_samples]) # サンプル
plt.scatter([p[0] for p in eval_samples], [p[1] for p in eval_samples])
plt.show()