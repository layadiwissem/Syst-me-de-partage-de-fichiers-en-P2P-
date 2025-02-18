import socket

# Création d'un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
server_address = ('localhost', 12345)
client_socket.connect(server_address)
# Envoyer le mot 'recherche' au serveur
client_socket.sendall(b'recherche')

try:
    # Demander à l'utilisateur un mot-clé
    keyword = input("Entrez un mot-clé : ")
    host = 'user2'
    search = "{},{}".format(keyword, host)
    # Envoyer le mot-clé au serveur
    client_socket.sendall(search.encode())

    # Attendre la réponse du serveur
    response = client_socket.recv(1024).decode().split(",")
    print("réponse du serveur")
    for j in response:
        print(j)

    choix=input("donnez le nom du fichier")
    client_socket.sendall(choix.encode())

finally:
    # Fermeture de la connexion
    client_socket.close()
