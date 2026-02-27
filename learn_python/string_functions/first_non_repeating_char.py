def first_non_repeating_char(text):

    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    for char in text:
        if char_count[char] == 1:
           return char

    return None

input_str = str(input("Input the string : "))
result = first_non_repeating_char(input_str)

if result:
    print(f"The first non-repeating charcters are :'{result}'")
else:
    print("all characters are repeating")
