import socket

# Paramètres du serveur
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
MESSAGE = "Bonjour, serveur UDP !"

# Création du socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Envoi du message
    sock.sendto(MESSAGE.encode(), (SERVER_IP, SERVER_PORT))
    print(f"Message envoyé à {SERVER_IP}:{SERVER_PORT}")