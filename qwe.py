import mysql.connector
from random import randint

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="Solynka"
)

def get_store():
    cursor = mydb.cursor()
    query = "select * from store"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def get_users_card(users_id):
    cursor = mydb.cursor()
    query = "select debute_user from user_tb where Id_user = %s"
    values = (users_id)
    cursor.execute(query,values)
    result = cursor.fetchone()[0]
    mydb.commit()
    return result

def get_users_data(users_id):
    cursor = mydb.cursor()
    query = "select balance_user from user_tb where Id_user = %s"
    values = (users_id)
    cursor.execute(query,values)
    result = cursor.fetchone()[0]
    print("На балансе: " + str(result))
    mydb.commit()
    return result

def get_data_for_admin(users_number):
    cursor = mydb.cursor()
    query = "select Id_user from user_tb where phone_user = %s"
    values = (str(users_number))
    cursor.execute(query,values)
    ids = cursor.fetchone()
    print("На балансе: " + str(result))
    mydb.commit()
    cursor = mydb.cursor()
    query = "select * from order_tb where user_id = %s"
    values = (ids)
    cursor.execute(query,values)
    result = cursor.fetchall()
    print("1 - лук, 2 - огурцы, 3 - томаты, 4 - сосиски, 5 -  перец, 6 - Мясо копченое, 7 - Колбаса: " + result)
    mydb.commit()

def create_order(prod_list,price,users_id,count):
    cursor = mydb.cursor()
    query = "insert into order_tb(ingredients_order,price_order,count_order,user_id)VALUES (%s,%s,%s,%s)"
    values = (prod_list,price,count,users_id[0])
    cursor.execute(query,values)
    print("Ваш заказ: " + prod_list+ str(price) +" "+ str(count))
    mydb.commit()

def get_orders(users_id):
    cursor = mydb.cursor()
    query = "select * from order_tb where user_id = %s"
    values = (users_id)
    cursor.execute(query,values)
    result = cursor.fetchall()
    print(result)
    mydb.commit()

def admins_menu(users_id):
    admin=True
    while(admin):
        balance = get_users_data(users_id)
        print("Меню админа")
        print("Выберите действие: 1 - Склад,  2 - История покупок, q - Выход")
        choose = input()
        if(choose=="1"):
            print("Склад")
            data = get_store()
            print("Лука = " + str(data[1]))
            print("Огурцов = " + str(data[2]))
            print("Томатов = " + str(data[3]))
            print("Сосисок = " + str(data[4]))
            print("Перца = " + str(data[5]))
            print("Копченого мяса = " + str(data[6]))
            print("Колбасы = " + str(data[7]))
            chose = input("Cделать закупку? y/n")
            if(chose == "y"):
                price = 0
                onecount = int(input("Сколько закупить лука? - "))
                price+=20*onecount
                twocount = int(input("Сколько закупить огурцов? - "))
                price+=25*twocount
                threecount = int(input("Сколько закупить томатов? - "))
                price+=25*threecount
                fourcount = int(input("Сколько закупить сосисок? - "))
                price+=25*fourcount
                fivecount = int(input("Сколько закупить перца? - "))
                price+=20*fivecount
                sixcount = int(input("Сколько закупить копченого мяса? - "))
                price+=25*sixcount
                sevencount = int(input("Сколько закупить колбасы? - "))
                price+=20*sevencount
                onecount+=data[1]
                twocount+=data[2]
                threecount+=data[3]
                fourcount+=data[4]
                fivecount+=data[5]
                sixcount+=data[6]
                sevencount+=data[7]
                print("Общая сумма закупки = " + str(price))
                yn = input("Продолжить? y/n")
                if(yn == "y"):
                    cursor = mydb.cursor()
                    query = "update store set count_one = %s, count_two = %s, count_three = %s, count_four = %s, count_five = %s, count_six = %s, count_seven = %s where Id_store = 1"
                    values = (onecount,twocount,threecount,fourcount,fivecount,sixcount,sevencount)
                    cursor.execute(query,values)
                    mydb.commit()
                    balance = float(balance) - float(price)
                    cursor = mydb.cursor()
                    query = "update user_tb set balance_user = %s where Id_user = %s"
                    values = (str(balance),users_id[0])
                    cursor.execute(query,values)
                    mydb.commit()


        elif(choose=="2"):
            cursor = mydb.cursor()
            query = "select * from user_tb"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            phone= input("Введите номер пользователя")
            get_data_for_admin(phone)
        elif(choose=="q"):
            admin=False
        else:
            print("Неверный ввод данных")

def users_menu(users_id):
    user = True
    while(user):
        balance = get_users_data(users_id)
        discont = get_users_card(users_id)
        if(float(discont) < 5000):
            print("У вас нет карты лояльности")
        elif(float(discont) >= 5000 and float(discont)<15000):
            print("У вас бронзовая карта лояльности")
        elif(float(discont) >= 15000 and float(discont)<25000):
            print("У вас серебряная карта лояльности")
        elif(float(discont) >= 25000):
            print("У вас золотая карта лояльности")
        
        print("Меню пользователя")
        print("Выберите действие: 1 - Сделать заказ,  2 - Смотреть историю покупок, q - Выход")
        choose = input()
        if(choose == "1"):
            price = 100
            prod_list = ""
            print("Просто выберите ингредиенты для вашей пиццы")
            order=True
            one= True
            two= True
            three= True
            four= True
            five= True
            six= True
            seven = True
            data = get_store()
            onecount = data[1]
            twocount = data[2]
            threecount = data[3]
            fourcount = data[4]
            fivecount = data[5]
            sixcount=data[6]
            sevencount = data[7]
            while(order):
                print("1 - лук, 2 - огурцы, 3 - томаты, 4 - сосиски, 5 -  перец, 6 - Мясо копченое, 7 - Колбаса, cl - очистка списка, 0 - закончить добавление ингредиентов")
                products = input()
                if(products == "1" and one):
                    if(onecount>0):
                        one=False
                        prod_list+="-лук"
                        price+=23
                        onecount-=1
                        print(prod_list)
                    else:
                        print("Данный ингредиент закончился")
                        print(prod_list)
                elif(products=="2" and two):
                    if(twocount>0):
                        two=False
                        prod_list+="-огурцы"
                        price+=27
                        twocount-=1
                        print(prod_list)
                    else:
                        print("Данный ингредиент закончился")
                        print(prod_list)
                elif(products=="3" and three):
                    if(threecount>0):
                        three=False
                        prod_list+="-томаты"
                        price+=20
                        threecount-=1
                        print(prod_list)
                    else:
                        print("Данный ингредиент закончился")
                        print(prod_list)
                elif(products=="4" and four):
                    if(fourcount>0):
                        four=False
                        prod_list+="-сосиски"
                        price+=26
                        fourcount-=1
                        print(prod_list)
                    else:
                        print("Данный ингредиент закончился")
                        print(prod_list)
                elif(products=="5" and five):
                    if(fivecount>0):
                        five=False
                        prod_list+="-Перец"
                        price+=20
                        fivecount-=1
                        print(prod_list)
                    else:
                        print("Данный ингредиент закончился")
                        print(prod_list)
                elif(products=="6" and six):
                    if(sixcount>0):
                        six=False
                        prod_list+="-Мясо копченое"
                        price+=28
                        sixcount-=1
                        print(prod_list)
                elif(products=="7" and seven):
                    if(sevencount>0):
                        seven=False
                        prod_list+="-Колбаса"
                        price+=28
                        print(prod_list)
                    else:
                        print("Данный ингредиент закончился")
                        print(prod_list)
                elif(products=="0"):
                    order=False
                elif(products=="cl"):
                    one=True
                    two=True
                    three=True
                    four=True
                    five=True
                    six=True
                    seven=True
                    prod_list = ""
                    price=0
                    onecount = data[1]
                    twocount = data[2]
                    threecount = data[3]
                    fourcount = data[4]
                    fivecount = data[5]
                    sixcount=data[6]
                    sevencount = data[7]
                else:
                    print("Продукт уже добавлен/Неизвесная команда")
            count = int(input("Введите желаемое колическтво: "))
            if(count>=5):
                price=price*count-(price/100*15)
            else:
                price=price*count

            rnd=randint(1,6)

            if(rnd == 5):
                prod_list+="-таракан"
                price=price/100*30

            if(float(discont) >= 5000 and float(discont)<15000):
                price=price/100*5
            elif(float(discont) >= 15000 and float(discont)<25000):
                price=price/100*10
            elif(float(discont) >= 25000):
                price=price/100*20
            
            print("Ингридиенты " +prod_list+ " Количество блюд-"+str(count)+" Цена-" + str(price))
            yn = input("Оформить заказ? y/n: ")
            if(yn=="y"):
                balance = float(balance) - float(price)
                cursor = mydb.cursor()
                query = "select balance_user from user_tb where Id_user = 1"
                cursor.execute(query)
                admin_balance = cursor.fetchone()[0]
                cursor = mydb.cursor()
                query = "update user_tb set balance_user = %s, debute_user = %s where Id_user = %s"
                values = (str(balance),str(price),users_id[0])
                cursor.execute(query,values)
                mydb.commit()
                newBalance = float(price) + float(admin_balance)
                cursor = mydb.cursor()
                query = "update user_tb set balance_user = %s where Id_user = %s"
                usersss=1
                values = (str(newBalance), usersss)
                cursor.execute(query,values)
                mydb.commit()
                create_order(prod_list,price,users_id,count)
                print("Ингридиенты " +prod_list+ " Количество блюд-"+str(count)+" Цена-" + str(price))

                cursor = mydb.cursor()
                query = "update store set count_one = %s, count_two = %s, count_three = %s, count_four = %s, count_five = %s, count_six = %s, count_seven = %s where Id_store = 1"
                values = (onecount,twocount,threecount,fourcount,fivecount,sixcount,sevencount)
                cursor.execute(query,values)
                mydb.commit()
            elif(yn=="n"):
                print("Заказ отменён")
            else:
                print("Неверный ввод данных")
                print("Заказ отменён")
        elif(choose == "2"):
            get_orders(users_id)
        elif(choose == "q"):
            user=False
        else:
            print("Неверный ввод данных")

            
def registration(name,login, password, phone):
    cursor = mydb.cursor()
    query = "insert into user_tb(name_user,login_user,password_user,phone_user,role_user,balance_user,debute_user)VALUES (%s,%s,%s,%s,'user','30000','0')"
    values = (name,login,password,phone)
    cursor.execute(query,values)
    mydb.commit()

def authorization(login,password):
    cursor = mydb.cursor()
    query = "select Id_user from user_tb where login_user = %s and password_user = %s"
    values = (login,password)
    cursor.execute(query,values)
    result = cursor.fetchone()
    if result:
        query = "select role_user from user_tb where Id_user = %s"
        values = (result)
        cursor.execute(query,values)
        role = cursor.fetchone()[0]
        if(role == "user"):
            users_menu(result)
            mydb.commit()
        elif(role == "admin"):
            admins_menu(result)
        else:
            print("Что-то пошло не так")
    else:
        print("Неверный логин или пароль")
        mydb.commit()


while(True):
    print("Выберите действие: 1 - Авторизация, 2 - Регистрация")
    choose = input()
    if(choose == "1"):
        print("Авторизация")
        login = input("Введите лонин: ")
        password = input("Введите пароль: ")
        authorization(login,password)
    elif(choose == "2"):
        print("Регистрация")
        name = input("Введите имя: ")
        login = input("Введите логин: ")
        check=True
        while(check):
            password = input("Введите пароль: ")
            if(len(password)>=8):
                check=False
            else:
                print("Пароль должен содержать не менее восьми символов")
        phone = input("Введите номер телефона: ")

        registration(name,login,password,phone) 
    else:
        print("Неверный ввод данных")