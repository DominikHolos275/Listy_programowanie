def kon_lin(sciezka_do_pliku):
    """ Funkcja kon_lin(sciezka_do_pliku) zmienia znaki końca linii w plikach tekstowych z uniksowych
    na widowsowe i odwrotnie
    Input:
        sciezka_do_pliku(str)-ściezka do pliku tekstowego
    Output:
        brak"""
        
    with open(sciezka_do_pliku, 'rb') as plik:
        tekst = plik.read()
        print(tekst)
        # konwersja znaków końca linii z uniksowych na windowsowe
        if b'\r\n' in tekst:
            tekst = tekst.replace(b'\r\n', b'\n')
        # konwersja znaków końca linii z windowsowych na uniksowe
        
        else:
            if b'\n' in tekst:
                tekst = tekst.replace(b'\n', b'\r\n')
    
        with open(sciezka_do_pliku, 'wb') as plik:
            plik.write(tekst)


kon_lin(r"C:\Users\dbjd2\Desktop\PYTON\txt_l3z2.txt")