# Description

Projet pour génerer le site <http://le-sceptre-de-la-destruction.net>

# Installation

Il faut installer le module Python [markdown2](https://github.com/trentm/python-markdown2) :

    pip install markdown2

De préférence avec Python3.

# Générer le site

Se mettre à la racine du projet puis lancer `generate.py`

    cd ~/Dev/sceptre
    python3 generate.py

Le projet est généré dans le repertoire www.

# Tester le site en local

En local, on peut tester le projet

    cd ~/Dev/sceptre/www
    python3 runserver.py

Puis aller sur <http://localhost:8000>

# Mettre à jour le site distant

    cd ~/Dev/sceptre/
    scp www/*.html sceptre@vps1:~/sites/www/
    scp www/css/* sceptre@vps1:~/sites/www/css/