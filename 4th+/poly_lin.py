# poly_lin.py
# バージョンは 3.11.9 想定
import numpy as np
import matplotlib.pyplot as plt

# 関数
def poly_lin(x, y):
    B = np.vstack([x, y]).T # 元の配列の作成
    x0 = np.mean(x) # 平均値を求める
    y0 = np.mean(y)
    V = B - np.array([x0, y0])
    VTV = V.T @ V
    val, vec = np.linalg.eig(VTV) # eig関数を使う
    m = np.argmin(val) # 小さい方の位置を選ぶ
    ab = vec[:, m]
    a = ab[0] # 対応する固有ベクトル
    b = ab[1]
    c = -(x0 * a + y0 * b) # cを導く
    return a, b, c

# データの入力
data = np.loadtxt("springData.txt",delimiter=" ",skiprows=1)
x = data[:,1]
y = data[:,0]

# 計算と出力
a, b, c = poly_lin(x, y)
a2 = -a / b
c2 = -c / b
print("式: y =", a2, "x +", c2)
xx = np.array([0.0, 4.0])
yy = c2 + a2 * xx
plt.plot(xx, yy, label="predicted")
plt.scatter(x, y, label="real")
plt.legend(loc=2)
plt.show()