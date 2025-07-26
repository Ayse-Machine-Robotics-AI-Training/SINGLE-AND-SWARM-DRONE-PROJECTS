import socket

def start_server():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Sunucu dinleniyor: {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Bağlantı geldi: {addr}")
                data = conn.recv(1024)
                if data:
                    print("Alınan veri:", data.decode('utf-8'))
                    yanit = f"Aldım: {data.decode('utf-8')}"
                    conn.sendall(yanit.encode('utf-8'))

start_server()
