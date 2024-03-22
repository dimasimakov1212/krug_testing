import csv
import os
import datetime
import locale


# Устанавливаем русскую локаль
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

# путь к файлу с исходными данными
# file_start_csv = os.path.abspath(f'./786442_Ribbon1.csv')
file_start_csv = os.path.abspath(f'./786442_Ribbon1_test.csv')

# путь к файлу с исходными данными
file_finish_csv = os.path.abspath(f'./786442_Ribbon2.csv')


def reading_csv(data_file):
    """ Чтение файла с данными в формате csv"""

    # формируем исходный список
    list_start = []

    with open(data_file, 'r', encoding='windows-1251') as file:
        datas = csv.reader(file, delimiter=';')
        for line in datas:
            list_start.append(line)

    return list_start


def reformat_date_new(date_data):
    """
    Преобразует входящую дату в объект datetime
    """

    # убираем лишние символы
    date_data = date_data.replace(' г.', '').replace(' мсек', '')

    # преобразуем дату
    new_date_data = datetime.datetime.strptime(date_data, '%d %B %Y %H:%M:%S.%f')

    return new_date_data


def preparing_data(list_data):
    """
    Подготавливает данные для обработки
    """
    title_list = list_data[0]

    # формируем новый список
    new_list = []

    # меняем дату на объект datetime и складываем в новый список
    for number in range(1, len(list_data)):

        single_list = list_data[number]  # получаем элемент списка (список)
        date_data = single_list[1]  # получаем дату
        new_date_data = reformat_date_new(date_data)  # преобразуем дату
        single_list[1] = new_date_data  # заменяем дату
        new_list.append(single_list)  # добавляем в новый список

    # сортируем срисок, чтобы операции шли по порядку
    sorted_list = sorted(new_list, key=lambda x: x[1])

    return sorted_list


if __name__ == '__main__':
    list_1 = reading_csv(file_start_csv)
    preparing_data(list_1)
