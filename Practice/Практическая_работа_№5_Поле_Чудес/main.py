from game_libs.files import load_word
from game_libs.records import track_record
from game_libs.records import load_leading_record

lives = 0
breaker = 1
record = 0
load_leading_record()
while True:
    try:
        choice = int(input('Выберите уровень сложности (1-легкий, 2-нормальный, 3-сложный): '))
        if 0 < choice < 4:
            break
        else:
            print('Выбрана неправильная сложность!')
    except ValueError:
        print('Выбрана неправильная сложность!')
while True:
    if choice == 1:
        lives = 7
        print('Кол-во жизней: ', '♥' * 7)
    elif choice == 2:
        lives = 5
        print('Кол-во жизней: ', '♥' * 5)
    elif choice == 3:
        lives = 3
        print('Кол-во жизней: ', '♥' * 3)
    if breaker:
        word = load_word('this breaks the file loading :P input "game_libs\words.txt"')
        breaker = 0
    else:
        word = load_word()
    fin_word = '■'*len(word)
    print('Загаданное слово (на английском):', fin_word)
    while lives != 0:
        if fin_word == word:
            record += 1
            print(f'Вы отгадали слово! {word}\nВаш текущий рекорд: {record}')
            break
        print(''.join(fin_word), '|', '♥' * lives)
        while True:
            try:
                answer = input('Введите букву или слово полностью: ')
                break
            except ValueError:
                print('Введено неправильное значение')
        if len(answer) > 1:
            if answer == word:
                fin_word = word
            else:
                print('Вы ввели... неправильное слово!')
                lives -= 1
        elif len(answer) == 0 or answer.isdigit():
            print('Ничего не было введено')
        else:
            if answer in word:
                for i in range(len(fin_word)):
                    if answer == word[i]:
                        fin_word = fin_word[:i] + answer + fin_word[i+1:]
                print('Вы угадали букву!')
            else:
                print('Вы не угадали букву!')
                lives -= 1
    if lives == 0:
        print(f'Вы проиграли! Ваш рекорд: {record}')
        track_record(record)
        break
    while True:
        choice_cont = input('Желаете продолжить игру? (y/n): ')
        if choice_cont == 'y':
            break
        elif choice_cont == 'n':
            track_record(record)
            print(f'Ваш финальный рекорд: {record}. Ждём вас на следующей игре!')
            exit()
        else:
            print('Введено неправильное значение...')