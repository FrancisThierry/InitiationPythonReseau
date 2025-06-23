import socket

# Paramètres du serveur
HOST = '0.0.0.0'  # écoute sur toutes les interfaces
PORT = 12345      # port d'écoute

# Création du socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"Serveur UDP en écoute sur le port {PORT}...")

    # Réception d'un message
    data, addr = server_socket.recvfrom(1024)  # buffer de 1024 octets
    print(f"Message reçu de {addr}: {data.decode()}")