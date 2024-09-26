import csv
import os
import datetime
import locale


# Устанавливаем русскую локаль
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')


def reading_csv(data_file):
    """ Чтение файла с данными в формате csv"""

    # формируем исходный список
    list_start = []

    with open(data_file, 'r', encoding='windows-1251') as file:
        datas = csv.reader(file, delimiter=';')
        for line in datas:
            list_start.append(line)

    return list_start


def writing_csv(data_file, input_data: list):
    """ Запись данных в файл в формате csv"""

    with open(data_file, 'w', newline='', encoding='windows-1251') as file:
        datas = csv.writer(file, delimiter=';')
        datas.writerows(input_data)


def reformat_date_new(date_data: str):
    """
    Преобразует входящую дату в объект datetime
    """

    # убираем лишние символы
    date_data = date_data.replace(' г.', '').replace(' мсек', '')

    # преобразуем дату
    new_date_data = datetime.datetime.strptime(date_data, '%d %B %Y %H:%M:%S.%f')

    return new_date_data


def checkin_data(list_data: list, time_start, time_finish, difference):
    """
    Проверка разницы данных между собой
    :param list_data: список данных для проверки
    :param time_start: начало временного интервала
    :param time_finish: окончание временного интервала
    :param difference: разница данных
    :return: список, подходящий по заданным параметрам
    """

    # формируем новый список
    new_list = [list_data[0]]  # добавляем заголовок

    data_number = len(list_data[0])  # количество элементов в одном списке

    # перебираем списки с данными
    for number in range(1, len(list_data)):

        if number == 1:
            datas_1 = list_data[len(list_data) - 1]  # получаем первый список данных для сравнения
            datas_2 = list_data[number]  # получаем второй список данных для сравнения
        else:
            datas_1 = list_data[number - 1]  # получаем первый список данных для сравнения
            datas_2 = list_data[number]  # получаем второй список данных для сравнения

        date_1 = reformat_date_new(datas_1[1])  # получаем дату первого списка данных
        date_2 = reformat_date_new(datas_2[1])  # получаем дату второго списка данных

        # проверяем условие, что даты списков данных идут друг за другом
        if date_2 > date_1:

            # проверяем попадает ли дата в заданный диапазон
            if time_start <= date_2 <= time_finish:

                # проверяем данные в первом и втором списке
                for item in range(2, data_number):

                    figure_1 = float(datas_1[item].replace(',', '.'))  # приводим к типу параметр 1
                    figure_2 = float(datas_2[item].replace(',', '.'))  # приводим к типу параметр 2

                    # если разница в данных превышает заданный параметр
                    if abs(figure_2 - figure_1) > difference:

                        new_list.append(datas_2)  # добавляем данные в новый список

                        break

    return new_list


def start_researching():
    """ Функция запуска расчета """

    # ----- задаем файлы для данных -----

    # путь к файлу с исходными данными
    file_start_csv = os.path.abspath(f'./786442_Ribbon1.csv')

    # путь к файлу с исходными данными
    file_finish_csv = os.path.abspath(f'./786442_Ribbon2.csv')

    # ----- задаем параметры поиска -----

    # время начала интервала поиска
    time_start = datetime.datetime(2022, 8, 18, 7, 58, 1, 12000)

    # время окончания интервала поиска
    time_finish = datetime.datetime(2022, 8, 18, 10, 57, 39, 2000)

    # разница данных, при которых будет выполняться условие добавления в конечный результат
    difference = 74.5

    # ----- запуск проверки -----

    # получаем время начала проверки
    time_launch = datetime.datetime.now()

    # считываем данные из файла csv
    list_in = reading_csv(file_start_csv)
    print(f'Количество строк начальных данных - {len(list_in) - 1}')

    # запускаем проверку параметров
    list_out = checkin_data(list_in, time_start, time_finish, difference)
    print(f'Количество строк конечных данных - {len(list_out) - 1}')

    # получаем время окончания проверки
    time_end = datetime.datetime.now()

    # записываем полученные данные в файл
    writing_csv(file_finish_csv, list_out)

    # получаем время выполнения проверки
    time_delta = time_end - time_launch
    print(f'Время выполнения проверки - {time_delta}')


if __name__ == '__main__':

    start_researching()
    print('')
