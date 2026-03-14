# polyfit-1.py
# バージョンは 3.11.9 想定
import numpy as np
import matplotlib.pyplot as plt
# データの入力
data = np.loadtxt("bikesharing.csv",delimiter=",",skiprows=1)
data = data[data[:, 1] == 1]
x = data[:,11]
y = data[:,14]

# 直線の正規方程式を立てる(m=1ver)
n = len(x)
sx = np.sum(x)
sy = np.sum(y)
sx2 = np.sum(x**2)
sxy = np.sum(x*y)
A = np.array([[n, sx],
              [sx, sx2]])
b = np.array([sy,
              sxy])

# 正規方程式を解く
c = np.linalg.solve(A, b)

# 多項式をテキスト出力
print("多項式: y =")
print(c[0], "+")
print(c[1], "x")
# 推定値のベクトルを作成
yy = c[0] + c[1] * x
# LMSEを計算して値をテキスト出力
print("LMSE:", np.mean((y - yy)**2))
# グラフを表示
plt.plot(x, yy, label="predicted")
plt.scatter(x, y, label="real")
plt.legend(loc=2)
plt.show()