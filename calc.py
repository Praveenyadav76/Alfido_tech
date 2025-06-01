def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error! any number divided by 0 is undefined"
    else:
        return a / b

print("select your operation :-")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")

choice = input("enter choice (1/2/3/4): ")
num1 = float(input("enter your first number :-"))
num2 = float(input("enter your second number :-"))

if choice == "1":
    print("result:-", add(num1, num2))
elif choice == "2":
    print("result:-", subtract(num1, num2))
elif choice == "3":
    print("result:-", multiply(num1, num2))
elif choice == "4":
    print("result:-", divide(num1, num2))
else:
    print("invalid input")