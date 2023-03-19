while(True):
    countOperation = int(input("Количество операций: "))
    n1 = float(input("Введите число: "))
    rez=n1
    i=0
    for i in range (countOperation):
        i+=1
        sym = input("Введите знак: ")
        c = float(input("Введите второe число или степень: "))

        if c == 0:
            print("деление на ноль")
            i-=0
        elif sym == '+':
            rez = rez+c
            print(rez)
        elif sym == '-':
            rez = rez-c
            print(rez)
        elif sym == '/':
            rez = rez/c
            print(rez)
        elif sym == '*':
            rez = rez*c
            print(rez)
        elif sym == '^':
            rez = rez**c
            print(rez)
        else:
            print("Error")
    print("Выход из цикла")