
def consonantsandvowelcount(text):
    vowels = 'aeiou'
    v_count = 0
    c_count = 0
    text =  text.lower()

    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count         

user_input =  input("please enter any string :")

v, c  = consonantsandvowelcount(user_input)

print(f"vowel count is: {v}")
print(f"consonant count is: {c}")