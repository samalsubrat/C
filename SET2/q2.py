def reverse_words(sentence):
    """Reverse the words in a sentence."""
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def count_word_occurrences(paragraph):
    """Count the occurrences of each word in a paragraph."""
    word_count = {}
    words = paragraph.split()
    for word in words:
        word = word.lower().strip(".,!?")  # Normalize words
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def replace_word(paragraph, old_word, new_word):
    """Replace all occurrences of a specific word in a paragraph."""
    return paragraph.replace(old_word, new_word)

def menu():
    """Menu-driven application."""
    while True:
        print("\nMenu:")
        print("1. Reverse the words in a sentence")
        print("2. Count occurrences of each word in a paragraph")
        print("3. Find and replace all occurrences of a specific word in a paragraph")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            sentence = input("Enter a sentence: ")
            print("Reversed Sentence:", reverse_words(sentence))
        elif choice == "2":
            paragraph = input("Enter a paragraph: ")
            word_count = count_word_occurrences(paragraph)
            print("Word Count:", word_count)
        elif choice == "3":
            paragraph = input("Enter a paragraph: ")
            old_word = input("Enter the word to replace: ")
            new_word = input("Enter the new word: ")
            print("Modified Paragraph:", replace_word(paragraph, old_word, new_word))
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
