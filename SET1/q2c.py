# Find the maximum frequency
max_frequency = max(char_frequency.values())

# Get all characters with the highest frequency
most_frequent_chars = [char for char, freq in char_frequency.items() if freq == max_frequency]

print("Most Frequent Character(s):", most_frequent_chars)
