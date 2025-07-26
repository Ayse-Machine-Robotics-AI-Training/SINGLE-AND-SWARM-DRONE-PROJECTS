import socket

dron_verileri = {
    "dron1": "",
    "dron2": "",
    "dron3": ""
}

def start_server():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Sunucu dinleniyor {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Bağlantı: {addr}")
                data = conn.recv(1024)
                if data:
                    mesaj = data.decode('utf-8')
                    print("Alınan:", mesaj)

                    try:
                        dron, veri = mesaj.split(":", 1)
                        if dron in dron_verileri:
                            dron_verileri[dron] = veri
                            print(f"{dron} verisi güncellendi: {veri}")
                    except Exception as e:
                        print("Veri ayrıştırma hatası:", e)

                    print("⏬ Anlık Durum:", dron_verileri)

start_server()
