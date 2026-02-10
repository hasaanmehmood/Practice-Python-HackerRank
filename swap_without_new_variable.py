num1 = 10
num2 = 20

# num1, num2 = num2, num1             -- Simplest way to swap two variables

def foo(n1, n2):
    if n1 < n2:
        n2 = n1 + n2
        n1 = n2 - n1
        n2 = n2 - n1
    else:
        n1 = n2 + n1
        n2 = n1 - n2
        n1 = n1 - n2
    return n1, n2


num1, num2 = foo(num1, num2)

print("num1:", num1)
print("num2:", num2)