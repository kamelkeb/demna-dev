#!/bin/sh

curl -i -X POST -H "Content-Type: application/json" -d '{"email":"testemail@laposte.net","nom":"testnom","prenom":"testprenom","pseudo":"testpseudo","motdepasse":"testmotdepasse","numtelephone":"0123456789","image":"testimage.png"}' http://127.0.0.1:5000/api/utilisateurs
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"testemail@laposte.net","password":"testmotdepasse"}' http://127.0.0.1:5000/auth

