import socket
import os

# Création d'un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
current_directory = os.getcwd()
# Connexion au serveur
server_address = ('localhost', 12345)
client_socket.connect(server_address)
# Envoyer le mot 'recherche' au serveur
client_socket.sendall(b'recherche')

try:
    # Demander à l'utilisateur un mot-clé
    keyword = input("Entrez un mot-clé : ")
    host = 'user1'
    search = "{},{}".format(keyword, host)
    # Envoyer le mot-clé au serveur
    client_socket.sendall(search.encode())

    # Attendre la réponse du serveur
    response = client_socket.recv(1024).decode().split(",")
    print("réponse du serveur")
    if not response:
        print("aucun fichier ne correspond au mot-clé")
    else:    
        for j in response:
            print(j)

        choix=input("donnez le nom du fichier : ")
        if choix in response:
            client_socket.sendall(choix.encode())
            port = client_socket.recv(1024).decode
        else:
            print("ce fichier linux n'existe pas")


finally:
    # Fermeture de la connexion
    client_socket.close()

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12346)
    client_sock.connect(server_address)
    client_sock.sendall(choix.encode())
    path = current_directory + "/test-2"
    with open(path, 'wt') as file:
        data = client_sock.recv(1024).decode()
        #print(data)
        file.write(data)

