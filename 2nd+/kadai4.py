# kadai4.py(追加)
# バージョンは 3.11.9
import math

def addMyFloat(r1, r2):
    sig1, coe1, idx1 = r1
    sig2, coe2, idx2 = r2
    coef1 = str(coe1)
    coeff1 = int(coef1, 2)
    coef2 = str(coe2)
    coeff2 = int(coef2, 2)
    M = (1 << 24) # １を仮定
    M1 = M + coeff1
    M2 = M + coeff2
    M1s = sig1 * M1
    M2s = sig2 * M2
    if idx1 < idx2: # 指数合わせ
        im = idx2
        d = idx2 - idx1
        s = M1s >> d
        Ms = s + M2s
    elif idx2 < idx1:
        im = idx1
        d = idx1 - idx2
        s = M2s >> d
        Ms = s + M1s
    else:
        im = idx1
        Ms = M1s + M2s
    sig = 1 if Ms > 0 else -1 # 符号
    Ma = abs(Ms)
    while Ma >= (M << 1):
        Ma >>= 1 # 右シフト
        im += 1
    while Ma < M and im > -128:
        Ma <<= 1 # 左シフト
        im -= 1
    coeff = Ma - M
    idx = im
    return [sig, coeff, idx] # 戻り値

r1 = [1, 111101000000000000000011, 9]
r2 = [1, 111011011101001011110000, 6]
res = addMyFloat(r1, r2)
print(f"[{res[0]}, {res[1]:b}, {res[2]}]") # 出力

# 情報落ちは、指数のアラインメントの際に発生
# 加算・減算において、指数の差が大きい場合、小さい指数を持つ数の仮数部は差分だけ右シフト
# この右シフトにより、元の仮数部の下位ビットが切り捨てられ、小さい数の情報が失われる
# 桁落ちは、符号が異なり、絶対値が非常に近い2つの数を減算した際に発生
# 上位の有効桁が相殺され、残った結果の有効桁数が大幅に減少、計算結果の相対誤差が増大
# これにより、結果の精度が著しく低下する