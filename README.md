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
>>> prenoms.get_prenom(originality=Originality.VERY_RARE, gender=Gender.MALE, year=1995)
'Hortensius'
>>> prenoms.get_nom(originality=Originality.VERY_RARE, year=1995)
'Wazner'
```

Le paramètre `originality` permet de spécifier l'originalité du nom ou du prénom. Quatre options sont disponibles :

* `COMMON`
* `UNCOMMON`
* `RARE`
* `VERY_RARE`

Le paramètre `gender` permet de spécifier le genre du prénom, les options sont `MALE` ou `FEMALE`.

Le paramètre `year` permet de spécifier la décennie de recherche pour un nom ou un prénom. Si ce paramètre est égal à `None`, l'entièreté des données est utilisée.

## Détails sur les données
Les prénoms sont ceux de personnes nées entre 1900 et 2018 en France (hors Mayotte), regroupés par décennies. Ils doivent avoir été donnés au moins 3 fois par an pour figurer dans la liste globale, et 10 fois par décénnie pour apparaître dans les listes décennales.

Les noms de famille (anciennement noms patronymiques) sont ceux de personnes nées entre 1891 et 2000 en France métropolitaine (sauf celles nées avant 1946 et décédées avant 1972) et celles nées entre 1900 et 2000 dans un département d'outremer. Un nom doit apparaître 10 fois par décénnie pour apparaître dans les listes décennales.

Un nom ou un prénom est commun s'il apparaît plus de 500 fois dans une liste, peu commun s'il apparaît plus de 100 fois, rare s'il apparaît plus de 50 fois, et très rare sinon.

## Licence
Ce projet est sous licence MIT.

Les données dans le dossier `prenoms/data` proviennent de l'INSEE et appartiennent au domaine public.
