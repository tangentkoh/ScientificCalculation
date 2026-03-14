# kadai4.py(追加)
# バージョンは 3.11.9
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("Lenna.png") # 4-1
imgnp = np.array(img)
print("課題4-1")
for i in range(0, 8):
    bitimgnp = imgnp.copy() # シフトして戻す
    bitimgnp[:, :, 0] = bitimgnp[:, :, 0] >> i
    bitimgnp[:, :, 1] = bitimgnp[:, :, 1] >> i
    bitimgnp[:, :, 2] = bitimgnp[:, :, 2] >> i
    bitimgnp[:, :, 0] = bitimgnp[:, :, 0] << i
    bitimgnp[:, :, 1] = bitimgnp[:, :, 1] << i
    bitimgnp[:, :, 2] = bitimgnp[:, :, 2] << i
    plt.imshow(bitimgnp)
    plt.show() # この課題は出力まで