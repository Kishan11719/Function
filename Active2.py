def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return  x*y

def divides(x,y):
    return  x/y

num1 = int(input("Enter Number1"))
num2 = int(input("Enter Number2"))

print("Sum :", add(num1, num2))
print("Difference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotient :", divides(num1, num2))