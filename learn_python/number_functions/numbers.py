# x= 10
# y=5
# print("subtracting two numbers", x-y)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, **): ")

if operation == "+":
    print("Result:", x + y)

elif operation == "-":
    print("Result:", x - y)

elif operation == "*":
    print("Result:", x * y)

elif operation == "/":
    print("Result:", x / y)

elif operation == "**":
    print("Result:", x ** y)

else:
    print("Invalid operation")