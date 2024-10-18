try:
    lb1 = float(input('pierwsza liczba: '))
    lb2 = float(input('druga liczba: '))
except ValueError:
    print('Upewnij się że wpisałeś poprawną liczbę')
    print('koniec programu')
    exit()
#d.

if lb1 < 0 and lb2 < 0 :
    print('koniec programu')
       
else:
    #e.
    if lb1 < 0:
        lb1 = lb1 * (-1) 
    if lb2 < 0:
        lb2 = lb2 * (-1)    
    #a.

    print(f"Suma: {lb1 + lb2}")
    print(f"Różnica: {lb1 - lb2}")
    print(f"Iloczyn: {lb1 * lb2}")
    print(f"Iloraz: {lb1 / lb2}")
    print(f"Kwadrat: {lb1**2} oraz {lb2**2}")
    print(f"Pierwiastek Kwadratowy: {lb1**(1/2) } oraz { lb2**(1/2)}")

    #f.
    if (lb1 * lb2) == 10:
        print("YAY")

'''
b.
'''