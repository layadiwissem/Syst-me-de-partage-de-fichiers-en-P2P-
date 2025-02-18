import socket
import hashlib

# Création d'un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port souhaités
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Écoute des connexions entrantes 
server_socket.listen(5)

print("Le serveur écoute sur {}:{}".format(server_address[0], server_address[1]))
hote = "faux"
# Dictionnaire contenant les informations d'authentification
users = {
    "wissam": hashlib.sha256("irs".encode()).hexdigest(),
    "syrine": hashlib.sha256("irs".encode()).hexdigest(),
    "ines": hashlib.sha256("irs".encode()).hexdigest()
}

# Dictionnaire pour stocker les listes de fichiers de chaque client
client_files = {}

# Dictionnaire pour stocker le hostname associé au numéro de port du client
client_info = {}
tableau = []
def authenticate(username, password):
    # Vérification de l'authentification
    if username in users and users[username] == password:
        return True
    else:
        return False

while True:
    # Attente d'une connexion
    client_socket, client_address = server_socket.accept()
    
    print("Nouvelle connexion de:", client_address)
    # Réception du mot envoyé par le client
    received_word = client_socket.recv(1024).decode()
    if received_word == 'ftp':

        # Réception des données d'authentification
        data = client_socket.recv(1024).decode().split(",")
        username = data[0]
        password = data[1]

        # Vérification de l'authentification
        if authenticate(username, password):
            client_socket.send(bytes("Authentification réussie!","utf8"))
            #réception du hostname
            hostname = client_socket.recv(1024).decode()
            print("Hostname reçu du client:", hostname)
            # Enregistrement du hostname avec le numéro de port du client
            client_info[hostname] = client_address[1]
            # Réception de la liste des fichiers
            files_data = client_socket.recv(1024).decode()
            files_list = files_data.split(",")
            
            #for desc in files_list : 
             #   print(desc)
            
            for result in files_list:
                
                tableau.append(result.split('\n'))
            #for case in tableau:
             #   print('affichage case de tableau')
              #  for i in case:
               #     print(i)

            # Stockage de la liste de fichiers dans le dictionnaire
            client_files[hostname] = files_list
            
            # Affichage des fichiers du client actuel
            #print("Liste des fichiers reçus du client {} :".format(hostname))
            #for key, value in client_files.items():
             #   print(key, ":", value)
        else:
            client_socket.send(bytes("Échec de l'authentification!","utf8"))
    else:
        search = client_socket.recv(1024).decode().split(",")
        keyword = search[0]
        host = search[1]
        print(keyword)
        print(host)
        result = []
        #for case in tableau:
         #    print('affichage case de tableau dans recherche')
          #   for i in case:
           #      print(i)

        for fichier in tableau:
            if host != fichier[2]:
                if keyword in fichier[1]:
                    tmp = []
                    tmp.append(fichier[0])
                    tmp.append(fichier[2])
                    result.append(tmp)
        
            
        #for rslt in result:
         #   print(rslt[0])
        noms = []
        for f in result:
            noms.append(f[0])
        names=",".join(noms)
        client_socket.sendall(names.encode())


        choix = client_socket.recv(1024).decode()
        for r in result:
            if choix == r[0]:
                hote = r[1]
        port = client_info[hote]
        
        client_socket.sendall(port.encode())
        
            
    
        
        
        
        
        # Liste pour stocker les fichiers non associés à la clé précise
        #files_without_key = []
        #for hostname, files in client_files.items():
         #   if hostname != host:
          #      files_without_key.extend(files)

        #print("Fichiers non associés à la clé précise :", files_without_key)

        # Liste pour stocker les fichiers contenant le mot précis
        #files_with_word = []
        #for file_content in files_without_key:
         #   print(file_content)
            
            
          #  if keyword in file_content:
           #     files_with_word.append(file_content)

        # Afficher les fichiers contenant le mot précis
        #print("Fichiers contenant le mot précis :", files_with_word)
    
    
    # Fermeture de la connexion
    client_socket.close()
