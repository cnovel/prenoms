from os.path import abspath, join, dirname
import random
from math import floor


def full_path(filename: str):
    return abspath(join(dirname(__file__), filename))


FILES = {
    'first': full_path('dist.prenoms.txt'),
    'last': full_path('dist.noms.txt'),
}

TABLES = {
    'first': [line.strip() for line in open(FILES['first'], encoding="utf-8")],
    'last': [line.strip() for line in open(FILES['last'], encoding="utf-8")],
}


def get_double_rank(originality: float):

    if originality < 0:
        originality = 0
    if originality > 1:
        originality = 1
    rank = random.random()

    power = originality ** 2 - 2.5 * originality + 2

    return rank ** power


def get_name(table: str, originality: float):
    if not TABLES[table]:
        return ""
    rank = get_double_rank(originality)
    list_index = int(floor(rank * len(TABLES[table])))
    return TABLES[table][list_index]
