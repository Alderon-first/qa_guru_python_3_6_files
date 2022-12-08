from zipfile import ZipFile
import zipfile
import os

# – Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;
# – Положить его в ресурсы;
# – Реализовать чтение и проверку содержимого каждого файла из архива в виде тестов

# объявление переменных
path_ = 'resources/'
name_fale = 'names.csv'
root = 'files/'
# открытие файла на запись
zip_p = ZipFile(os.path.join(path_, 'zip_1.zip'), 'w')
# Запись файла в архив с указанием типа архивирования
print(os.listdir('files/'))
print(len(os.listdir('files/')))
n = os.listdir('files/')
len_list: int = len(os.listdir('files/'))
# zip_p.write((os.path.join(path_, name_fale)), compress_type=zipfile.ZIP_DEFLATED)
# Запись нескольких файлов в архив
for root, dirs, files in os.walk('files'): # Список всех файлов и папок в директории folder
    for file in files:
        zip_p.write(os.path.join(root, file)) # Создание относительных путей и запись файлов в архив
# чтение содержимого
print(zip_p.namelist())
len_list_zip: int = len(zip_p.namelist())
print(len_list_zip)
# проверка имени файла

assert len_list == len_list_zip # папака содержит столько же файлов, сколько архив
i = 0
for file in n:
    assert n[i] in str(zip_p.namelist())
    i= i+1
# закрытие файла
zip_p.close()
# удаление файла
# os.remove(os.path.join(path_, 'zip_1.zip'))
