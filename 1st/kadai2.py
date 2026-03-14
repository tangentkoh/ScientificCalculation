# kadai2.py
# バージョンは 3.11.9

import numpy as np

F = [0, 1, 1] # 2-1
for i in range(3, 31):
  a = F[i-1] + F[i-2]
  F.append(a)
print("課題2-1")
print(F[30])

b = 0 # 2-2
while b * b < 3000:
  b += 1
print("課題2-2")
print(b - 1)

np.random.seed(9) # 2-3
c = np.random.normal(80.0, 10.0, 100000)
ave = sum(c) / len(c)
sta = np.std(c)
print("課題2-3")
print(ave)
print(sta)
maxc = np.amax(c)
minc = np.amin(c)
print(maxc)
print(minc)

d = np.array([[9, 5, 0], # 2-4
              [9, 3, 0],
              [5, 4, 9]])
e = np.array([[5, 10, 5],
              [4, 4, 1],
              [6, 10, 4]])
f = np.array([[10],
              [6],
              [7]])
v = d * e * f
print("課題2-4")
print(v)