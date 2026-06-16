def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

num1 = float(input("Enter dividend: "))
num2 = float(input("Enter divisor: "))

print("Division =", divide(num1, num2))