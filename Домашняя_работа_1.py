import math

a = int(input())
b = int(input())
alf = int(input())
alf = alf * math.pi / 180
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(alf))

print (c)