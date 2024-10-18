#NWD 3 liczb a,b,c można obliczyc jakos NWD(NWD(a,b),c)

def najwiekszyWspolnyDzielnikoinator(a,b):
    iloraz = 0
    reszta = 0
    while a%b != 0:
        # print(a,b,a%b,)
        reszta = a%b
        a = b
        b = reszta
    return b    


def najwiekszyWspolnyTrzechLiczbDzielnikoinator(a,b,c):
    d = najwiekszyWspolnyDzielnikoinator(a,b)
    return najwiekszyWspolnyDzielnikoinator(d,c)


#testy    
print(najwiekszyWspolnyTrzechLiczbDzielnikoinator(12,16,24)) # 4
print(najwiekszyWspolnyTrzechLiczbDzielnikoinator(30,45,60)) # 15
print(najwiekszyWspolnyTrzechLiczbDzielnikoinator(36,54,90)) # 18
print(najwiekszyWspolnyTrzechLiczbDzielnikoinator(42,70,98)) # 14
