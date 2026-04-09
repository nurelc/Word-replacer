def replace_words(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

if __name__ == "__main__":
    sample_text = input("Введите текст: ")
    old_word = input("Слово, которое нужно заменить: ")
    new_word = input("Слово на которое заменить: ")
    replacements = {old_word: new_word}
    print("Результат:", replace_words(sample_text, replacements))
