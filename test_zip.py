from zipfile import ZipFile
import zipfile
import os

# – Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;
# – Положить его в ресурсы;
# – Реализовать чтение и проверку содержимого каждого файла из архива в виде тестов

# объявление переменных
path_ = 'resources/'

# открытие файла на запись
zip_p = ZipFile(os.path.join(path_, 'zip_1.zip'), 'w')
# Запись файла в архив с указанием типа архивирования
print(os.listdir('resources/'))
zip_p.write('names.csv', compress_type=zipfile.ZIP_DEFLATED)
# Запись нескольких файлов в архив
# чтение содержимого
print(str(zip_p.namelist()))
# проверка имени файла
#assert 'names.csv' in zip_p.namelist()
# закрытие файла
zip_p.close()
# удаление файла
os.remove(os.path.join(path_, 'zip_1.zip'))
