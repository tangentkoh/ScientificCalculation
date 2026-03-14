# bilinear.py (3.11.9)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def bilinear(f, size, mag):
    A = np.zeros((size * mag, size * mag))
    for n in range(size * mag):
        for m in range(size * mag):
            x = m / mag # 範囲を限定
            y = n / mag 
            xi = int(x)
            yi = int(y)
            xi1 = min(xi + 1, size - 1) # 範囲内に収める
            yi1 = min(yi + 1, size - 1)
            dxi = xi - xi1
            if dxi == 0: # 0で割るのを防ぐ
                dxi = -1 
            dyi = yi - yi1
            if dyi == 0:
                dyi = -1
            dxi1 = xi1 - xi
            if dxi1 == 0:
                dxi1 = 1
            dyi1 = yi1 - yi
            if dyi1 == 0:
                dyi1 = 1
            Q = f[yi, xi] # 左上
            R = f[yi, xi1]
            S = f[yi1, xi]
            T = f[yi1, xi1]
            w1 = ((x - xi1) / dxi * (y - yi1) / dyi) * Q # 左上の式
            w2 = ((x - xi) / dxi1 * (y - yi1) / dyi) * R
            w3 = ((x - xi1) / dxi * (y - yi) / dyi1) * S
            w4 = ((x - xi) / dxi1 * (y - yi) / dyi1) * T
            A[n, m] = w1 + w2 + w3 + w4
            if A[n, m] == 0: # 真っ黒になるのを防ぐ
                A[n, m] = f[n // mag, m // mag]
    return A

img = Image.open("Lenna64.png") # ここで対応する画像を設定
size = 64 # 画像のサイズを入力(32, 64)
mag = 4 # 拡大率を入力(8, 4)
imgnp = np.array(img)
r = bilinear(imgnp[:, :, 0], size, mag)
g = bilinear(imgnp[:, :, 1], size, mag)
b = bilinear(imgnp[:, :, 2], size, mag)
imgnp = np.dstack((r, g, b)).astype(np.uint8) # 合成する
plt.imshow(imgnp)
plt.show()