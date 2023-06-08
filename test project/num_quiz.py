from numbers import Number
from decimal import Decimal
from fractions import Fraction

print(isinstance(2.0, Number))
print(isinstance(Decimal('2.0'), Number))
print(isinstance(Fraction(2, 1), Number))
print(isinstance("2", Number))

print(0b101)  # - binary
print(0o10)  # - octal
print(0x1F)  # - hexadecimal

z = complex(1.25)
print(z)


print(round(100.2563, 3))
print(round(100.000056, 3))

print( (1.1 + 2.2) == 3.3 )

import math
print(math.ceil(252.4))
print(math.floor(252.4))

print(int(2.999))

x = -5j
print(type(x))

print(abs(-45.300))
