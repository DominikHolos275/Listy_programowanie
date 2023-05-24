import random
import string
""" funkcja password(x, znaki) tworzy hasło o okreslonej długości i z określonych znaków
    Input:
        x(int)-liczba znaków pożadanego hasła
        znaki(str)-rodzaje znaków które mogą zostać zawarte w hasle
    Output:
        wygenerowane hasło"""
def password(x, znaki):
    password = ''
    for i in range(x):
        password += random.choice(znaki)
    return password
    
znaki = string.ascii_letters + string.digits + string.punctuation
znaki2 = string.ascii_letters + string.digits 
znaki3 = string.ascii_letters + string.digits + "?!@#$%"

print(password(12, znaki), "\n", password(12, znaki2), "\n", password(12, znaki3))