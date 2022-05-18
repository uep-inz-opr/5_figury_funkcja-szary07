from cmath import pi
import math

liczba_figur = int(input())
tablica_liczb = []

def liczenie_pol():
    
    for x in range(liczba_figur):
        x = map(int, input().split())
        liczby = list(x)
        

        y = len(liczby)
        if y == 1:
            pole_kola = pi*liczby[0]*liczby[0]
            print(pole_kola)
            suma_pol_kola.append(pole_kola)
        elif y == 2:
            pole_prostokata = liczby[0]*liczby[1]
            print(pole_prostokata)
        elif y == 3:
            polowa_obwodu = (liczby[0]+liczby[1]+liczby[2])/2
            
            pole_trojkata = math.sqrt(polowa_obwodu*(polowa_obwodu-liczby[0])*(polowa_obwodu-liczby[1])*(polowa_obwodu-liczby[2]))
            print(pole_trojkata)
        elif y>=4:
            return ("Błąd: można podać maksymalnie 3 liczby")
            break 
        
        print(liczby)
        print(y)
print("Suma pol kola", suma_pol_kola)
    #suma_pol = pole_kola+pole_prostokata+pole_trojkata
    #print(suma_pol)
        


liczenie_pol()