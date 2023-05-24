import requests
from bs4 import BeautifulSoup
import webbrowser

def Wiki(ilosc_prob):
    """ Funkcja Wiki(ilosc_prob) podaje tytuł losowego artykułu z wikipedii i pyta czy chcemy go otworzyć, 
    wpisujemy tak/nie w zależności czy zainteresował nas tan temat. Losowane jest maksymalnie ilosc_prob artukułów 
    Input:
        ilosc_prob- maksymalna ilość proprzycji, które zostaną zaprezentowane
    Output:
        pytanie Czy chcesz otworzyć artykuł w przeglądarce? (tak/nie) na które odpowiadamy
        w zależności czy zainteresował nas tan temat"""
    
    for i in range(ilosc_prob):
        # Pobranie losowego artykułu z Wikipedii
        url = "https://en.wikipedia.org/wiki/Special:Random"
        response = requests.get(url)
        
        # Parsowanie HTML artykułu za pomocą BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h1", {"id": "firstHeading"}).text
        
        # Wyświetlenie tytułu artykułu
        print("Wylosowany artykuł: {}".format(title))
        
        # Pytanie użytkownika o otwarcie artykułu w przeglądarce
        answer = input("Czy chcesz otworzyć artykuł w przeglądarce? (tak/nie)\n")
        if answer.lower() == "tak":
            # Otwarcie artykułu w przeglądarce za pomocą webbrowser
            webbrowser.open_new_tab(response.url)
            break
        elif answer.lower() == "nie":
            continue
        else:
            raise ValueError("zła odpowiedz napisz tak lub nie")
Wiki(5)