import math
c1 = float(input('Digite cateto oposto:'))
c2 = float(input('Digite cateto adjacente:'))
r = (c1**2 + c2**2)
h = math.sqrt(r)
print(f'{h:.2f}')