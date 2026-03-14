# kadai5.py(追加)
# バージョンは 3.11.9
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Lenna.png") # 5-1
imgnp = np.array(img)
print("課題5-1")
tateimgnp = imgnp[::-1, :, :]
plt.imshow(tateimgnp)
plt.show() # 縦反転
yokoimgnp = imgnp[:, ::-1, :]
plt.imshow(yokoimgnp)
plt.show() # 横反転
for j in range(2, 5): # 縮小
    reduimgnp = imgnp[0::j, 0::j]
    plt.imshow(reduimgnp)
    plt.show()
for k in range(2, 5): # 拡大
    nh = 255 * k
    nt = 255 * k
    expaimg = img.resize((nh, nt))
    plt.imshow(expaimg)
    plt.show()
a = 50 # チェッカーパターン
cimgnp = imgnp.copy()
for k in range(0, 256):
    for l in range(0, 256):
        if (k // a + l // a) % 2 == 0:
            cimgnp[k, l, :] = 0
plt.imshow(cimgnp)
plt.show()