# poly_lin2.py
# バージョンは 3.11.9 想定
import numpy as np
import matplotlib.pyplot as plt

# 関数
def poly_lin2(x, y):
    V = np.vstack([x**2, y**2, x*y, x, y, np.ones_like(x)]).T # 一気に計算
    VTV = V.T @ V
    val, vec = np.linalg.eig(VTV)
    m = np.argmin(val)
    abcdef = vec[:, m]
    a, b, c, d, e, f = abcdef
    return a, b, c, d, e, f

# データの入力
data = np.loadtxt("c1.txt",delimiter=" ",skiprows=1)
x = data[:,0]
y = data[:,1]

# 計算と出力
a, b, c, d, e, f = poly_lin2(x, y)
x_min, x_max = np.min(x) - 1.0, np.max(x) + 1.0
y_min, y_max = np.min(y) - 1.0, np.max(y) + 1.0
points = 300
xg = np.linspace(x_min, x_max, points)
yg = np.linspace(y_min, y_max, points)
xx, yy = np.meshgrid(xg, yg)
z = a * xx**2 + b * yy**2 + c * xx * yy + d * xx + e * yy + f
print("式:", a, "x^2 +", b, "y^2 +", c, "xy",)
print("+", d, "x +", e, "y +", f, "= 0")
plt.contour(xx, yy, z, levels=[0])
plt.scatter(x, y)
plt.legend(loc=2)
plt.show()