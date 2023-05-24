import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import argparse
import random
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model SEIR')
    parser.add_argument('S', nargs='?', type=int, default=random.uniform(1000, 10000), help='liczba podatnych (susceptible)')
    parser.add_argument('E', nargs='?', type=int, default=random.uniform(0, 100), help='liczba narażonych (exposed)')
    parser.add_argument('I', nargs='?', type=int, default=random.uniform(0, 100), help='liczba zarażonych (infectious)')
    parser.add_argument('R', nargs='?', type=int, default=random.uniform(0, 10), help='liczba wyleczonych (recovered)')
    parser.add_argument('beta', nargs='?', type=float, default=random.uniform(0.1, 2), help='wskaźnik infekcji')
    parser.add_argument('sigma', nargs='?', type=float, default=random.uniform(0.1, 0.9), help='wskaźnik inkubacji')
    parser.add_argument('gamma', nargs='?', type=float, default=random.uniform(0.1, 0.6), help='wskaźnik wyzdrowień')

    args = parser.parse_args()
    S, E, I, R, beta, sigma, gamma=int(args.S), int(args.E), int(args.I), int(args.R), float(args.beta), float(args.sigma), float(args.gamma)
    N=S+E+I+R

    t_max = 150
    t = np.linspace(0, t_max, t_max)

# Rozwiązanie równań różniczkowych metodą Eulera

def SEIR(S, E, I, R, beta, sigma, gamma):
    """Funkcja SEIR rozwiazuje równanie różniczkowe
    input:
        S(int)-liczeba osób podatnych
        E(int)-liczeba osób narażonych
        I(int)-liczba osób zarażonych
        R(int)-liczba osób wyleczonych
        beta(float)-wskaźnik infekcji
        sigma(float)-wskaźnik inkubacji
        gamma(float)-wskaźnik wyzdrowień
    output:
        S_list, E_list, I_list, R_list (list)- listy następnych wartości przyjmowanych przez S E I R 
    """
    N = S + E + I + R
    t_max = 150
    t = np.linspace(0, t_max, t_max)

    def model(y, t):
        S, E, I, R = y
        dSdt = -beta * S * I / N
        dEdt = beta * S * I / N - sigma * E
        dIdt = sigma * E - gamma * I
        dRdt = gamma * I
        return [dSdt, dEdt, dIdt, dRdt]

    y0 = [S, E, I, R]
    result = odeint(model, y0, t)
    
    S_list = result[:, 0]
    E_list = result[:, 1]
    I_list = result[:, 2]
    R_list = result[:, 3]
    
    return S_list, E_list, I_list, R_list


S_list, E_list, I_list, R_list = SEIR(S, E, I, R, beta, sigma, gamma)
# Tworzenie wykresów
fig, ax = plt.subplots()
ax.plot(t, S_list, label='Susceptible')
ax.plot(t, E_list, label='Exposed')
ax.plot(t, I_list, label='Infectious')
ax.plot(t, R_list, label='Recovered')
ax.legend()
ax.set_xlabel('Czas (dni)')
ax.set_ylabel('Liczba ludzi')

plt.savefig(("C:\\Users\\dbjd2\\Desktop\\PYTON\\wykresy\\"+f"wykres_{beta}_{sigma}_{gamma}.jpg"), format="jpg")

#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  999 1 0 0 1.34 0.19 0.34
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  999 1 0 0 0.7 0.19 0.34
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  999 1 0 0 1.34 0.8 0.34
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  999 1 0 0 1.34 0.19 0.05
#plt.show()

#morzemy stworzyc kilka rodzajów przebiegu epidemi np:
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  900 90 5 5 0.5 0.9 0.7
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  900 100 0 0 0.4 0.6 0.8
#w ten sposób uzyskujemy mało zakarzeń i szybki przebieg
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  900 90 5 5 1.2 0.1 0.6
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  900 2 4 2 1.4 0.2 0.3
#w ten sposób uzyskujemy liczbę zakarzeń około połowy liczebności populacji przebieg jej jest dosć lagodny
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  900 90 5 5 1.5 0.8 0.4
#python "C:\Users\dbjd2\Desktop\PYTON\2 Semestr\lista4\końcowa wersja\ZADANIE1.py"  900 54 91 8 1.3 0.7 0.25
#w ten sposób uzyskujemy sporą liczbę zakarzeń przebieg jej jest dosć dynamiczny
