import json
import csv


def true_struct(file, encode, formata):
    lst_file = []
    with open(file, encoding=encode) as f:
        if formata is "json":
            file = json.load(f)
            lst_file.append(list(file[0].keys()))
            for d in file:
                lst_file.append(list(d.values()))
            return lst_file
        elif formata is "csv":
            file = csv.reader(f, delimiter="\t")
            for lst in file:
                lst_file.append(list(lst))
            return lst_file


def true_print(file, encode, formata):
    maks_len_str = []
    lst_file = true_struct(file, encode, formata)
    for i in range(len(lst_file[0])):
        maks_len = 0
        for j in range(len(lst_file)):
            if len(str(lst_file[j][i])) > maks_len:
                maks_len = len(str(lst_file[j][i]))
        maks_len_str.append(maks_len)
    len_str_1 = sum(maks_len_str) + 6 + 5 * (len(lst_file[0]) - 1)
    enex_str = "-" * len_str_1
    print(enex_str)
    print("|", end="")
    for i in range(len(lst_file[0])):
        num_prob = maks_len_str[i]
        print("  "+lst_file[0][i].center(num_prob)+"  ", end="")
        print("|", end="")
    print()
    for i in range(1, len(lst_file)):
        print("|", end="")
        for j in range(len(lst_file[i]) - 1):
            num_prob = maks_len_str[j]
            print(("  " + lst_file[i][j]).ljust(num_prob+2)+"  ", end="")
            print("|", end="")
        num_prob = maks_len_str[len(lst_file[i]) - 1]
        print("  "+str(lst_file[i][len(lst_file[i]) - 1]).rjust(num_prob)+"  ",
              end="")
        print("|")
    print(enex_str)


__all__ = ["true_print"]
