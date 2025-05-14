def topla(a,b):
    return a + b

def carp(a,b):
    return a*b

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    sonuc = 1
    for i in range(2, n+1):
        sonuc *= i
    return sonuc
