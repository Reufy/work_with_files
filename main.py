import sys
from daily_information import daily_information as daily
from indicated_date import indicated_date as indicated
from help import help


if len(sys.argv) > 1:
    var = sys.argv[1]
    if var == '1':
        daily()
        sys.exit()
    elif var == '2':
        indicated()
        sys.exit()
    elif var == 'help':
        help()
        sys.exit()
    else:
        help()
        sys.exit()

else:
    while True:
        print("1. Сведения за текущие сутки")
        print("2. Сведения за интересующие сутки")
        print("3. Выход")
        answer = input("Введите интересующий пункт меню: ")
        if answer == '1':
            daily()
            sys.exit()
        elif answer == '2':
            indicated()
            sys.exit()
        elif answer == '3':
            sys.exit()
        else:
            print("Проверьте введённое значение и повторите ввод")
