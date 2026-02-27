# def is_palindrome_number(num):

#     if num < 0:
#         return False
    
#     original_num = num
#     reversed_num = 0
    
  
#     while num > 0:
#         remainder = num % 10
#         reversed_num = (reversed_num * 10) + remainder
#         num = num // 10
    
  
#     return original_num == reversed_num


# n = int(input("enter any positive number: "))
# if is_palindrome_number(n):
#     print(f"{n} is the palindrome number")
# else:
#     print(f"{n} is not a palindrome number")

def is_palindrome(num):
    if num < 0:
       return False
    
    orignal_num = num
    reverse_num = 0

    while num > 0:
        reminder =  num % 10
        reverse_num = (reverse_num * 10) + reminder
        num =  num // 10

    return orignal_num == reverse_num


user_input =  int(input("enter any number : "))
if is_palindrome(user_input):
    print(f"{user_input} is palindrome")
else:
    print(f"{user_input} is not palindrome")