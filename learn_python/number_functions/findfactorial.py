# import math

# def FirstFactorial(num):
#     if not isinstance(num, int) or num < 0:
#         raise ValueError("Input must be non-negative integer")
#     return math.factorial(num)

# try:
#     user_input = int(input("pls enter a non-negative integer to find factorial: "))
#     print(FirstFactorial(user_input))
# except ValueError as e:
#     print(e)
def find_factorial_recursive(n):
    # Base Case: ਜੇਕਰ ਨੰਬਰ 0 ਜਾਂ 1 ਹੈ, ਤਾਂ ਫੈਕਟੋਰੀਅਲ 1 ਹੁੰਦਾ ਹੈ
    if n == 0 or n == 1:
        return 1
    # Recursive Case: n * (n-1 ਦਾ ਫੈਕਟੋਰੀਅਲ)
    else:
        return n * find_factorial_recursive(n - 1)

# ਟੈਸਟ ਕਰੋ
num = int(input("enter the number to find the factorial: "))
print(f"factorial of {num} is: {find_factorial_recursive(num)}")