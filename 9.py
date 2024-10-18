def wplata():
    global saldo

    try:
        kwotaWplaty = int(input('Ile chcesz wpłacić: '))
    except ValueError:
        print('bledny numer')
        wyborZadania()

    saldo += kwotaWplaty
    wyborZadania()


def wyplata():
    global saldo

    try:
        kwotaWyplaty = int(input('Ile chcesz wypłacić: '))
    except ValueError:
        print('bledny numer')
        wyborZadania()

    if kwotaWyplaty > saldo :
        print('nie masz tyle pieniędzy')      
    else: saldo -= kwotaWyplaty  

    wyborZadania()

def saldoSprawdzenie():
    
    print(f'Twoje saldo to {saldo}')
    wyborZadania()

def wyborZadania():
    
    try:
        operacja = int(input('Co chcesz teraz zrobić? \n 1. wpłacić pieniądze \n 2. wypłacić pieniądze \n 3. sprawdzić saldo \n 4. zakończyć program \n'))    
        if operacja == 4 : exit()  
        pin = int(input('podaj swój czterocyfrowy PIN: '))
    except ValueError:
        print('Zły PIN lub nieprawidłowa operacja')    
        wyborZadania()


    if pin == true_pin:
        if operacja == 1 : wplata()       
        elif operacja == 2 : wyplata()       
        elif operacja == 3 : saldoSprawdzenie()       
        else : 
            print("nieprawidłowa operacja")   
            wyborZadania()    

    else:
        print("zly PIN")
        wyborZadania()


saldo = 0
true_pin = 2304        

wyborZadania()