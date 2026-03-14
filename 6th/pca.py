# pca.py (3.11.9)
import numpy as np
import matplotlib.pyplot as plt

# 行列(元のデータ)
A = [[8, 9, 4],
     [2, 5, 7],
     [8, 5, 6],
     [3, 5, 4],
     [7, 4, 9],
     [4, 3, 4],
     [3, 6, 8],
     [6, 8, 2],
     [5, 4, 5],
     [6, 7, 6]]
A = np.array(A)
n = len(A)
n2 = len(A[0])
# 平均ベクトル
m = np.zeros(n2)
for i in range(n2):
    x = 0
    for j in range(n):
        x += A[j][i]
    m[i] = x / n
Bdash = A - m
S = (Bdash.T @ Bdash) / n # 分散共分散行列
l,w = np.linalg.eig(S)
y = l.argsort()[::-1] # 固有値順に
l = l[y]
w = w[:, y]
print(f"平均ベクトル:{m}")
lsum = np.sum(l)
lsum2 = 0
for i in range(n2):
    print(f"第{i+1}主成分")
    print(f"z{i+1} = {w[0,i]:.4f}(x1 - {m[0]:.1f}) + {w[1,i]:.4f}(x2 - {m[1]:.1f}) + {w[2,i]:.4f}(x3 - {m[2]:.1f})")
    ki = l[i] / lsum
    print(f"寄与率:{ki:.4f}")
    lsum2 += l[i]
    sumki = lsum2 / lsum
    print(f"累積寄与率:{sumki:.4f}")