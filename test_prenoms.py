#!/usr/bin/env python
import unittest
import sys
from os.path import abspath, join, dirname
from io import StringIO
import prenoms
from prenoms import Originality, Gender
from prenoms.utils import create_key
from prenoms.main import main


def full_test_path(filename: str) -> str:
    return abspath(join(dirname(__file__), "test", filename))


class patch_stdout(object):
    def __init__(self):
        self.stdout = StringIO()
        self.real_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = self.stdout
        return sys.stdout

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self.real_stdout


class patch_file:

    def __init__(self, file_dict, tables_dict):
        self.files = file_dict
        self.tables = tables_dict

    def __enter__(self):
        self.old_files = prenoms.utils.FILES
        self.old_tables = prenoms.utils.TABLES
        prenoms.utils.FILES = self.files
        prenoms.utils.TABLES = self.tables

    def __exit__(self, type, value, traceback):
        prenoms.FILES = self.old_files
        prenoms.TABLES = self.old_tables


test_files = {}
for t in ['first', 'last']:
    for gdr in ['.m', '.f']:
        # Years
        for y in range(1891, 2021, 10):
            if (y == 1891 and t == 'first') or (y >= 2001 and t == 'last'):
                continue
            file_key = t
            if t == 'first':
                file_key += gdr
            file_key += '.{}'.format(y)
            test_files[file_key] = full_test_path("prenoms.txt") if t == 'first'\
                else full_test_path("noms.txt")

        # Complete collection
        all_key = t
        if t == 'first':
            all_key += gdr
        all_key += '.all'
        test_files[all_key] = full_test_path("prenoms.txt") if t == 'first'\
            else full_test_path("noms.txt")

test_tables = {}
for k in test_files.keys():
    test_tables[k] = prenoms.utils.NameTable(test_files[k])


class NamesTest(unittest.TestCase):
    def test_correct_files(self):
        with patch_file(test_files, test_tables):
            # Without argument
            self.assertEqual(prenoms.get_prenom(), "Claude")
            self.assertEqual(prenoms.get_nom(), "Dupont")
            self.assertEqual(prenoms.get_nom_complet(), "Claude Dupont")

            # Originality
            self.assertEqual(prenoms.get_prenom(originality=Originality.COMMON), "Claude")
            self.assertEqual(prenoms.get_prenom(originality=Originality.UNCOMMON), "Lawrence")
            self.assertEqual(prenoms.get_prenom(originality=Originality.RARE), "Elidja")
            self.assertEqual(prenoms.get_prenom(originality=Originality.VERY_RARE), "Élouen")
            self.assertEqual(prenoms.get_nom(originality=Originality.COMMON), "Dupont")
            self.assertEqual(prenoms.get_nom(originality=Originality.UNCOMMON), "Galopin")
            self.assertEqual(prenoms.get_nom(originality=Originality.RARE), "Mournet")
            self.assertEqual(prenoms.get_nom(originality=Originality.VERY_RARE), "Zablot")

            # Gender
            self.assertEqual(prenoms.get_prenom(gender=Gender.MALE), "Claude")
            self.assertEqual(prenoms.get_prenom(gender=Gender.FEMALE), "Claude")

            # Year
            self.assertEqual(prenoms.get_prenom(year=1995), "Claude")
            self.assertEqual(prenoms.get_nom(year=1995), "Dupont")

    def test_empty_file(self):
        empty_files = {}
        empty_tables = {}
        for key in test_files.keys():
            empty_tables[key] = prenoms.utils.NameTable(full_test_path('empty.txt'))
        with patch_file(empty_files, empty_tables):
            pren = prenoms.get_prenom()
            self.assertEqual(pren, '')
            self.assertEqual(prenoms.get_nom(), '')
            self.assertEqual(prenoms.get_nom_complet(), '')

    def test_create_key(self):
        for i in range(1899, 1999, 10):
            self.assertEqual(create_key('last', i), 'last.{}'.format(i-8))
        self.assertEqual(create_key('last', 2003), 'last.1991')
        self.assertEqual(create_key('first', 1850, Gender.MALE), 'first.m.1901')
        self.assertEqual(create_key('first', 2005, Gender.MALE), 'first.m.2001')
        self.assertEqual(create_key('first', 2015, Gender.FEMALE), 'first.f.2011')

    def test_bad_name_tables(self):
        for i in [1, 2]:
            nt = prenoms.utils.NameTable(full_test_path('bad_{}.txt'.format(i)))
            self.assertEqual(nt.common_id(), 0)
            self.assertEqual(nt.uncommon_id(), 0)
            self.assertEqual(nt.rare_id(), 0)
            self.assertEqual(nt.total_id(), 0)
            self.assertEqual(nt.get_name(0), '')


class CommandLineTest(unittest.TestCase):
    def test_cli(self):
        with patch_stdout() as stdout:
            with patch_file(test_files, test_tables):
                main()
                self.assertEqual(stdout.getvalue(), "Claude Dupont\n")


if __name__ == '__main__':
    unittest.main()
