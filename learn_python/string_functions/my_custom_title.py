def my_custom_title(text):
    if not text:
        return ""

    text = text.lower()

    words = text.split(" ")

    title_words = []

    for word in words:
        if word:

            new_word = word[0].upper() + word[1:]
            title_words.append(new_word)
        else:
            title_words.append("")

    return " ".join(title_words)

user_input =  str(input("enter the string: "))
print(f"Orignal: {user_input}")
print(f"Custom title: {my_custom_title(user_input)}")

