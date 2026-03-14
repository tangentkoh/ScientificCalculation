# PCA.py (バージョンは3.11.9想定)
from PIL import Image
import numpy as np
import glob
import matplotlib.pyplot as plt

# 画像保存用関数
# 固有ベクトル画像の保存にはこれを使うと良い
def save_image(array,width,height,filename):
    min = np.amin(array)
    max = np.amax(array)
    array = (array - min) / (max - min) * 255
    Image.fromarray(array.reshape([height,width,3]).astype(np.uint8)).save(filename)
## 画像保存終わり

## ここからプログラム本体

# 実行ディレクトリ中に people ディレクトリがあることを想定（配布した雛形の構成に沿っている）
# 変更する場合は適当に書き換えること
# single を読み込む場合は，people を single に変更
files = glob.glob("./single/*.bmp")
char = "s"

# 縦幅，横幅，画像枚数を取得
# num : 画像枚数
num = len(files)

imtest = Image.open(files[0])
# width : 横，height : 縦
width = imtest.width
height = imtest.height

# 画像読み込み部分，1枚ずつ読み込んだ後に列ベクトルを横に並べた形式に変形
# im = [x1, x2, x3, ...]
# x : 画像の輝度を列ベクトルとして並べたもの
# im は num 行， width * height 列の行列となる．
im = []
for f in files:
    im.append(np.array(Image.open(f),np.float64))
im = np.array(im).reshape([num,width*height*3]).transpose()

# サンプルとして平均画像を計算するプログラムを示す(回答の一つ)
# ここではすべての要素が1/numであるベクトルを作成し
# そのベクトルと読み込んだデータの積を計算することで平均を計算している
one = np.ones([num,1])/num
ave = im @ one
save_image(ave,width,height,f"average{char}.png")

## ここから固有ベクトルの計算プログラムを記述する
## 計算された固有ベクトルについては上記のsave_imageを使って保存するとよい
## width, height は変化しないので，eigen1に計算された固有ベクトルが格納されている場合は
## 例えば以下のように呼び出す
## save_image(eigen1, width,height,"eigen1.png")
Bdash = im - ave
S = (Bdash.T @ Bdash) / num # 分散共分散行列
l,w = np.linalg.eig(S)
y = np.argsort(l)[::-1] # 固有値順に
l = l[y]
w = w[:, y]
w2 = Bdash @ w
lsum = np.sum(l)
for i in range(3):
    ki = l[i] / lsum
    eigen1 = w2[:, i]
    fn = f"eigen{i+1}{char}.png"
    save_image(eigen1, width, height, fn)
    print(f"{fn}を作成しました")
cbr = l / lsum
plt.figure(figsize=(7, 4))
plt.plot(range(1, len(cbr) + 1), cbr, marker='o', linestyle='-')
plt.savefig(f"kiyo{char}.png")
print(f"kiyo{char}.pngを作成しました")
plt.close()
