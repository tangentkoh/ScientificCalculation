# kadai2.py (3.11.9)
import numpy as np
import matplotlib.pyplot as plt

# 行列
A = np.array([[1, 4],
              [2, 3]])
l,v = np.linalg.eig(A) # 関数
v = v / np.min(np.abs(v), axis=0) # 絶対値で割る
v = v * np.sign(v[0, :]) # 符号の調整
print("固有値は")
print(l)
print("固有ベクトルは")
print(v)