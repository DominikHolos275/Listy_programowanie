from PyPDF2 import PdfReader, PdfWriter

def dzielPDF(sciezka_do_pdf, sciezka_do_zapisu, podzial_stron):
    """ Funkcja dzielPDF(sciezka_do_pdf, sciezka_do_zapisu, podzial_stron)
    dzieli wskazany przez nas (za pomocą scieżki) plik PDF na mniejsze co okresloną ilość stron
    ostatni plik to pozostałe strony(reszta z podzielenia całości przez wskazaną ilość
    Input:
        sciezka_do_pdf(str)-sciezka do pdf 
        sciezka_do_zapisu(str)-scieżka do miejsca w którym chcemy zapisać nasze pliki PDF
        podzial_stron(int)-liczba stron każdego dokumentu.
    Output:
        lista_pdfów(list)-lista ścieżek do nowopowstałych podzielonych PDF-ów."""
    reader = PdfReader(open(sciezka_do_pdf, "rb"))
    ilosc_stron = len(reader.pages)
    lista_pdfów=[]
    print()
    for i in range(0, ilosc_stron, podzial_stron):
        pdf_writer = PdfWriter()
        for j in range(i, i+podzial_stron):
            if j < ilosc_stron:
                strona = reader.pages[j]
                pdf_writer.add_page(strona)
            else:
                break
        sciezka_do_nowego_pdf = f"{sciezka_do_zapisu}/part_{i//podzial_stron+1} strony {i+1} - {int((i//podzial_stron+1)*podzial_stron)}.pdf"
        with open(sciezka_do_nowego_pdf, 'wb') as nowy_plik:
            pdf_writer.write(nowy_plik)
        lista_pdfów.append(sciezka_do_nowego_pdf)
    return lista_pdfów
#podział pliku PDF
lista=dzielPDF(r"C:\Users\dbjd2\Desktop\PYTON\AM2.pdf", r"C:\Users\dbjd2\Desktop\PYTON", 27)
 
def laczPDF(lista_pdfów, sciezka_do_zapisu):
    """ Funkcja laczPDF(lista_pdfów, sciezka_do_zapisu)
    łączy wskazane przez nas (za pomocą scieżek w postaci listy) pliki PDF w jeden duży plik PDF
    Input:
        lista_pdfów(list)-lista ścieżek do PDF-ów które chcemy złączyć (w odpowiedniej kolejności),
        sciezka_do_zapisu(str)-scieżka do miejsca w którym chcemy zapisać nasz plik
    Output:
        brak"""
    pdf_writer = PdfWriter()
    for i in range(len(lista_pdfów)):
        reader = PdfReader(open(lista_pdfów[i], "rb"))
        ilosc_stron = len(reader.pages)
        
        for j in range(ilosc_stron):
            strona = reader.pages[j]
            pdf_writer.add_page(strona)

    sciezka_do_nowego_pdf = f"{sciezka_do_zapisu}/połączony PDF.pdf"
    with open(sciezka_do_nowego_pdf, 'wb') as nowy_plik:
        pdf_writer.write(nowy_plik)
        
#łączenie pliku PDF
laczPDF(lista, r"C:\Users\dbjd2\Desktop\PYTON")

import difflib

pdf1 = PdfReader(open(r"C:\Users\dbjd2\Desktop\PYTON\AM2.pdf", "rb"))
pdf2 = PdfReader(open(r"C:\Users\dbjd2\Desktop\PYTON\połączony PDF.pdf", "rb"))

#Pętla sprawdzająca czy plik pierwotny i powstały po podzielieniu i ponownym złączeniu są identyczne jeśli tak to print("All pages match.") 
for i in range(len(pdf1.pages)):
    page1 = pdf1.pages[i].extract_text()
    page2 = pdf2.pages[i].extract_text()
    # porównanie tekstu na poziomie linii i znaków
    diff = difflib.ndiff(page1.splitlines(), page2.splitlines())
    # obliczenie stopnia dopasowania
    match_ratio = difflib.SequenceMatcher(None, page1, page2).ratio()
    # drukowanie wyniku
    if match_ratio != 1.0:
        print(f"Pages {i+1} do not match.")
        print('\n'.join(diff))
        break
else:
    print("All pages match.")
    
#pdf1 = PdfReader(open(r"C:\Users\dbjd2\Desktop\PYTON\AM2.pdf", "rb"))
#pdf2 = PdfReader(open(r"C:\Users\dbjd2\Desktop\PYTON\połączony PDF.pdf", "rb"))

#for i in range(len(pdf1.pages)):
#    if pdf1.pages[i] != pdf2.pages[i]:
#        print(False)
#        break
#else:
#    print(True)
