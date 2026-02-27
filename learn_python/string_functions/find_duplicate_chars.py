def find_duplicate(text):

    char_count = {}
    duplicates = []

    for char in text:
        if char == " ":
            continue
        char_count[char] = char_count.get(char, 0) + 1

    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        if count > 1:
            duplicates.append(f"{char} ({count} times)")

    return duplicates


user_Input = str(input("enter the string to find the duplicated : "))
result = find_duplicate(user_Input)

if result:
    print(f"duplicate characters are :")
    for item in result:
        print(item)
else:
    print("No duplicate characters are find")
