import socket
import uno

def send_data_via_socket(*args):
    # LibreOffice belge ve hücreye erişim
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.Sheets[0]  # İlk sayfa (Sheet1)

    # A1 hücresindeki veriyi al
    cell_value = sheet.getCellByPosition(0, 0).String

    # TCP soket bağlantı bilgileri
    host = '127.0.0.1'  # Yerel sunucu (localhost)
    port = 12345        # Örnek port (sunucunuzla aynı olmalı)

    try:
        # Soket oluştur ve bağlan
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(cell_value.encode('utf-8'))  # Veriyi gönder
            response = s.recv(1024).decode('utf-8')  # Yanıtı al

            # Yanıtı B1 hücresine yaz
            sheet.getCellByPosition(1, 0).String = response

    except Exception as e:
        # Hata durumunda B1 hücresine hata mesajı yaz
        sheet.getCellByPosition(1, 0).String = f"Hata: {e}"
