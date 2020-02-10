a,b,c = 3, 7, 11
a,c = a + b, a
b = a - b
a,c = a - b, b
print(a,b,c)
while c < a*b:
    c = 2*c + 1
print('c =', c)
