prenoms
=======

Générateur de prénoms

Installation
------------

Le script est disponible sur PyPI. Pour installer avec pip :

    pip install prenoms

Utilisation
-----------
`prenoms` peut être utilisé via la ligne de commande ou importé comme paquet Python.

Utilisation depuis la ligne de commande
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pour utiliser `prenoms` depuis la ligne de commande :

.. code-block::

    $ prenoms
    Jean Dupont

Utilisation du paquet Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Quelques exemples d'utilisation :

.. code-block::

        >>> import prenoms
        >>> prenoms.get_nom_complet()
        'Jean Bernard'
        >>> prenoms.get_prenom()
        'Lucie'
        >>> prenoms.get_nom()
        'Lefevre'
        >>> prenoms.get_prenom(originality=1)
        'Hortensius'


Le paramètre `originality` permet de spécifier l'originalité du nom. Une originalité proche de 0 va retourner des noms communs, une originialité proche de 1 va retourner des noms rares.

Licence
-------
Ce projet est sous licence MIT.

Les données suivante proviennent de l'INSEE et appartiennent au domaine public :

- dist.prenoms.txt
- dist.noms.txt
