# Initialize a dictionary to store frequencies
char_frequency = {}

# Count frequencies of each character
for char in sentence:
    if char != " ":  # Ignore spaces
        char_frequency[char] = char_frequency.get(char, 0) + 1

print("Character Frequencies:", char_frequency)
