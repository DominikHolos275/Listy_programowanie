from PyPDF2 import PdfReader, PdfWriter
""" Funkcja dzielPDF(sciezka_do_pdf, sciezka_do_zapisu, podzial_stron)
    dzieli wskazany przez nas (za pomocą scieżki plik pdf na mniejsze co okresloną ilość stron
    ostatni plik to pozostałe strony(reszta z podzielenia całości przez wskazaną ilość
    Input:
        sciezka_do_pdf(str)-sciezka do pdf 
        sciezka_do_zapisu(str)-scieżka do miejsca w którym chcemy zapisać nasze pliki
        podzial_stron(int)-liczba stron każdego dokumentu."""
def dzielPDF(sciezka_do_pdf, sciezka_do_zapisu, podzial_stron):
    reader = PdfReader(open(sciezka_do_pdf, "rb"))
    ilosc_stron = len(reader.pages)
    
    for i in range(0, ilosc_stron, podzial_stron):
        pdf_writer = PdfWriter()
        for j in range(i, i+podzial_stron):
            if j < ilosc_stron:
                strona = reader.pages[j]
                pdf_writer.add_page(strona)
            else:
                break
        sciezka_do_nowego_pdf = f"{sciezka_do_zapisu}/part_{i//podzial_stron+1}.pdf"
        with open(sciezka_do_nowego_pdf, 'wb') as nowy_plik:
            pdf_writer.write(nowy_plik)

dzielPDF(r"C:\Users\dbjd2\Desktop\PYTON\AM2.pdf", r"C:\Users\dbjd2\Desktop\PYTON", 25)