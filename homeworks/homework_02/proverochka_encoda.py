def proverka_utf8(file):
    try:
        with open(file, encoding="utf8") as f:
            f.read()
    except Exception:
        return False
    else:
        return True


def proverka_cp1251(file):
    try:
        with open(file, encoding="cp1251") as f:
            f.read()
    except Exception:
        return False
    else:
        return True


def proverka_utf16(file):
    try:
        with open(file, encoding="utf16") as f:
            f.read()
    except Exception:
        return False
    else:
        return True


def true_encode(file):
    if proverka_utf8(file) is True:
        return "utf8"
    elif proverka_utf16(file) is True:
        return "utf16"
    elif proverka_cp1251(file) is True:
        return "cp1251"
    else:
        return None


__all__ = ["true_encode"]
