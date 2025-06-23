import socket

HOST = '127.0.0.1'  # Adresse IP locale
PORT = 65432        # Port d'écoute

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serveur en écoute sur {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connecté par {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Reçu: {data.decode()}")
            conn.sendall(data)  # Echo des données reçues