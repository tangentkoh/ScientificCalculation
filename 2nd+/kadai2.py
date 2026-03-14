# kadai2.py(追加)
# バージョンは 3.11.9
import math

def myFloat(r):
    sig = r[0] # 符号
    rfo = r[2] * 0.0001 # 小数に戻す
    rit = bin(r[1])[2:]
    rft = ''
    while rfo != 0 and len(rft) < 28:
        rfo *= 2
        if rfo >= 1:
            rft += '1'
            rfo -= 1
        else:
            rft += '0'
    t = rit + '.' + rft # 再構築
    tn = t.replace('.', '')
    f = tn.find('1')
    coeff = int(tn[f + 1 : f + 25])
    di = t.find('.')
    fdi = t.find('1')
    idx = di - fdi - 1
    if(idx < 0): # 負の値の場合調整
        idx += 1
    return [sig, coeff, idx]

r = [1, 0, 1000] # rを分解(0.1)
print(myFloat(r))
r2 = [1, 1000, 1] # rを分解(1000.0001)
print(myFloat(r2))
r3 = [1, 123, 4560] # rを分解(123.456)
print(myFloat(r3))