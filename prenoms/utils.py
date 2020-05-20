from os.path import abspath, join, dirname
import random
from math import floor
from enum import Enum


def full_names_path(filename: str):
    return abspath(join(dirname(__file__), 'data', filename))


FILES = {}
for t in ['first', 'last']:
    for gdr in ['.m', '.f']:
        # Years
        for y in range(1891, 2021, 10):
            if (y == 1891 and t == 'first') or (y >= 2001 and t == 'last'):
                continue
            file_key = t
            dist = 'dist'
            if t == 'first':
                dist += '.prenoms{}'.format(gdr)
                file_key += gdr
            dist += '.{}.txt'.format(y)
            file_key += '.{}'.format(y)
            FILES[file_key] = full_names_path(dist)

        # Complete collection
        all_key = t
        all_dist = 'dist'
        if t == 'first':
            all_dist += '.prenoms{}'.format(gdr)
            all_key += gdr
        all_key += '.all'
        all_dist += '.all.txt'
        FILES[all_key] = full_names_path(all_dist)


class NameTable:
    def _clear(self):
        self._ids = [0, 0, 0, 0]
        self._names = ['']

    def __init__(self, file):
        with open(file, mode='r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) < 2:  # Bad format -> empty table
                self._clear()
                return

            self._ids = [int(i) for i in lines[0].strip().split()]
            self._names = [n for n in lines[1].strip().split(',') if n]
            if len(self._ids) != 4 or len(self._names) == 0:
                self._clear()
                return

    def common_id(self):
        return self._ids[0]

    def uncommon_id(self):
        return self._ids[1]

    def rare_id(self):
        return self._ids[2]

    def total_id(self):
        return self._ids[3]

    def get_name(self, i: int):
        return self._names[i]


TABLES = {}
for k in FILES.keys():
    TABLES[k] = NameTable(FILES[k])


class Originality(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4


class Gender(Enum):
    MALE = 1
    FEMALE = 2


def create_key(name_type: str, year: int, gender: Gender = None):
    if year is not None:
        if year < 1901 and name_type == 'last':
            year_string = '1891'
        elif year < 1911:
            year_string = '1901'
        elif year < 1921:
            year_string = '1911'
        elif year < 1931:
            year_string = '1921'
        elif year < 1941:
            year_string = '1931'
        elif year < 1951:
            year_string = '1941'
        elif year < 1961:
            year_string = '1951'
        elif year < 1971:
            year_string = '1961'
        elif year < 1981:
            year_string = '1971'
        elif year < 1991:
            year_string = '1981'
        elif year < 2001:
            year_string = '1991'
        elif year >= 2001 and name_type == 'last':
            year_string = '1991'
        elif year < 2011:
            year_string = '2001'
        else:
            year_string = '2011'
    else:
        year_string = 'all'

    key = name_type
    if gender is not None:
        if gender == Gender.MALE:
            key += '.m'
        else:
            key += '.f'
    key += '.' + year_string
    return key


def get_bounds_from_table(table: NameTable, originality: Originality) -> (int, int):
    if originality == Originality.UNCOMMON:
        return table.common_id(), table.uncommon_id()
    if originality == Originality.RARE:
        return table.uncommon_id(), table.rare_id()
    if originality == Originality.VERY_RARE:
        return table.rare_id(), table.total_id()
    return 0, table.common_id()


def get_name_from_table(table: NameTable, originality: Originality):
    min_id, max_id = get_bounds_from_table(table, originality)
    name_id = int(floor(random.random() * (max_id - min_id) + min_id))
    return table.get_name(name_id)


def get_name(name_type: str, originality: Originality, year: int, gender: Gender = None):
    key = create_key(name_type, year, gender)
    return get_name_from_table(TABLES[key], originality)
