from game_libs.files import load_word
from game_libs.records import track_record
from game_libs.records import load_leading_record

lives = 0
breaker = 1
record = 0
load_leading_record()
while True:
    try:
        choice = int(input('Choose difficulty (1 - easy, 2 - normal, 3 - hard): '))
        if 0 < choice < 4:
            break
        else:
            print('Wrong difficulty chosen!')
    except ValueError:
        print('Wrong difficulty chosen!')
while True:
    if choice == 1:
        lives = 7
        print('Life value: ', '♥' * 7)
    elif choice == 2:
        lives = 5
        print('Life value: ', '♥' * 5)
    elif choice == 3:
        lives = 3
        print('Life value: ', '♥' * 3)
    if breaker:
        word = load_word()
        breaker = 0
    else:
        word = load_word()
    fin_word = '■'*len(word)
    print('Chosen word:', fin_word)
    while lives != 0:
        if fin_word == word:
            record += 1
            print(f'You guessed the word right! {word}\nYour current record: {record}')
            break
        print(''.join(fin_word), '|', '♥' * lives)
        while True:
            try:
                answer = input('Input character or the whole word: ')
                break
            except ValueError:
                print('Wrong character!')
        if len(answer) > 1:
            if answer == word:
                fin_word = word
            else:
                print('You entered... wrong word, yes?')
                lives -= 1
        elif len(answer) == 0 or answer.isdigit():
            print('Nothing was entered')
        else:
            if answer in word:
                for i in range(len(fin_word)):
                    if answer == word[i]:
                        fin_word = fin_word[:i] + answer + fin_word[i+1:]
                print('You`ve guessed the character right!')
            else:
                print('You haven`t guessed the character right!')
                lives -= 1
    if lives == 0:
        print(f'You`ve lost! Your record: {record}')
        track_record(record)
        break
    while True:
        choice_cont = input('Do you want to continue? (y/n): ')
        if choice_cont == 'y':
            break
        elif choice_cont == 'n':
            track_record(record)
            print(f'Your final record: {record}!')
            exit()
        else:
            print('Wrong value entered!')
