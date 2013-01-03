PyCraft
=======

Résumé
------

Jeu où l'on place des blocs en 2D. (Fortement inspiré de Minecraft). 

Dépendances (pour Debian/Ubuntu)
--------------------------------

Dans un terminal, entrer la commande suivante : ::
    
    sudo apt-get install python-pygame

Lancement du jeu
----------------

Dans un terminal, entrer les commandes suivantes : ::
    
    cd pycraft/
    python game.py

Commandes
---------

* Clic gauche : place un bloc.
* Clic droit : supprime le bloc en dessous du pointeur.
* Barre Espace : supprime tous les blocs sur la map.
* Touche 's' : sauvegarde la map (interface dans le terminal !) ::

    ===SAUVEGARDE===
    Destination : chemin/vers/le/fichier.nimportequelformat

* Touche 'l' : lire un fichier que vous avez sauvegardé (interface dans le
  terminal !) ::

    ===LECTURE===
    Destination : chemin/vers/le/fichier.nimportequelformat

* Touche 'échap' : quitter le jeu

