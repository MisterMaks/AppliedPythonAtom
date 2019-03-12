import sys

# Ваши импорты

from proverochka_encoda import *
from proverochka_formata import *
from cool_print import *
import os.path

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код


def proverochka_isfile(file):
    if os.path.isfile("files/posts-utf8.json") is True:
        return True
    else:
        return False

if proverochka_isfile(filename) is False:
    print("Файл не валиден")
elif true_encode(filename) is None:
    print("Формат не валиден")
elif true_format(filename, true_encode(filename)) is None:
    print("Формат не валиден")
else:
    encode = true_encode(filename)
    formata = true_format(filename, encode)
    true_print(filename, encode, formata)
