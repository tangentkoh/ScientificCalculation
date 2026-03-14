import numpy as np

# 例として、課題1のテスト(2)の係数行列を使用
A = np.array([[4., 1., -1.],
              [8., 2., 3.],
              [1., 3., 4.]])

# L2ノルムを計算
norm_A_l2 = np.linalg.norm(A, 2)

print(f"行列AのL2ノルム:{norm_A_l2}")

cond_A_l2 = np.linalg.cond(A, 2)

print(f"行列Aの条件数:{cond_A_l2}")

# 悪条件の例 (ほぼ線形従属)
#B = np.array([[1.000, 2.000],
#              [1.001, 2.001]])
#cond_B_l2 = np.linalg.cond(B, 2)
#
#print(f"行列 B の条件数 (L2): {cond_B_l2}")