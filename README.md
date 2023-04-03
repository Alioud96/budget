# Gestion de budget

Développper une application de gestion de budget en python console
Description

La platefome d'une gestion de budget doit permettre à l'utilisateur:

. D'enrigistrer ses depenses . D'enrigistrer ses revenus . De consulter l'ecart qui est entre ses depenses et revenus.

. Les pré-requis

tout d'abord on va installé visual code et python pour la version 3

. Guide d'installation

pour installer dbBrowsersur linux on utilise la commande suivante: sudo apt-get update sudo apt install sqlite3browser

. Guide d'utilisation on cree un dossier vide dans mon bureau, ensuite de l'ouvrir avec visual code en tout supposant qu'on a deja installé python sur notre machine et ensuite creer un fichier python en format py c'est a dire le nom du fichier point(.)py et commencer a coder sur notre environnement de travail visual code import sqlite3 qui permet d'importer le module sqlite 3 en mettant conn=sqlite3.connect('nom de la base de donnes'.db) permettant la creation de la bse de donnees cursor= conn.cursor() permet de se connecter a la base de donnees conn.commit() permet de sauvegarder toutes les modifications a la base de donnees
