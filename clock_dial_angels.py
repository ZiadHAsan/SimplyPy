H, M = map(int, input().split())
h1 = H * 300 + M*5
m1 = M * 60
a1 = abs((h1 - m1)/10)
a2 = 360 - a1
if (a1 > a2):
    a = a2
else: 
    a = a1
print(a)