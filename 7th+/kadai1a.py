import numpy as np
from PIL import Image

def basis(j, k, t, s):
    if k == 0:
        if s[j] <= t < s[j+1]: 
            return 1.0
        elif t == s[-1] and j == len(s) - 2: 
            return 1.0
        else: 
            return 0.0
    d1 = s[j+k] - s[j]
    d2 = s[j+k+1] - s[j+1]
    t1 = 0.0
    t2 = 0.0
    if d1 != 0.0:
        t1 = ((t - s[j]) / d1) * basis(j, k-1, t, s)
    if d2 != 0.0:
        t2 = ((s[j+k+1] - t) / d2) * basis(j+1, k-1, t, s)
    return t1 + t2

def basisx(ts, k, s):
    p = len(s) - k - 1
    A = np.zeros((len(ts), p))
    for l in range(len(ts)):
        for i in range(p):
            A[l, i] = basis(i, k, ts[l], s)
    return A

# メイン
img = Image.open('image.png')
imgx = np.array(img).astype(float) / 255.0
h, w, c = imgx.shape
ts = np.linspace(0, 1, h)
k = 3 

for m in [10, 40]: # ノット数
    s = np.linspace(0, 1, m)
    A = basisx(ts, k, s)
    A_pinv = np.linalg.pinv(A) # 最小二乗法
    
    r = np.zeros_like(imgx)
    for i in range(c):
        Y = imgx[:, :, i]
        P = A_pinv @ Y @ A_pinv.T
        r[:, :, i] = A @ P @ A.T

    imgr = Image.fromarray((np.clip(r, 0, 1) * 255).astype(np.uint8))
    imgr.save(f'{m}.png')