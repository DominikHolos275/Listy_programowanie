from scipy.integrate import odeint
import numpy as np
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
    t_max = 100
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