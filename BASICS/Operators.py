"""Arthmetic operators in Python"""
a = 5
b = 10

print("Sum: ",a + b)
print("Difference: ",a - b)
print("Product: ",a * b)
print("Division: ",a / b)
print("Modulus: ",a % b)
print("Exponent: ",a ** b) # a^b

"""Relational operators in Python"""

print("Equal: ",a == b) #False
print("Not equal: ",a != b) #True
print("Greater than: ",a > b) #Flase
print("Less than: ",a < b) #False
print("Greater than or equal to: ",a >= b) #False
print("Less than or equal to: ",a <= b) #True
 
"""Assignment operator in Python"""

num = 10
num = num + 10
num *= 10 
num -= 10
num /= 10
num %= 10
num **= 10
print("num: ", num)

"""Logical operator of Python"""

print (not True)
print (not False)
print (not(a > b))

val1 = True
val2 = False
print(f"AND operator: {val1 and val2}")
print(f"OR operator: {val1 or val2}")
print("expression",(a==b) or (a < b))