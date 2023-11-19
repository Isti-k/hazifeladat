import random
import math

# 1.feladat:
#Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!

def feladat1():
    oszthato = 0

    for szam in range(1, 1001):
        if szam % 7 == 0:
            oszthato += 1

    print("7-tel osztható számok száma:",oszthato)

#2.feladat:
#Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!

def feladat2():
    oszthato = 0

    for szam in range(2000, 20001):
        if szam % 12 == 0:
            oszthato += 1

    print("12-vel osztható számok száma:",oszthato)


#3. feladat:
#Írd ki az első 20 3-mal osztható szám négyzetének összegét!

def feladat3():
    osszeg = 0

    for i in range(1, 21):
        szam = i * 3
        negyzet = szam ** 2
        osszeg += negyzet

    print("A 3-mal osztható szám négyzetének összege:",osszeg)

#4. feladat:
#Keresd meg egy szám egész osztóit!

def feladat4(szam:int):
    osztoi = []
    
    for i in range(1, szam + 1):
        if szam % i == 0:
            osztoi.append(i)
    
    return osztoi

#5. feladat:
#Keresd meg egy szám legnagyobb egész osztóját!

def feladat5(szam:int):
    legnagyobb = 1
    
    for i in range(2, szam + 1):
        if szam % i == 0:
            legnagyobb = i
    
    return legnagyobb

#6. feladat:
#6Vizsgáljuk meg, hogy egy adott szám prímszám-e!

'''def feladat6(szam:int):
    if szam < 2:
    for i in range(2, int(szam**0.5) + 1):
        if szam % i == 0:
    
    return''' #nem sikerült megoldani!

#7. feladat:
#Számold meg, hogy hány négyzetszám van 0-100000 között!

def feladat7():
    szam = 0

    for i in range(101):
        if i**2 <= 100000:
            szam += 1

    print("A négyzetszámok száma:",szam)

#8. feladat:
#Számold meg, hogy hány négyzetszám van 10000-100000 között!

def feladat8():
    szam = 0

    for i in range(10001):
        if i**2 <= 100000:
            szam += 1

    print("A négyzetszámok száma:",szam)

#9. feladat:
#Add össze, hogy mennyi a 0-10000 közötti négyzetszámok összege!

def feladat9():
    i = 0
    szam = 0

    while i <= 100:
        szam += i**2
        i += 1

    print("A négyzetszámok összege:",szam)


