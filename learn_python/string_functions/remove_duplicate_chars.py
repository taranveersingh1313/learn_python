def remove_duplicate_chars(text):

    duplicates = ""

    for char in text:
        if char not in duplicates:
            duplicates += char
    return duplicates

user_input = str(input("enter the string to remove the duplicates :"))
result = remove_duplicate_chars(user_input)

if result:
    print(result)
else:
    print("no duplicate charcters in your string")
