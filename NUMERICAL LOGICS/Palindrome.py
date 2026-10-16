n =int(input("Enter the number: "))
num = n
result = 0
if n < 0:
    print("True")
else:
    while num > 0:
        ld = num % 10
        result = (result * 10) + ld
        num = num // 10
    if result == n:
        print("True")
    else:
        print("False")