from math import * 

print("Ruudu karakteristikud")
a=float(input(" Sisesta ruudu külje pikkus => ")) #panin folat ja sulgudes
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) #eemaldatud math
print("Ruudu diagonaal", round(di, 2))
print()
print("Ristküliku karakteristikud") #eemaldati üks sulg
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #panin input ja sulgud
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #panin input ja sulgud
S=b*c
print("Ristküliku pindala", S) 
print("Ristküliku pindala", S) eemaldasin jutumärk
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b*2+c*2) eemaldasin math
print("Ristküliku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
r=float(input ('Sisesta ringi raadiusi pikkus => ` ')) #float
d=2*r #kordamine
print("Ringi läbimõõt" ,d) #koma
S=pi*r**2 #kordamine
print("Ringi pindala", round(S, 2)) #kaks
C=2*pi*r #eemaldasin sulgused
print("Ringjoone pikkus", round(C, 2)) #kaks
