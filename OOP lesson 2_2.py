import os

"""Создаём функцию, которая будет заносить 3 файла в 1 при этом будет принимать на вход папку"""


def create_file(folder):
    file_lst = os.listdir(folder)  # считываем название файлов в папке
    merged_file_lst = []  # создаём список для добавления в неге содержимое файлов
    for file in file_lst:  # проходимся по списку содержимых файлов
        with open(folder + '/' + file, encoding='utf-8-sig') as file_in_temp:  # считываем файлы поочерёдно
            # Ниже добавляем в список 1) Название файла.file 2) Кол-во строк.(0) 3) Содержимое.[]
            merged_file_lst.append([file, 0, []])
            for lines in file_in_temp:  # построчно проходимся по файлам
                merged_file_lst[-1][2].append(lines.strip())  # добавляем построчно информацию
                merged_file_lst[-1][1] += 1  # с прохождением по каждой строке увеличиваем их кол-во для подсчёта
    return sorted(merged_file_lst, key=lambda x: x[1], reverse=False)  # возвращаем полученный файл,
    # при этом, используем ключ и лямбда функцию для сортировки


"""Создаём функцию, которая будет записывать итоговый файл, при этом она принимает на вход папку и имя файла"""


def create_merge_file(folder, the_final_file):
    with open(the_final_file + '.txt', 'w+', encoding='utf-8-sig') as merged_file:  # создаём результирующий файл с именем the_final_file
        merged_file.write(f'Даны файлы:\n')  # Добавляем строку в файл
        for write_3_files in create_file(
                folder):  # используя первую функцию мы занесём все значения в результирующий файл
            merged_file.write(f'Название файла: {write_3_files[0]}\n')  # Записываем название файла
            merged_file.write(f'Количество строк: {write_3_files[1]}\n')  # Записываем количество строк в type int
            for str_ in write_3_files[2]:  # Проходимся по файлу и по 2 индексу заносим информацию
                merged_file.write(str_ + '\n')  # Записываем эту информацию в файл
            merged_file.write('\n')  # Каждый раз делаем перенос строки, чтобы информация не было однострочной
    return print('Файл успешно создан')  # Возвращаем положительный результат файл успешно создан


create_merge_file('txt_docx', 'the_final_file')