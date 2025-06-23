import socket

def main():
    host = '127.0.0.1'  # Adresse du serveur
    port = 65432   
    
    # définition AF_INET
    #     est une constante utilisée dans la bibliothèque socket de Python. Elle indique que vous souhaitez utiliser le protocole IPv4 pour la communication réseau.

    # AF signifie "Address Family" (famille d'adresses).
    # INET fait référence à "Internet", c’est-à-dire IPv4.
    # Quand vous écrivez :

    # Vous créez un socket qui :

    # utilise IPv4 (AF_INET)
    # fonctionne en mode "stream" (flux), c’est-à-dire TCP (SOCK_STREAM)
    # À retenir :
    # AF_INET = sockets réseau utilisant des adresses IPv4 (par exemple, 127.0.0.1, 192.168.1.1).
    # Pour IPv6, on utiliserait AF_INET6.
    
    # SOCK_STREAM
    #     est une constante utilisée dans la bibliothèque socket de Python. Elle indique que vous souhaitez créer un socket qui utilise le protocole TCP (Transmission Control Protocol).
    # SOCK signifie "Socket Type" (type de socket).


    

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("Entrez un message à envoyer au serveur : ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Réponse du serveur :', data.decode())

if __name__ == "__main__":
    main()
    
# Ce code est un client TCP qui se connecte à un serveur, envoie un message et affiche la réponse du serveur.
# Il utilise le module `socket` de Python pour établir une connexion TCP.
