import os
import datetime
from ftp_connect import ftp_copy


def ind_date():
    now_date = datetime.datetime.now()
    month_text = ['январь', 'февраль', 'март', 'апрель',
                  'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                  'ноябрь', 'декабрь']
    month_int = ['01 ', '02 ', '03 ', '04 ', '05 ', '06 ', '07 ', '08 ', '09 ', '10 ', '11 ', '12 ']
    while True:
        year = input("Введите год: ")
        if (year == '2019') or (year == '2020'):
            break
        else:
            print("Дата не верна! Повторите ввод")

    while True:
        try:
            month = input("Введите месяц: ")
            try:
                month_test_num = int(month)
            except ValueError:
                month = month.lower()
                try:
                    ind = month_text.index(month)
                    month = month_int[ind]
                    month = month.strip()
                    month_t = month_text[ind]
                    month_i = month_int[ind]
                    break
                except:
                    print("Дата не верна! Повторите ввод")
                    continue
            if (month_test_num < 1) or (month_test_num > 12):
                print("Дата не верна! Повторите ввод")
                continue
            try:
                month = int(month)
                month_t = month_text[month - 1]
                month_i = month_int[month - 1]
                if len(str(month)) != 2:
                    month_t = month_text[month - 1]
                    month_i = month_int[month - 1]
                    month = '0' + str(month)
                break
            except ValueError:
                try:
                    ind = month_text.index(month)
                    month = month_int[ind]
                    month_t = month_text[ind]
                    month_i = month_int[month - 1]
                    break
                except ValueError:
                    print("Дата не верна! Повторите ввод")
                    continue
        except IndexError:
            print("Дата не верна! Повторите ввод")
    while True:
        d_day = ''
        try:
            day = input("Введите день: ")
            day_test_num = int(day)
            if (day_test_num < 1) or (day_test_num > 31):
                print("Дата не верна! Повторите ввод")
                continue
            day = day.lower()
            try:
                day = int(day)
                if len(str(day)) != 2:
                    d_day = day
                    day = '0' + str(day)
                break
            except ValueError:
                print("Дата не верна! Повторите ввод")
        except ValueError:
            print("Дата не верна! Повторите ввод")
        except IndexError:
            print("Дата не верна! Повторите ввод")
    full_date_now = str(day) + '.' + str(month) + '.' + str(year)
    d_day_date = str(d_day) + '.' + str(month) + '.' + str(year)
    result = [month_t, full_date_now, year, month_i, d_day_date]
    return result


def now_date():
    now_date = datetime.datetime.now()
    month_text = ['январь', 'февраль', 'март', 'апрель',
                  'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                  'ноябрь', 'декабрь']
    month_int = ['01 ', '02 ', '03 ', '04 ', '05 ', '06 ', '07 ', '08 ', '09 ', '10 ', '11 ', '12 ']
    year = now_date.year
    month = now_date.month
    month_t = month_text[month - 1]
    month_i = month_int[month - 1]
    if len(str(month)) != 2:
        month = '0' + str(month)
    day = now_date.day - 1
    if len(str(day)) != 2:
        day = '0' + str(day)
    full_date_now = str(day) + '.' + str(month) + '.' + str(year)
    result = [month_t, full_date_now, year, month_i]
    return result


def copy_file(result):
    dir_date_name = str(result[1])
    path_to_month = 'D:\\' + str(result[0]) + '\\'
    try:
        os.mkdir(path_to_month)
    except:
        pass
    path_to_copy = path_to_month + str(result[1]) + '\\'
    try:
        os.mkdir(path_to_copy)
    except:
        print("Директория " + path_to_copy + " уже создана")
    tmp_dir = path_to_copy + 'tmp\\'
    try:
        os.mkdir(tmp_dir)
    except:
        print("Директория " + tmp_dir + " уже создана")
    ftp_copy(result, path_to_copy)
    dir_result = [path_to_copy, tmp_dir, dir_date_name]
    return dir_result

