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
    """ Чтение файла с данными """

    # исходный список
    list_start = []

    with open(data_file, 'r', encoding='windows-1251') as file:
        datas = csv.reader(file, delimiter=';')
        for line in datas:
            list_start.append(line)

    return list_start


def reformat_date_new(date_data):
    date_data = date_data.replace(' г.', '').replace(' мсек', '')

    new_date_data = datetime.datetime.strptime(date_data, '%d %B %Y %H:%M:%S.%f')
    return new_date_data


def new_data(list_data):
    title_list = list_data[0]
    print(title_list)
    new_list = []
    print(len(list_data))

    for number in range(1, len(list_data)):
        single_list = list_data[number]
        date_data = single_list[1]
        new_date_data = reformat_date_new(date_data)
        single_list[1] = new_date_data
        new_list.append(single_list)

    print(new_list)


if __name__ == '__main__':
    list_1 = reading_csv(file_start_csv)
    new_data(list_1)
