from math import * 

print("Ruudu karakteristikud")
a=float(input(" Sisesta ruudu k�lje pikkus => ")) #panin folat ja sulgudes
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu �mberm��t", P)
di=a*sqrt(2) #eemaldatud math
print("Ruudu diagonaal", round(di, 2))
print()
print("Ristk�liku karakteristikud") #eemaldati �ks sulg
b=float(input("Sisesta ristk�liku 1. k�lje pikkus => ")) #panin input ja sulgud
c=float(input("Sisesta ristk�liku 2. k�lje pikkus => ")) #panin input ja sulgud
S=b*c
print("Ristk�liku pindala", S) 
print("Ristk�liku pindala", S) eemaldasin jutum�rk
P=2*(b+c)
print("Ristk�liku �mberm��t", P)
di=sqrt(b*2+c*2) eemaldasin math
print("Ristk�liku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
r=float(input ('Sisesta ringi raadiusi pikkus => ` ')) #float
d=2*r #kordamine
print("Ringi l�bim��t" ,d) #koma
S=pi*r**2 #kordamine
print("Ringi pindala", round(S, 2)) #kaks
C=2*pi*r #eemaldasin sulgused
print("Ringjoone pikkus", round(C, 2)) #kaks
