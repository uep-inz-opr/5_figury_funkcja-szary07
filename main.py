from cmath import pi
import math

liczba_figur = int(input())
tablica_liczb = []

def liczenie_pol():
    baza_pol = []
    for x in range(liczba_figur):
        x = map(float, input().split())
        liczby = list(x)
        
        y = len(liczby)
        if y == 1:
            pole_kola = pi*liczby[0]*liczby[0]
            #print(pole_kola)
            baza_pol.append(pole_kola)
        elif y == 2:
            pole_prostokata = liczby[0]*liczby[1]
            #print(pole_prostokata)
            baza_pol.append(pole_prostokata)
        elif y == 3:
            polowa_obwodu = (liczby[0]+liczby[1]+liczby[2])/2
            
            pole_trojkata = math.sqrt(polowa_obwodu*(polowa_obwodu-liczby[0])*(polowa_obwodu-liczby[1])*(polowa_obwodu-liczby[2]))
            #print(pole_trojkata)

            baza_pol.append(pole_trojkata)
        elif y>=4:
            komunikat = ("Błąd: można podać maksymalnie 3 liczby")
            return (komunikat)
            break 
        
        #print(liczby)
    suma_pol = sum(baza_pol)
    #print("baza", baza_pol)
    totalna_suma = round(suma_pol,2)
    print(totalna_suma)
    
        #print(y)
    #print("Suma pol kola", suma_pol_kola)
    #suma_pol = pole_kola+pole_prostokata+pole_trojkata
    #print(suma_pol)
        


liczenie_pol()