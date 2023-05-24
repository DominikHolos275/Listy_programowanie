import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import argparse
import random
#from ZADANIE1_SEIR import SEIR
from ZADANIE1 import SEIR

parser = argparse.ArgumentParser(description='Model SEIR')
parser.add_argument('-S', default=random.uniform(1000, 10000), help='liczba podatnych (susceptible)')
parser.add_argument('-E', default=random.uniform(0, 100), help='liczba narażonych (exposed)')
parser.add_argument('-I', default=random.uniform(0, 100), help='liczba zarażonych (infectious)')
parser.add_argument('-R', default=random.uniform(0, 10), help='liczba wyleczonych (recovered)')
parser.add_argument('-beta', default=random.uniform(1.1, 2.2), help='wskaźnik infekcji')
parser.add_argument('-sigma', default=random.uniform(0, 0.9), help='wskaźnik inkubacji')
parser.add_argument('-gamma', default=random.uniform(0, 0.9), help='wskaźnik wyzdrowień')

args = parser.parse_args()
S, E, I, R, beta, sigma, gamma=int(args.S), int(args.E), int(args.I), int(args.R), float(args.beta), float(args.sigma), float(args.gamma)
N=S+E+I+R

t_max = 100
t = np.linspace(0, t_max, t_max)

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

plt.savefig(("C:\\Users\\dbjd2\\Desktop\\PYTON\\wykresy\\"+f"wykres_zad2_{beta}_{sigma}_{gamma}.jpg"), format="jpg")
