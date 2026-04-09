def replace_word(text, old_word, new_word):
    if old_word not in text:
        return "Слово не найдено!"
    return text.replace(old_word, new_word)

while True:
    text = input("Введите текст: ")
    old_word = input("Какое слово заменить: ")
    new_word = input("На какое слово заменить: ")

    print("Результат:", replace_word(text, old_word, new_word))

    again = input("Еще раз? (да/нет): ")
    if again.lower() != "да":
        break
