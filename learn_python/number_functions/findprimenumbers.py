def findprimeNumbers(num):

    if not isinstance(num, int) or num <= 2 or num >= 100:
        raise ValueError("Input must be an integer and between 2 and 100")

    prime_numbers = []

    for n in range(2, num + 1):
        is_prime = True

        for divisor in range(2, int(n**0.5) + 1):
            if n % divisor == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(n)

    return prime_numbers


try:
    user_Input = int(input("Please enter the number between 2 to 100 : "))
    result = findprimeNumbers(user_Input)
    print(f"Prime Numbers : {result}")
except ValueError as e:
    print(e)


# def findprimeNumbers2(num):  
#     # 1. ਪਹਿਲਾਂ ਸ਼ਰਤਾਂ ਚੈੱਕ ਕਰੋ
#     if not isinstance(num, int) or num <= 2 or num >= 100:
#         raise ValueError("Input must be an integer and between 2 and 100") 
    
#     prime_numbers = []

#     # 2. ਬਾਹਰਲਾ ਲੂਪ: 2 ਤੋਂ ਲੈ ਕੇ num ਤੱਕ ਹਰ ਨੰਬਰ ਲਈ
#     for n in range(2, num + 1):
#         is_prime = True
        
#         # 3. ਅੰਦਰੂਨੀ ਲੂਪ: ਚੈੱਕ ਕਰੋ ਕਿ ਕੀ n ਕਿਸੇ ਹੋਰ ਨਾਲ ਭਾਗ ਹੁੰਦਾ ਹੈ
#         for divisor in range(2, int(n**0.5) + 1):
#             if n % divisor == 0: # n ਨੂੰ divisor ਨਾਲ ਭਾਗ ਕਰੋ
#                 is_prime = False
#                 break
        
#         # 4. ਜੇ ਪ੍ਰਾਈਮ ਹੈ ਤਾਂ ਲਿਸਟ ਵਿੱਚ ਪਾਓ (ਇਹ ਅੰਦਰੂਨੀ ਲੂਪ ਤੋਂ ਬਾਹਰ ਹੈ)
#         if is_prime:
#             prime_numbers.append(n)

#     # 5. ਸਾਰੇ ਨੰਬਰ ਚੈੱਕ ਕਰਨ ਤੋਂ ਬਾਅਦ ਲਿਸਟ ਵਾਪਸ ਕਰੋ
#     return prime_numbers

# # 6. ਇਨਪੁਟ ਅਤੇ ਕਾਲ (ਫੰਕਸ਼ਨ ਤੋਂ ਬਾਹਰ)
# try:
#     user_Input = int(input("Please enter the number between 2 to 100: "))
#     result = findprimeNumbers2(user_Input)
#     print(f"Prime Numbers : {result}")
# except ValueError as e:
#     print(e)