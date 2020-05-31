from copy_file import now_date, ind_date
import requests
import bs4


def now(now_date):
    result = []
    date_split = str(now_date[1]).split(".")
    day_first = date_split[0]
    month_first = date_split[1]
    year_first = date_split[2]
    day_second = date_split[0]
    month_second = date_split[1]
    year_second = date_split[2]
    url = requests.post("путь",
                        data={
                            ключ:значение
                        })
    if url.status_code == 200:
        for textres in url.iter_content(100000):
            text_web = bs4.BeautifulSoup(textres, features='lxml')
            header = text_web.select('.title01')
            header = header[0].getText()
            result.append(header)
            sved = text_web.select('.style1')
            i = 11
            arr = [11, 12, 20, 21, 29, 30, 38, 39, 47, 48, 56, 57, 65, 66, 74, 75, 83, 84, \
                   92, 93, 101, 102, 110, 111, 119, 120, 128, 129, 137, 138, 146, 147, 155, 156, 164, 165, 173, 174]
            while i < len(sved):
                if i in arr:
                    result.append(sved[i].getText())
                i += 1
    return result


def ind(ind_date):
    result = []
    date_split = str(ind_date[2]).split(".")
    day_first = date_split[0]
    month_first = date_split[1]
    year_first = date_split[2]
    day_second = date_split[0]
    month_second = date_split[1]
    year_second = date_split[2]
    url = requests.post("путь",
                        data={
                            ключ: значение
                        })
    if url.status_code == 200:
        for textres in url.iter_content(100000):
            text_web = bs4.BeautifulSoup(textres, features='lxml')
            header = text_web.select('.title01')
            header = header[0].getText()
            result.append(header)
            sved = text_web.select('.style1')
            i = 11
            arr = [11, 12, 20, 21, 29, 30, 38, 39, 47, 48, 56, 57, 65, 66, 74, 75, 83, 84, \
                   92, 93, 101, 102, 110, 111, 119, 120, 128, 129, 137, 138, 146, 147, 155, 156, 164, 165, 173, 174]
            while i < len(sved):
                if i in arr:
                    result.append(sved[i].getText())
                i += 1
    return result

