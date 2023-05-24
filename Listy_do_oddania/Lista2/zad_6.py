""" funkcja def obliczenia(wejscie) pozwana na obliczanie działań +-*/ podanego w formie łańcucha znaków i zwraca go w słupku
    input:
        wejscie(srt)-łańcuch znaków zawierający obliczenia
    output:
        zwraca obliczenia w słupku"""
def obliczenia(wejscie):
    wyrazenie = wejscie.replace(" ", "")
    wynik = 0
    # Zainicjowanie zmiennej przechowującej aktualną liczbę
    liczba = 0
    # Zainicjowanie zmiennej przechowującej aktualny operator
    operator = "+"
    liczby=[]
    for i in range(len(wyrazenie)):
        znak = wyrazenie[i]
        # Jeśli znak jest cyfrą, dodaj ją do aktualnej liczby
        if znak.isdigit():
            liczba = (liczba * 10) + int(znak)
        # Jeśli znak nie jest cyfrą lub nie jest ostatnim znakiem w łańcuchu,
        # wykonaj odpowiednie działanie z użyciem aktualnej liczby i operatora
        if not znak.isdigit() or i == len(wyrazenie) - 1:
            liczby.append(liczba)
            if operator == "+":
                wynik += liczba
            elif operator == "-":
                wynik -= liczba
            elif operator == "*":
                wynik *= liczba
            elif operator == "/":
                wynik /= liczba
            # Zresetuj aktualną liczbę i ustaw nowy operator
            liczba = 0
            operator = znak 
    if int(liczby[0])+int(liczby[1]) == wynik:
        print("", liczby[0], "\n", "+", liczby[1], "\n", "-----", "\n", wynik )
    elif liczby[0]-liczby[1] == wynik:
        print("", liczby[0], "\n", "-", liczby[1], "\n", "-----", "\n", wynik )
    elif liczby[0]*liczby[1] == wynik:
        print("", liczby[0], "\n", "*", liczby[1], "\n", "-----", "\n", wynik )
    elif liczby[0]/liczby[1] == wynik: 
        print("", liczby[0], "\n", "/", liczby[1], "\n", "-----", "\n", wynik )
    else:   
        print(wynik)

obliczenia(str(input("Podaj dzałanie ")))

