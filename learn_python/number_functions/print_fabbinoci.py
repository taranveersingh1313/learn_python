def print_fabbinoci(num):
    t, j = 0, 1

    if num < 0:
        print("please enter the positive number")
    elif num == 0:
        print(t)
    else:
        print("fabiconi series :", end=" ")

    while t <= num:
        print(t, end=" ")
        t, j = j, t + j


try: 
    user_Input = int(input("you want to print fabbiconi series upto which number ? "))
    print_fabbinoci(user_Input)
except ValueError:
    print("Please enter valid integer")    