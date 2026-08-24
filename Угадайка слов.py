import random

word_list = [
    "Проститутка",
    "Велосипед",
    "Гномики",
    "Угадайка",
    "Пожалуйста",
    "Кокшага",
    "Волжский",
    "Бабушка",
]
flag_1 = True


def get_word(slovo):
    word = random.choice(slovo)
    word = word.upper()
    return word


def is_valid(a):
    if a.isalpha():
        return flag_1 == True
    else:
        return flag_1 == False


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\_
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |    _/ \\
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def play(word_1):
    word_1 = get_word(word_list)
    word_1 = word_1.upper()
    word_completion = "_" * len(
        word_1
    )  # строка, содержащая символы _ на каждую букву задуманного слова
    word_2 = []
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 8  # количество попыток
    flag = True

    print(display_hangman(tries))
    print("Загаданное  слово:   ", word_completion)
    word_3 = list(word_1)
    word_2.extend(word_3)
    word_4 = list(word_completion)
    if otvet_flag == True:
        word_4[0] = word_2[0]
        word_4[len(word_4) - 1] = word_2[len(word_2) - 1]
        print("Загаданное слово с первой и последней буквой: ", *word_4)

    while flag:
        while flag_1:
            moe_slovo = input("Введите букву или слово: ")
            moe_slovo = moe_slovo.upper()
            if is_valid(moe_slovo) == False:
                print("А может быть все-таки введем правильно ?")
                continue
            else:
                break
        if moe_slovo in guessed_letters or moe_slovo in guessed_words:
            print("Слово или буква уже названа")
        else:
            if len(moe_slovo) > 1:
                guessed_words.append(moe_slovo)
            else:
                guessed_letters.append(moe_slovo)
        if moe_slovo in word_1 and len(moe_slovo) == 1:

            for i in range(len(word_2)):
                if word_3[i] == moe_slovo:
                    word_4[i] = word_3[i]
            print("Загаданное слово", *word_4)

        elif (
            (len(moe_slovo) >= 1 and moe_slovo not in word_1)
            or (len(moe_slovo) > 1 and len(moe_slovo) != len(word_1))
            or (len(moe_slovo) == len(word_1) and moe_slovo not in word_1)
        ):
            tries -= 1
            print(display_hangman(tries))
        new_slovo = "".join(word_4)
        if moe_slovo in word_1 and len(moe_slovo) == len(word_1) or new_slovo == word_1:
            print("Поздравляем, вы угадали слово! Вы победили!")
            exit()
        if (tries == 0 and otvet_1_flag == False) and word_1 not in guessed_words:
            print("Вы проиграли.")
            print(f"Загаданное слово - {word_1}")
            exit()
        if (tries == 2 and otvet_1_flag == True) and word_1 not in guessed_words:
            print("Вы проиграли.")
            print(f"Загаданное слово - {word_1}")
            exit()


print("Давайте играть в угадайку слов!")
print("Можно отображать первую и последнюю букву слова Да / Нет")
otvet = input()
if otvet == "да":

    otvet_flag = True
else:
    otvet_flag = False
print("Шесть или восемь попыток?")
otvet_1 = input()

if otvet_1.lower() == "да" or otvet == "6":
    otvet_1_flag = True
    get_word(word_list)
    play(word_list)
else:
    otvet_1_flag = False

    get_word(word_list)

    play(word_list)
