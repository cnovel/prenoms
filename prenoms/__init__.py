import prenoms.utils
from prenoms.utils import Gender, Originality
from random import random

__title__ = 'prenoms'
__version__ = '0.5.1'
__author__ = 'Cyril Novel'
__license__ = 'MIT'


def get_prenom(originality: prenoms.utils.Originality = prenoms.utils.Originality.COMMON,
               gender: prenoms.utils.Gender = None,
               year: int = None):
    if gender is None:
        r = random()
        gender = prenoms.utils.Gender.MALE if r < 0.5 else prenoms.utils.Gender.FEMALE
    return prenoms.utils.get_name('first', originality, year, gender)


def get_nom(originality: prenoms.utils.Originality = prenoms.utils.Originality.COMMON,
            year: int = None):
    return prenoms.utils.get_name('last', originality, year)


def get_nom_complet(originality: prenoms.utils.Originality = prenoms.utils.Originality.COMMON,
                    gender: prenoms.utils.Gender = None,
                    year: int = None):
    return '{} {}'.format(get_prenom(originality, gender, year),
                          get_nom(originality, year)).strip()
