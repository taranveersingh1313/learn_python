from collections import Counter

# Example list
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Count frequency
frequency = Counter(items)

print(frequency)


numbers = [1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]

freq_dict = {}

for num in numbers:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

                            
print(freq_dict)
