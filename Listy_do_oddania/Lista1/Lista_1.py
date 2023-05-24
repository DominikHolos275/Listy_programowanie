import random
import math
class Vector:
    def __init__ (self, size=3):
        """Funkcja inicjująca klasę Vector
        size(int)-wymiar danego wektora (domyslnie 3)
        elementy(list)-wektor zaprezentowany w postaci listy (domyslnie same zera)"""
        self.size=int(size)
        elementy=[]
        for i in range (size):
            elementy.append(0)
        self.elementy=elementy    
        
    def generator(self):
        """Funkcja generująca wektory z losowo wybranymi wartościami z przedziału [-20,20] 
        i dwoma miejscami po porzecinku 
        output:
        self.elementy(list)-wektor z losowo wybranymi wartościami"""
        self.elementy=[]
        for i in range(self.size):
            self.elementy.append(round(random.uniform(-20, 20), 2))   
        return self.elementy
        
    def chage_list(self, x):
        """Funkcja zamieniajaca elementy istniejących już wektorów na podane w formie listy elementy
        input:
        x(list)-nowe wartości wektora
        output:
        self.elementy(list)wektor z nowymi danymi
        Funkcja w razie podania wektorów o innych wymiarach zwróci ValueError "zły wymiar wektora"""
        if self.size!=len(x):
            raise ValueError("zły wymiar wektora")
        self.elementy=x
        return self.elementy
        
    def __add__(self, v2):
        """Funkcja pozwalająca dodawać wektory za pomocą znaku "+" 
        input:
        v2(list)-wektor który chcemy dodać do naszego wektora
        output:
        suma(list)-wektor powstały poprzez dodanie v2
        Funkcja w razie podania wektorów o innych wymiarach zwróci ValueError "zły wymiar wektora" """
        if self.size!=v2.size:
            raise ValueError("zły wymiar wektora")
        suma=[]
        for i in range (self.size):
            suma.append(round(self.elementy[i]+v2.elementy[i],3))
        self.elementy=suma
        return suma
        
    def __sub__(self, v2):
        """Funkcja pozwalająca odejmować macierze za pomocą znaku "-" 
        input:
        v2(list)-wektor który chcemy odjąć do naszego wektora
        output:
        różnica(list)-wektor powstały poprzez odjęcie v2
        Funkcja w razie podania wektorów o innych wymiarach zwróci ValueError "zły wymiar wektora" """
        if self.size!=v2.size:
            raise ValueError("zły wymiar wektora")
        różnica=[]
        for i in range (self.size):
            różnica.append(round(self.elementy[i]-v2.elementy[i],3))
        self.elementy=różnica
        return różnica
        
    def __mul__(self, alfa):
        """Funkcja obliczająca mnożenie wektora przez skalar za pomocą znaku "*" 
        input:
        alfa(int)-skalar przez który mnożymy
        output:
        iloczyn(list)-wektor powstały poprzez przemnożenie wektora przez alfa"""
        iloczyn=[]
        for i in range (self.size):
            iloczyn.append(self.elementy[i]*alfa)
        self.elementy=iloczyn
        return iloczyn
        
    def długość(self):
        """Funkcja obliczająca długość wektora
        output:
        długość(float)-długość wektora"""
        d=0
        for i in range (self.size):
            d+=(self.elementy[i])**2
        długość=math.sqrt(d)
        return długość
        
    def suma_elementów(self):
        """Funkcja obliczająca sumę elementów wektora
        output:
        suma(float)-suma elementów wektora"""
        suma=0
        for i in range (self.size):
            suma+=(self.elementy[i])
        return suma
        
    def ilczyn_skalarny(self, v2):
        """Funkcja obliczająca iloczyn skalarny dwóch wektorów
        input:
        v2(list)-wertor przez który będziemy mnożyć skalarnie
        output:
        iloczyn_sk(float)-wartość iloczynu skalarnego
        Funkcja w razie podania wektorów o innych wymiarach zwróci ValueError "zły wymiar wektora"""
        if self.size!=v2.size:
            raise ValueError("zły wymiar wektora")
        iloczyn_sk=0
        for i in range(self.size):
            iloczyn_sk+=(self.elementy[i]*v2.elementy[i])
        return round(iloczyn_sk,3)
        
    def __getitem__(self, x):
        """Funkcja pozwalająca na dostep do konkretnych elementów wektora (za pomocą[])
        input:
        x(int)-pozycja zajmowana przez pożdany element w rozumieniu pythonowym (0,1,2,3) nie (1,2,3)
        output:
        self.elementy[x](float)-pożądana element znajdujący się na wskazanym przez nas miejscu
        Funkcja w razie podania wektorów o innych wymiarach zwróci ValueError "zły wymiar wektora"""
        if self.size<=x:
            raise ValueError("brak wartości na podanym miejscu wektora")
        return self.elementy[x]
         
    def __contains__(self, x):
        """Funkcja sprawdzajaca przynależność do konkretnego wektora
        input:
        x(float)-sprawdzany element
        output:
        True or False w zależności czy dany element należy do wektora, 
        jeśli tak to zwraca True a jeśli nie to False"""
        return x in self.elementy
        
    def __str__ (self):
        """Funkcja umożliwiajaca reprezentacje tekstową wektora"""
        return str(self.elementy)

