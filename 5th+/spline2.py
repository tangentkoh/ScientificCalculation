# spline2.py (3.11.9)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def splinex(points, new): # スプライン補間に従い補間した値を返す
    points.sort() # 前回のものを少しだけ変更
    n = len(points) - 1
    if n <= 0:
        return 0, 0
    A = np.zeros((4 * n, 4 * n))
    b = np.zeros(4 * n)
    row = 0
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
    for j in range(n - 1):
        x = points[j+1][0]
        A[row, 4*j:4*j+4] = [3*x**2, 2*x, 1, 0]
        A[row, 4*(j+1):4*(j+1)+4] = [-3*x**2, -2*x, -1, 0]
        b[row] = 0
        row += 1
    for j in range(n - 1):
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
    params = np.linalg.solve(A, b)
    R2 = np.zeros_like(new)
    for i, x_val in enumerate(new):
        j = -1
        for k in range(n):
            if points[k][0] <= x_val <= points[k+1][0] or \
               (k == 0 and x_val < points[0][0]) or \
               (k == n-1 and x_val > points[n][0]):
                j = k
                break
        if j != -1:
            aj, bj, cj, dj = params[4*j:4*j+4]
            R2[i] = aj*x_val**3 + bj*x_val**2 + cj*x_val + dj
    return R2

def spline2(f, size, mag):
    A = np.zeros((size * mag, size * mag))
    original = np.arange(size) # 対応する配列を準備
    new = np.arange(size * mag) / mag
    fx = np.zeros((size, size * mag))
    for yy in range(size): # 1変数と仮定して2回行う
        points = [[x, f[yy, x]] for x in original]
        v = splinex(points, new)
        fx[yy, :] = v # 先にxを決める
    original2 = np.arange(size)
    new2 = np.arange(size * mag) / mag
    for xx in range(size * mag):
        points = [[y, fx[y, xx]] for y in original2]
        v2 = splinex(points, new2)
        A[:, xx] = v2
    A = np.clip(A, 0, 255) # 色を範囲内に抑える
    return A.astype(np.uint8)

img = Image.open("Lenna32.png") # ここで対応する画像を設定
size = 32 # 画像のサイズを入力(32, 64)
mag = 8 # 拡大率を入力(8, 4)
imgnp = np.array(img)
r = spline2(imgnp[:, :, 0], size, mag)
g = spline2(imgnp[:, :, 1], size, mag)
b = spline2(imgnp[:, :, 2], size, mag)
imgnp = np.dstack((r, g, b)).astype(np.uint8)
plt.imshow(imgnp)
plt.show()