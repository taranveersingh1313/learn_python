# def find_second_largest(numbers):
#     # Initialize first and second largest to the smallest possible value
#     first = float('-inf')
#     second = float('-inf')

#     for num in numbers:
#         # If current number is greater than the first largest
#         if num > first:
#             second = first
#             first = num
#         # If current number is between first and second largest
#         elif num > second and num != first:
#             second = num

#     return second

# # Taking input from the user
# try:
#     user_input = input("Enter numbers separated by space: ")
#     # Convert the input string into a list of integers
#     num_list = [int(x) for x in user_input.split()]

#     if len(num_list) < 2:
#         print("Error: Please enter at least two different numbers.")
#     else:
#         result = find_second_largest(num_list)

#         if result == float('-inf'):
#             print("There is no second largest number (all numbers might be the same).")
#         else:
#             print("The second largest number is:", result)

# except ValueError:
#     print("Invalid input! Please enter only integers.")


def find_second_largest(num):
    # Initialize with negative infinity
    first = second = float("-inf")

    for i in num:
        if i > first:
            # Current first becomes second, and i becomes new first
            second = first
            first = i
        # Fixed the condition: check if i is greater than second AND not equal to first
        elif i > second and i != first:
            second = i

    # IMPORTANT: Return must be outside the for loop
    return second


try:
    user_input = input("Enter numbers separated by spaces: ")
    # Converting input string to a list of integers
    num_list = [int(x) for x in user_input.split()]

    if len(num_list) < 2:
        print("Error: Please enter at least two different numbers.")
    else:
        result = find_second_largest(num_list)

        if result == float("-inf"):
            print("There is no second largest number (all values might be the same).")
        else:
            print("The second largest number is:", result)

except ValueError:
    print("Invalid Input! Please enter numbers only.")