import getpass
import socket
import hashlib
import os

# Création d'un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
server_address = ('localhost', 12345)
client_socket.connect(server_address)
# Envoyer le mot 'ftp' au serveur
client_socket.sendall(b'ftp')
current_directory = os.getcwd()

# Obtenir la liste des fichiers dans le répertoire courant
def filter_files():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    return [file for file in files if file.startswith('desc')]

# Afficher la liste des fichiers qui commencent par 'desc'
#print("Fichiers qui commencent par 'desc' dans le répertoire courant:")
#for file in filter_files:
 #   print(file)

# Afficher la liste des fichiers
#print("Fichiers dans le répertoire courant:")
#for file in files:
 #   print(file)
# Saisie du nom d'utilisateur et du mot de passe
username = input("Nom d'utilisateur : ")
password = getpass.getpass("Mot de passe : ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
auth_data = "{},{}".format(username, hashed_password)

# Envoi des données d'authentification au serveur
client_socket.sendall(auth_data.encode())

# Réception de la réponse du serveur
response = client_socket.recv(1024)
print("Réponse du serveur:", response.decode())
if response.decode() == "Authentification réussie!":
    hostname = "user2"
    client_socket.sendall(hostname.encode())
    # Liste pour stocker le contenu des fichiers
    files_content = []
    filtered_files = filter_files()
    for file_name in filtered_files :
        with open(file_name, 'r') as file:
            file_content = file.read()
            files_content.append(file_content)
    
    
    
    #for fichier in files_content :
     #   print(fichier)
    files_data = ",".join(files_content)
    client_socket.sendall(files_data.encode())

    print("Liste des fichiers envoyée au serveur.")

# Fermeture de la connexion
client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12346)
server_socket.bind(server_address)

# Écoute des connexions entrantes
server_socket.listen(5)

while True:
    # Attente d'une connexion
    client_sock, client_address = server_socket.accept()
    received_name = client_sock.recv(1024).decode()
    # Ouverture du fichier en mode lecture binaire
    with open(received_name, 'rt') as file:
         # Lecture et envoi du contenu du fichier par blocs
        while True:
            data = file.read(1024)
            if not data:
                break  # Fin de fichier
            client_sock.sendall(data.encode())
