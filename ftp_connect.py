import ftplib
from ftplib import FTP
import sys
import os



def ftp_copy(result, path_to_copy):
    out_path = path_to_copy
    end_path = 'путь'
    ftp = FTP('адрес')
    ftp.login('имя', 'пароль')
    ftp.__class__.encoding = sys.getfilesystemencoding()
    try:
        ftp.cwd('/путь/' + str(result[2]) + '/' + str(result[3]) + str(result[0]) + '/' + str(result[1]) + '/' + end_path + '/')
    except:
        ftp.cwd('/путь/' + str(result[2]) + '/' + str(result[3]) + str(result[0]) + '/' + str(
        result[4]) + '/' + end_path + '/')
    file_names = ftp.nlst()
    for filename in file_names:
        print('Копирование файла: ' + filename)
        host_file = os.path.join(out_path, filename)
        local_file = open(host_file, 'wb')
        ftp.retrbinary('RETR %s' % filename, local_file.write)
        local_file.close()
    print("----------------------------------------------------------------------")
    ftp.quit()
