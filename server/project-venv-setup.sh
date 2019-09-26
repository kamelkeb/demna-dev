#!/bin/sh

# Mise en place et activation de 
# l'environnement virtuel Python3
python3 -m venv venv
source venv/bin/activate

# Installation locale des dépendances
pip3 install flask
pip3 install flask-JWT
pip3 install flask-JWT-Extended
pip3 install flask-RESTful
pip3 install flask-SQLAlchemy
