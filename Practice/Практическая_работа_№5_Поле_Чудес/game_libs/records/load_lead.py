def load_leading_record():
    """
    Загружает высший рекорд из файла records.txt
    :return:
    """
    file = open('game_libs\\records.txt', 'r')
    top = file.readline()
    if top != '':
        print('Top record:', top)