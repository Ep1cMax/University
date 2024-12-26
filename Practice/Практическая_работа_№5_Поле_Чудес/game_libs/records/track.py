def track_record(record: int = 0) -> None:
    """
    Ведет запись рекордов в файл records.txt
    :param record: последний рекорд, добавляемый в файл
    :return:
    """
    file = open('game_libs\\records.txt', 'r+')
    old_recs = list(map(lambda x: int(x), file.read().replace('\n', ' ').split()))
    if len(old_recs) == 0:
        file.write(str(record))
    else:
        file.seek(0)
        while True:
            if record >= old_recs[0]:
                print('New record!')
                old_recs.append(record)
                old_recs.sort(reverse=True)
                for i in old_recs:
                    file.write(str(i) + '\n')
                break
            else:
                old_recs.append(record)
                old_recs.sort(reverse=True)
                for i in old_recs:
                    file.write(str(i) + '\n')
                break