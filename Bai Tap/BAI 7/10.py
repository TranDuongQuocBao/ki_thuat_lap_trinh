def longest_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]

    return longest

print("Những từ dài nhất:", longest_words("a.txt"))
