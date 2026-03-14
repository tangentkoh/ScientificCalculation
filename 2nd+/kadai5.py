# kadai5.py(追加)
# バージョンは 3.11.9
import math

def multMyFloat(r1, r2):
    sig1, coe1, idx1 = r1
    sig2, coe2, idx2 = r2
    coef1 = str(coe1)
    coeff1 = int(coef1, 2)
    coef2 = str(coe2)
    coeff2 = int(coef2, 2)
    sig = sig1 * sig2 # 符号
    idx = idx1 + idx2 # 指数
    M = (1 << 24) # 同じように1を仮定
    M1 = M + coeff1
    M2 = M + coeff2
    Mp = M1 * M2 # 乗算
    Mpr = Mp >> 24
    if Mpr >= (M << 1):
        Mpr >>= 1
        idx += 1
    while Mpr < M: # 桁の調整
        Mpr <<= 1
        idx -= 1
    coeff = Mpr - M # 切り捨て
    return [sig, coeff, idx]

r1 = [1, 111101000000000000000011, 9]
r2 = [1, 111011011101001011110001, 6]
res = multMyFloat(r1, r2)
print(f"[{res[0]}, {res[1]:b}, {res[2]}]") # 出力