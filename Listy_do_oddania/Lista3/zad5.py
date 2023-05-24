def nawiasy(wyrazenie):
    """ Funkcja nawiasy(wyrazenie) sprawdza czy wszystkie nawiasy w danym wyrazeniu są poprawnie użyte
    Input:
        wyrazenie(str)-wyrażenie arytmetyczne, które chcemy sprawdzić
    Output:
        True or False w zależnosci od poprawności"""
        
    stos = []
    lewe_nawiasy = "([{<"
    prawe_nawiasy = ")]}>"
    for znak in wyrazenie:
        if znak in lewe_nawiasy:
            stos.append(znak)
        elif znak in prawe_nawiasy:
            if len(stos) == 0:
                return False
            ostatni_lewy = stos.pop()
            if lewe_nawiasy.index(ostatni_lewy) != prawe_nawiasy.index(znak):
                return False
            if len(stos) > 0 and lewe_nawiasy.index(stos[-1]) < lewe_nawiasy.index(ostatni_lewy):
                return False
    return len(stos) == 0
    

print(nawiasy("{a[b]c}de(") )  # False, ostatni element to (, który nie został domknięty 
print(nawiasy("2{[3}]"))       # False, zła kolejność {[}]
print(nawiasy("(2{(((3)))})")) # False, wewnątrz () jest kolejny (),nie ma zmian na inny rodzaj nawiasów
print(nawiasy("(2+32(3+(5*(4-(4(3)))))"))   # False, same nawiasy ()
print(nawiasy("3434-<2{32[3*54(43-44)]}>")) # True
print(nawiasy("2[(9-4)3+(-2+2)]"))          # True
