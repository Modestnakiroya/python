import math
print(math.sqrt(25)) # square root
print(math.factorial(5)) # factorial
print(math.ceil(5.4)) # ceiling
print(math.floor(5.4)) # floor
from math import pi, e # import pi and e from math module 

#swapping variables
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)
# using math 
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)
# using math
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, ", b =", b)
# using math
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping: a =", a, ", b =", b)

