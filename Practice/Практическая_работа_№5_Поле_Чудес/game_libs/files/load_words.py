from random import randint


def load_word(directory: str = "game_libs\\words.txt") -> list:
    """
    Загружает случайное слово из текстового файла, указанного в directory
    :param directory: полный путь до текстового файла со словами
    :return: случайное слово
    """
    while True:
        try:
            file = open(directory, 'r')
            break
        except (FileNotFoundError, OSError):
            print('Wrong path to the word`s file! Input the path or enter quit to exit the game...')
            directory = input()
            if directory == 'quit':
                exit()
        except PermissionError:
            print('Do not have authorisation to read this file! Input the path or enter quit to exit the game... ')
            directory = input()
            if directory == 'quit':
                exit()
    file = open(directory, 'r')
    words = []
    for i in file.readlines():
        if '\n' in i:
            i = i.replace('\n', '')
        words.append(i)
    return words[randint(0, len(words) - 1)]
