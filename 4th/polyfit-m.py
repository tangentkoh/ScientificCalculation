# polyfit-m.py
# バージョンは 3.11.9 想定
import numpy as np
import matplotlib.pyplot as plt

# 関数として計算
def get_polyfit(x, y, m):
    A = [[0] * m for a in range(m)]
    b = [0] * m
    for i in range(m):
        for j in range(m):
            A[i][j] = np.sum(x**(i+j))
    A[0][0] = len(x)
    for i in range(m):
        b[i] = np.sum(y*(x**i))
    c = np.linalg.solve(A, b)
    return c

# データの入力
data = np.loadtxt("springData.txt",delimiter=" ",skiprows=1)
m = 3
x = data[:,1]
y = data[:,0]
m += 1 # 補正
cc = get_polyfit(x, y, m)
yy = 0
print("多項式: y =")
for i in range(m):
    if i == 0:
        print(cc[i], "+")
    elif i == m-1:
        print(cc[i], "x^", i)
    else:
        print(cc[i], "x^", i, "+")
for i in range(m):
    yy += cc[i] * x**i
print("LMSE:", np.mean((y - yy)**2))
plt.plot(x, yy, label="predicted")
plt.scatter(x, y, label="real")
plt.legend(loc=2)
plt.show()