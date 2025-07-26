import socket
import uno

def ensure_sheet_exists(doc, sheet_name):
    sheets = doc.Sheets
    if not sheets.hasByName(sheet_name):
        sheets.insertNewByName(sheet_name, len(sheets))
    return sheets.getByName(sheet_name)

# Her bir dronun kendi verisini yazması
def update_dron1(*args):
    _send_dron_data("dron1")

def update_dron2(*args):
    _send_dron_data("dron2")

def update_dron3(*args):
    _send_dron_data("dron3")

def _send_dron_data(sheet_name):
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = ensure_sheet_exists(doc, sheet_name)
    value = sheet.getCellByPosition(0, 0).String  # A1

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 12345))
            mesaj = f"{sheet_name}:{value}"
            s.sendall(mesaj.encode('utf-8'))
    except Exception as e:
        print("Sunucuya bağlanılamadı:", e)

# Tüm verileri sonuçlar sayfasında göster
def update_sonuclar(*args):
    doc = XSCRIPTCONTEXT.getDocument()

    # Gerekli sayfalar
    dron1 = ensure_sheet_exists(doc, "dron1")
    dron2 = ensure_sheet_exists(doc, "dron2")
    dron3 = ensure_sheet_exists(doc, "dron3")
    sonuc = ensure_sheet_exists(doc, "sonuçlar")

    # Başlıklar
    sonuc.getCellByPosition(0, 0).String = "dron1"
    sonuc.getCellByPosition(1, 0).String = "dron2"
    sonuc.getCellByPosition(2, 0).String = "dron3"

    # A1'leri oku → sonuçlar!A2, B2, C2 yaz
    sonuc.getCellByPosition(0, 1).String = dron1.getCellByPosition(0, 0).String
    sonuc.getCellByPosition(1, 1).String = dron2.getCellByPosition(0, 0).String
    sonuc.getCellByPosition(2, 1).String = dron3.getCellByPosition(0, 0).String




