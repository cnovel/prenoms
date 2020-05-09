import prenoms.utils

__title__ = 'prenoms'
__version__ = '0.1.7'
__author__ = 'Cyril Novel'
__license__ = 'MIT'


def get_prenom(originality: float = 0.2):
    return prenoms.utils.get_name('first', originality)


def get_nom(originality: float = 0.2):
    return prenoms.utils.get_name('last', originality)


def get_nom_complet(originality: float = 0.2):
    return '{} {}'.format(get_prenom(originality), get_nom(originality)).strip()
