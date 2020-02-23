'''programs of operators'''
#arithmetic operators are used with numeric values to perform common mathematical operations#
#addition#
a = 6
b = 3

print(a + b)
#subtraction#
a = 6
b = 3

print(a - b)

#multiplication#
a = 6
b = 3

print(a * b)
#division#
a = 6
b = 3

print(a / b)
#modulus#
a = 6
b = 3

print(a % b)
#Exponentiation#
a = 6
b = 3

print(a ** b)
#Floor division#
a = 6
b = 3

print(a //b)


#Assignment operators are used to assign values to variables#
z = 6
print(z)
k= z + 2
print(k)
y = z - 2
print(y)

a = z * 2
print(a)
x = z / 2
print(x)
c = z % 2
print(c)
e = z // 2
print(e)
d = z ** 2
print(d)
f = z & 2
print(f)
g = z | 2
print(g)
h = z ^ 2
print(h)
i = z >> 2
print(i)
j = z << 2
print(j)
#Comparison operators are used to compare two values#
#equal==#
x = 4
y = 2

print(x == y)
#Not equal!=#
x = 4
y = 2

print(x != y)
#Greater than#
x = 4
y = 2

print(x > y)
#Less than#
x = 4
y = 2

print(x < y)
#Greater than or equal to#
x = 4
y = 2

print(x >= y)
#Less than or equal to#
x = 4
y = 2

print(x <= y)
#ogical operators are used to combine conditional statements#
#and 	Returns True if both statements are true#
x = 6

print(x > 2 and x < 10)
#or	Returns True if one of the statements is true#
x = 6

print(x > 2 or x < 4)
#not	Reverse the result, returns False if the result is true	#

x = 6

print(not(x > 2 and x < 10))
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
#
#is 	Returns true if both variables are the same object#
x = ["orange", "pineapple"]
y = ["orange", "pineapple"]
z = x

print(x is z)
print(x is y)
print(x == y)
#is not	Returns true if both variables are not the same object	#
x = ["orange", "pineapple"]
y = ["orange", "pineapple"]
z = x
print(x is not z)
print(x is not y)
print(x != y)
#Membership operators are used to test if a sequence is presented in an object#
#in 	Returns True if a sequence with the specified value is present in the object#
x = ["orange", "pineapple"]
print("orange" in x)
#not in	Returns True if a sequence with the specified value is not present in the object#
x = ["orange", "pineapple"]
print("banana" not in x)
#Bitwise operators are used to compare (binary) numbers#
#& 	AND	Sets each bit to 1 if both bits are 1#
#~ 	NOT	Inverts all the bits#
#<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off#
#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off#























