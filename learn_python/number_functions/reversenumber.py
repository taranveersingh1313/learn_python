def reverseNumbrt(num):
    if not isinstance(num, int):
       raise ValueError("Please enter only integer value")

    sign = -1 if num < 0 else 1
    
    num = abs(num)

    reverse_num = 0

    while num > 0:

            reminder = num % 10

            reverse_num = (reverse_num * 10) + reminder

            num = num // 10

    return reverse_num * sign

try:
    user_Input = int(input("Please enter any number : "))
    result = reverseNumbrt(user_Input)
    print(result)
except ValueError as e:
    print(e)
