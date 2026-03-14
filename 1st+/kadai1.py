# kadai1.py(追加)
# バージョンは 3.11.9
# 今回は全ての課題で標準画像"Lenna"を利用
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Lenna.png") # 1-1
imgnp = np.array(img)
qimgnp = imgnp[:256 // 2, :256 // 2] # コピーして面積を1/4に
qimg = Image.fromarray(qimgnp)
print("課題1-1")
plt.imshow(qimg)
plt.show()
qimg.save("lena-quarter.png")

rimgnp = imgnp.copy() # 1-2
gimgnp = imgnp.copy()
bimgnp = imgnp.copy()
rimgnp[:, :, 1] = 0 # 上から赤緑青以外を抹消
rimgnp[:, :, 2] = 0
gimgnp[:, :, 0] = 0
gimgnp[:, :, 2] = 0
bimgnp[:, :, 0] = 0
bimgnp[:, :, 1] = 0
rimg = Image.fromarray(rimgnp)
gimg = Image.fromarray(gimgnp)
bimg = Image.fromarray(bimgnp)
print("課題1-2")
plt.imshow(rimg)
plt.show()
rimg.save("lena-red.png")
plt.imshow(gimg)
plt.show()
gimg.save("lena-green.png")
plt.imshow(bimg)
plt.show()
bimg.save("lena-blue.png")

himgnp = imgnp[0::2, 0::2] # 1-3
himg = Image.fromarray(himgnp) # 半減させた物を画像形式に
print("課題1-3")
plt.imshow(himg)
plt.show()
himg.save("lena-half.png")