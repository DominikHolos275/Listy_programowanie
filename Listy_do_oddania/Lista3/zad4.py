import qrcode
import cv2

def QR_creator(wiadomosc, sciezka_do_zapisu):
    """ Funkcja def QR_creator(wiadomosc, sciezka_do_zapisu) pozwala nam na stworzenie kodu QR 
    z dowolnego takstu i zapisania go we wskazanym miejscu.
    Input:
        wiadomosc(str)-wiadomość, którą chcemy zaszyfrować, 
        sciezka_do_zapisu(str)-ścieżka do zapisu kodu QR
    Output:
        brak""" 
        
    img = qrcode.make(wiadomosc)
    img=img.save(sciezka_do_zapisu)

QR_creator("Mam dwa psy, starszy wabi się Fifi a młodszy Wiertararara wrocławira", r"C:\Users\dbjd2\Desktop\PYTON\WIERTARA.png")

def QR_reader(sciezka_do_kodu):
    """ Funkcja def QR_reader(sciezka_do_kodu) pozwala nam na odczyt kodu QR.
    Input:
        sciezka_do_kodu(str)-ścieżka do miejsca zapisu kodu QR do odczytu
    Output:
        decoded_text(str)-odszyfrowana wiadomość"""
        
    # Wczytanie obrazu z pliku
    obraz = cv2.imread(sciezka_do_kodu)

    # Inicjalizacja detektora kodów QR
    detektor = cv2.QRCodeDetector()

    # Odczyt kodu QR z obrazu
    decoded_text, _, _ = detektor.detectAndDecode(obraz)

    return decoded_text

    
print(QR_reader(r"C:\Users\dbjd2\Desktop\PYTON\WIERTARA.png"))
