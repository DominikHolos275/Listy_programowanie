import os
import shutil
import datetime

def kopia(sciezka_do_katalogu, rozszerzenie):
    """ Funkcja kopia(sciezka_do_katalogu, rozszerzenie) tworzy kopie zapasowe zmodyfikowanych w ostatnich
    trzech dniach plikach o zadanych rozszerzeniach w podanym katalogu
    Input:
        sciezka_do_katalogu(str)-scieżka do katalogu w którym będziemy szukac plików do kopi zapasowej,
        rozszerzenie(str)-rozszerzenie z którym szukamy plików do kopi zapasowej
    Output:
        brak"""
    # Utwórz ścieżkę do katalogu Backup/copy-X 
    aktualna_data = datetime.datetime.now().strftime("%Y-%m-%d")
    sciezka_do_kopii = os.path.join(r"C:\Users\dbjd2\Desktop\PYTON\Backup", f"copy-{aktualna_data}")
    os.makedirs(sciezka_do_kopii, exist_ok=True)

    # Przeszukaj katalog pod kątem plików o zadanym rozszerzeniu i zapisz ich ścieżki do listy
    pliki_do_kopii = []
    for sciezka, _, pliki in os.walk(sciezka_do_katalogu):
        for plik in pliki:
            if plik.endswith(rozszerzenie):
                sciezka_pliku = os.path.join(sciezka, plik)
                czas_modyfikacji = os.path.getmtime(sciezka_pliku)
                czas_delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(czas_modyfikacji)
                if czas_delta.days <= 3:
                    pliki_do_kopii.append(sciezka_pliku)

    # Skopiuj pliki do katalogu kopii zapasowej, tworząc podkatalogi, jeśli to konieczne
    for plik in pliki_do_kopii:
        nazwa_pliku = os.path.basename(plik)
        sciezka_pliku_w_kopii = os.path.join(sciezka_do_kopii, os.path.relpath(plik, sciezka_do_katalogu))
        sciezka_katalogu_kopii = os.path.dirname(sciezka_pliku_w_kopii)
        os.makedirs(sciezka_katalogu_kopii, exist_ok=True)
        shutil.copy2(plik, sciezka_pliku_w_kopii)
kopia(r"C:\Users\dbjd2\Desktop\PYTON", ".py")