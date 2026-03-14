# kadai1.py (3.11.9)
import numpy as np
import matplotlib.pyplot as plt

# 行列
A = np.array([[1, 4],
              [2, 3]])
# 固有値
l1 = -1
l2 = 5
# 固有ベクトル
v1 = np.array([[-2],
               [1]])
v2 = np.array([[1],
               [1]])
# 1. Av = lv
print("A @ v1 は")
print(A @ v1)
print("l1 * v1 は")
print(l1 * v1)
print("A @ v2 は")
print(A @ v2)
print("l2 * v2 は")
print(l2 * v2)
print()
# 2. 固有値の和は A のトレースに等しい
print("固有値の和は")
print(l1 + l2)
print("Aのトレースは")
print(np.trace(A))
print()
# 3. 固有値の積は A の行列式に等しい
print("固有値の積は")
print(l1 * l2)
print("Aの行列式は")
print(int(np.linalg.det(A)))