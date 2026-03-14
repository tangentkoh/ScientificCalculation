# kadai2.py(追加)
# バージョンは 3.11.9
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Lenna.png") # 2-1
imgnp = np.array(img)
imgsum = 0
for x in range(0, 256): # 平均値を求める
    for y in range(0, 256):
        imgsum += np.double(imgnp[x, y, 0])
        imgsum += np.double(imgnp[x, y, 1])
        imgsum += np.double(imgnp[x, y, 2])
imgave = imgsum / (256 * 256 * 3)
imgsum2 = 0
for x in range(0, 256): # 分散を求める
    for y in range(0, 256):
        imgsum2 += (np.double(imgnp[x, y, 0]) - imgave) ** 2
        imgsum2 += (np.double(imgnp[x, y, 1]) - imgave) ** 2
        imgsum2 += (np.double(imgnp[x, y, 2]) - imgave) ** 2
imgstd = imgsum2 / (256 * 256 * 3)
print("課題2-1")
print("計算による平均：" + str(imgave))
print("計算による分散：" + str(imgstd))
print("Numpyによる平均：" + str(np.mean(imgnp)))
print("Numpyによる分散：" + str(np.var(imgnp)))

nimgnp = imgnp.copy() # 2-2
nimgnp[:, :, :] = 255 - nimgnp[:, :, :]
nimg = Image.fromarray(nimgnp)
print("課題2-2")
plt.imshow(nimg)
plt.show()
nimg.save("lena-naga.png")