import random

def calculator(a,b,symbol): 
    output = 0

    if symbol == "+":
        output = a + b
    elif symbol == "-":
        output = a - b
    elif symbol == "*":
        output = a * b   
    elif symbol == "/":
        if b == 0 :
            output = 'nie można dzielić przez 0'
        else:    
            output = a / b    
    elif symbol == "#":
        if b == 0 :
            output = 'nie ma pierwiastków o stopniu 0'
        else:            
            output = a**(1/b)    
    elif symbol == "^":
        output = a**b
    elif symbol == "x":
        if b < a :
            output = 'błędny zakres'
        else:     
            output = random.randint(a,b)     
    else:
        output = "błędna akcja"

    print(f"Wynik: {output}")

    shouldRepeat = input("Czy chcesz wprowadzić nowe dane? T/N : ")

    if shouldRepeat == 'T' or shouldRepeat =='t':
        gatherInput()
    else:
        exit()

def gatherInput():
    try:
        a = int(input('pierwsza liczba:'))
        b = int(input('druga liczba:'))
        operation = input('wybierz akcje +,-,*,/,#,^,x : ')
    except ValueError:
        print('błąd')
        gatherInput()

    calculator(a,b,operation)   

gatherInput()    