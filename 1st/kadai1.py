# kadai1.py
# バージョンは 3.11.9

x = [0, 1, 2, 3, 4, 5, 6] # 1-1
print("課題1-1")
print(x[2])

y = x.copy() # 1-2
y.reverse()
print("課題1-2")
print(y)

z = x[1:6:2] # 1-3
print("課題1-3")
print(z)

x = 10 # 1-4
print("課題1-4")
if (x > 0):
  print('x is positive')