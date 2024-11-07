"""
Word Occurrences
Estimate: 25 minutes
Actual:   13 minutes
"""

def main():
    string_input = input("Text: ")
    words = string_input.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_length = max(len(word) for word in word_count)
    sorted_words = sorted(word_count)

    for word in sorted_words:
        print(f"{word:{max_length}} : {word_count[word]}")


main()