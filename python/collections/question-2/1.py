def main(words):
    result = {}
    for word in words:
        word = word.strip() if word and isinstance(word, str) else ""
        first_ch = word[0].lower() if word else ""
        if not first_ch:
            continue

        if first_ch not in result:
            result[first_ch] = []

        result[first_ch].append(word)

    return result

if __name__ == "__main__":
    words = ["apple", "ant", "Apple", "banana", "ball", "cat"]
    result = main(words)
    print(result)

