# prenoms

[![Build Status](https://travis-ci.com/cnovel/prenoms.svg?branch=master)](https://travis-ci.com/cnovel/prenoms) [![CodeCoveragge](https://codecov.io/gh/cnovel/prenoms/branch/master/graph/badge.svg)](https://codecov.io/gh/cnovel/prenoms) [![PyPI version](https://badge.fury.io/py/prenoms.svg)](https://badge.fury.io/py/prenoms) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prenoms)

Générateur de prénoms

## Installation

Le script est disponible sur PyPI. Pour installer avec pip :

```bash
pip install prenoms
```

## Utilisation
`prenoms` peut être utilisé via la ligne de commande ou importé comme paquet Python.

### Utilisation depuis la ligne de commande
Pour utiliser `prenoms` depuis la ligne de commande :

```bash
$ prenoms
Jean Dupont
```

### Utilisation du paquet Python
Quelques exemples d'utilisation :

```python
>>> import prenoms
>>> prenoms.get_nom_complet()
'Jean Bernard'
>>> prenoms.get_prenom()
'Lucie'
>>> prenoms.get_nom()
'Lefevre'
>>> prenoms.get_prenom(gender=Gender.MALE, originality=Originality.VERY_RARE, year=1995)
'Hortensius'
```

Le paramètre `originality` permet de spécifier l'originalité du nom ou du prénom. Quatre options sont disponibles :

* `COMMON`
* `UNCOMMON`
* `RARE`
* `VERY_RARE`

Le paramètre `gender` permet de spécifier le genre du prénom, les options sont `MALE` ou `FEMALE`.

Le paramètre `year` permet de spécifier la décennie de recherche pour un nom ou un prénom. Si ce paramètre est égal à `None`, l'entièreté des données est utilisée.

## Licence
Ce projet est sous licence MIT.

Les données dans le dossier `prenoms/data` proviennent de l'INSEE et appartiennent au domaine public.
