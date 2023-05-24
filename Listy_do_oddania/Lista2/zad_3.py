import os
import zipfile
import datetime

""" Funkcja kopia(folder, sciezka_docelowa) tworzy kopię bezpieczeństwa 
    wybranych katalogów do archiwów ZIP, zapisuje je w określonym miejscu.

    Input:
    folder(str): ścieżka do folderu, który ma zostać skopiowany.
    sciezka_docelowa(str): ścieżka do folderu, gdzie kopia ma zostać zapisana.
    
    Output:
    wypisuje pliki które znalazły się w zipie oraz w zyznaczonym przez nas miejscu zapisuje kopię."""
def kopia(folder, sciezka_docelowa):
    nazwa_zip = datetime.datetime.now().strftime('%Y-%m-%d') + '_kopia.zip'
    archiwum = zipfile.ZipFile(os.path.join(sciezka_docelowa, nazwa_zip), 'w')

    for folder, podfoldery, pliki in os.walk(folder):
        for plik in pliki:
            sciezka_pliku = os.path.join(folder, plik)
            archiwum.write(sciezka_pliku, os.path.relpath(sciezka_pliku, folder), compress_type=zipfile.ZIP_DEFLATED)

    archiwum.close()

kopia(r"C:\Users\dbjd2\Desktop\PYTON", r"C:\Users\dbjd2\Desktop\PYTON")