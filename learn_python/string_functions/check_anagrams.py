def check_anagrams(str1, str2):

    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

string1 = str(input("Enter first string :"))
string2 = str(input("Enter second string :"))

if check_anagrams(string1, string2):
    print("yes! these strings an anagrams")
else:
    print("No! these strings are not an anagrams")