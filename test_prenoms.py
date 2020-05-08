#!/usr/bin/env python
import unittest
import sys
from os.path import abspath, join, dirname
from io import StringIO
import prenoms
from prenoms.main import main


def full_path(filename: str) -> str:
    return abspath(join(dirname(__file__), filename))


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


test_files = {
    'first': full_path('test/prenoms.txt'),
    'last': full_path('test/noms.txt'),
}

test_tables = {
    'first': [line.strip() for line in open(test_files['first'], encoding="utf-8")],
    'last': [line.strip() for line in open(test_files['last'], encoding="utf-8")],
}


class NamesTest(unittest.TestCase):
    def test_correct_files(self):
        with patch_file(test_files, test_tables):
            self.assertEqual(prenoms.get_prenom(), "Claude")
            self.assertEqual(prenoms.get_nom(), "Dupont")
            self.assertEqual(prenoms.get_nom_complet(), "Claude Dupont")
            self.assertEqual(prenoms.get_nom_complet(0.3), "Claude Dupont")

    def test_empty_file(self):
        empty_files = {
            'first': full_path('test/empty.txt'),
            'last': full_path('test/empty.txt'),
        }
        empty_tables = {
            'first': [],
            'last': [],
        }
        with patch_file(empty_files, empty_tables):
            pren = prenoms.get_prenom()
            self.assertEqual(pren, '')
            self.assertEqual(prenoms.get_nom(), '')
            self.assertEqual(prenoms.get_nom_complet(), '')


class CommandLineTest(unittest.TestCase):
    def test_cli(self):
        with patch_stdout() as stdout:
            with patch_file(test_files, test_tables):
                main()
                self.assertEqual(stdout.getvalue(), "Claude Dupont\n")


if __name__ == '__main__':
    unittest.main()
