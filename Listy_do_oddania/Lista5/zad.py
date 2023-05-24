from tkinter import *
import requests
import json

try:
    url = "http://api.nbp.pl/api/exchangerates/tables/a/"
    response = requests.get(url)
    data = response.json()

    currency_dict = {"złoty polski":1.00}

    if len(data) > 0 and "rates" in data[0]:
        rates = data[0]["rates"]
        for rate in rates:
            currency_name = rate["currency"]
            currency_rate = rate["mid"]
            currency_dict[currency_name] = currency_rate

    with open(r"C:\Users\dbjd2\Desktop\PYTON\kursy.txt", "w") as file:
        json.dump(currency_dict, file)
        
except:
    print("Wystąpił błąd podczas pobierania danych z serwera.")
    file_path = r"C:\Users\dbjd2\Desktop\PYTON\kursy.txt"
        
    with open(file_path, "r") as file:
        currency_dict = json.load(file)
        
    print("Słownik został wczytany z pliku:", file_path)
        

def oblicz():
    wynik=round(float(kwota1.get())*float(currency_dict[waluta1.get()])/float(currency_dict[waluta2.get()]), 4)
    kwota2.configure(text=str(wynik))

root = Tk()
root.title("Kalkulator walut")
root.geometry('600x150')

# Zwiększenie odstępów między wierszami i kolumnami
#root.grid_rowconfigure(0, minsize=20)
#root.grid_columnconfigure(0, minsize=20)

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)

Label(root, text="Pierwsza waluta").grid(row=1, column=1, sticky=E, padx=10, pady=5)
Label(root, text="Druga waluta").grid(row=2, column=1, sticky=E, padx=10, pady=5)

waluta1 = StringVar(root)
waluta1.set("Wybierz walutę")
waluta1_dropdown = OptionMenu(root, waluta1, "złoty polski", "bat (Tajlandia)", "dolar amerykański", "dolar australijski", "dolar Hongkongu", "dolar kanadyjski", "dolar nowozelandzki", "dolar singapurski", "euro", "forint (Węgry)", "frank szwajcarski", "funt szterling", "hrywna (Ukraina)", "jen (Japonia)", "korona czeska", "korona duńska", "korona islandzka", "korona norweska", "korona szwedzka", "lej rumuński", "lew (Bułgaria)", "lira turecka", "nowy izraelski szekel", "peso chilijskie", "peso filipińskie", "peso meksykańskie", "rand (Republika Południowej Afryki)", "real (Brazylia)", "ringgit (Malezja)", "rupia indonezyjska", "rupia indyjska", "won południowokoreański", "yuan renminbi (Chiny)", "SDR (MFW)")
waluta1_dropdown.grid(row=1, column=2, sticky=W, padx=10, pady=5)

waluta2 = StringVar(root)
waluta2.set("Wybierz walutę")
waluta2_dropdown = OptionMenu(root, waluta2, "złoty polski", "bat (Tajlandia)", "dolar amerykański", "dolar australijski", "dolar Hongkongu", "dolar kanadyjski", "dolar nowozelandzki", "dolar singapurski", "euro", "forint (Węgry)", "frank szwajcarski", "funt szterling", "hrywna (Ukraina)", "jen (Japonia)", "korona czeska", "korona duńska", "korona islandzka", "korona norweska", "korona szwedzka", "lej rumuński", "lew (Bułgaria)", "lira turecka", "nowy izraelski szekel", "peso chilijskie", "peso filipińskie", "peso meksykańskie", "rand (Republika Południowej Afryki)", "real (Brazylia)", "ringgit (Malezja)", "rupia indonezyjska", "rupia indyjska", "won południowokoreański", "yuan renminbi (Chiny)", "SDR (MFW)")
waluta2_dropdown.grid(row=2, column=2, sticky=W, padx=10, pady=5)


Label(root, text="Podaj kwotę").grid(row=1, column=3, sticky=E, padx=10, pady=5)
Label(root, text="Wynik").grid(row=2, column=3, sticky=E, padx=10, pady=5)

kwota1 = Entry(root)
kwota1.grid(row=1, column=4, sticky=W, padx=10, pady=5)

kwota2 = Label(root, text="...")
kwota2.grid(row=2, column=4, sticky=W, padx=10, pady=5)

przycisk_oblicz = Button(root, text="Oblicz", command=oblicz)
przycisk_oblicz.grid(row=1, column=5, sticky=W, padx=10, pady=5)

przycisk_zamknij = Button(root, text="Zamknij", command=root.quit)
przycisk_zamknij.grid(row=2, column=5, sticky=W, padx=10, pady=5)

root.mainloop()

