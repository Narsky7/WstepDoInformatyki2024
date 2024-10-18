import random

def treeMaker(x):
    for i in range(x):
 
        n = 0
        leaf = ''
        s = 0

        #stworzenie przestrzeni dla symetrii
        while s < x - i :
            leaf += " "
            s += 1

        #tworzy galezie choinki i randomowo (10% szans) zawiesza bombke
        while n < 2*i + 1:
            if random.random() < 0.9:
                leaf += '*'
            else:
                leaf +='o'

            n += 1
        
        #zamienia szczyt choinki na gwiazdke
        if len(leaf) == x + 1 :
            leaf = leaf[:-1]
            leaf +='X'
        print(leaf)

    #tworzy pien i umiejscawia go na srodku
    cone = ""
    for l in range(x):
        cone += " "

    cone +="U"
    print(cone)

#przypadki testowe
treeMaker(1)      
treeMaker(2)      
treeMaker(3)      
treeMaker(5)      
treeMaker(7)      
treeMaker(10)      