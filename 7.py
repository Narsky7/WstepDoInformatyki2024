try:
    a = int(input("Początek zakresu: "))
    b = int(input("Koniec zakresu: "))
except ValueError:
    print("Należy wpisać liczby całkowite")
    exit()


if b < a :
    print('błędny zakres')
    exit()

if b - a >= 19:
    #d

    num = (b - a + 1)/2 - 3
    for i in range(7):
        if num + 3 == num + i :
            pass
        else:      
            print(int(num+ i))

else: 
    n=0
    while n <= b - a:
        print(a+n)  
        n += 1
        
    