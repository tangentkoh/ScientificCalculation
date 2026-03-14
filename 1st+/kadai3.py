# kadai3.py(追加)
# バージョンは 3.11.9
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img = Image.open("Lenna.png") # 3-1
imgnp = np.array(img)
rdata = imgnp[:, :, 0]
h, w = rdata.shape # rdataより取得
x = np.arange(0, w, 1)
y = np.arange(0, h, 1)
xx, yy = np.meshgrid(x, y)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(211, projection='3d')
ax.plot_surface(xx, yy, rdata, cmap='cool')
print("課題3-1")
plt.show() # この課題は出力まで