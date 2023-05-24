from PIL import Image, ImageDraw, ImageEnhance
"""funkcja watermark(obrazek, znak_wodny, sciezka_do_zapisu) nakłada na siebie dwa obrazy z czego jegen jest znakiem wodnym czyli jest częsciowo przejrzysty.
    input:
        obrazek(str)-ścieżka do pliku z główną ilustracją
        znak_wodny(str)-ścieżka do pliku z ilustrasją która ma stać sie znakiem wodnym na głównym obrazku
        sciezka_do_zapisu(str)-ścieżka do miejsca w którym ma zostać zapisany plik ze zankiem wodnym."""
def watermark(obrazek, znak_wodny, sciezka_do_zapisu):
    img1=Image.open(obrazek)
    # Utwórz obiekt ImageDraw dla obrazka
    draw = ImageDraw.Draw(img1)

    # Ustaw przezroczystość znaku wodnego na 70%
    alpha = 0.3
    enhancer = ImageEnhance.Brightness(Image.open(znak_wodny))
    znak_wodny = enhancer.enhance(alpha)
    
    # Utwórz maskę przezroczystości dla znaku wodnego
    maska = znak_wodny.convert('RGBA')
    maska_data = maska.getdata()
    nowe_dane = []
    for item in maska_data:
        nowe_dane.append((item[0], item[1], item[2], int(alpha*255)))
    maska.putdata(nowe_dane)

    # Oblicz pozycję znaku wodnego w centralnej części obrazka
    pozycja_x = (img1.width - znak_wodny.width) // 2
    pozycja_y = (img1.height - znak_wodny.height) // 2

    # Nałóż znak wodny na obrazek
    img1.paste(znak_wodny, (pozycja_x, pozycja_y), maska)

    # Zapisz obrazek z nałożonym znakiem wodnym do pliku
    img1.save(sciezka_do_zapisu)
    
watermark(r"C:\Users\dbjd2\Desktop\Pies.jpeg",r"C:\Users\dbjd2\Desktop\znak_wodny.jpg", r"C:\Users\dbjd2\Desktop\Pies2.jpeg")