import json
import csv


def proverka_jsona(file, encode):
    try:
        with open(file, encoding=encode) as f:
            json.load(f)
    except Exception:
        return False
    else:
        return True


def proverka_csv(file, encode):
    try:
        with open(file, encoding=encode) as f:
            reader = csv.reader(f, delimiter="\t")
            for s in reader:
                len_s = len(s)
                break
            for s in reader:
                if len(s) != len_s:
                    return False
            return True
    except Exception:
        return False


def true_format(file, encode):
    if proverka_jsona(file, encode) is True:
        return "json"
    elif proverka_csv(file, encode) is True:
        return "csv"
    else:
        return None


__all__ = ["true_format"]
