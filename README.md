# Syst-me-de-partage-de-fichiers-en-P2P-

01. Explication du système de partage de fichiers P2P
Ce projet met en place un système de partage de fichiers en P2P basé sur un serveur centralisé et des hôtes utilisateurs (serveurs FTP)
Composants principaux :
Serveur centralisé (serveur-centre.py) :
  Authentifie les utilisateurs.
  Stocke la liste des fichiers partagés.
  Permet la recherche par mots-clés et retourne la localisation des fichiers.
Serveurs FTP (serveur-ftp-1.py, serveur-ftp-2.py) :
  Gèrent les fichiers disponibles.
  S'authentifient auprès du serveur central.
  Répondent aux requêtes de téléchargement.
Clients (client-1.py, client-2.py) :
  Effectuent des recherches de fichiers.
  Récupèrent l'adresse du serveur FTP concerné.
  Téléchargent les fichiers demandés.


