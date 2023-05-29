import mysql.connector
from random import randint

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="Pizza"
)

def get_store():
    cursor = mydb.cursor()
    query = "select * from store"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

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
    print("1 - лук, 2 - огурцы, 3 - томаты, 4 - баклажаны, 5 - охотничьи колбаски, 6 - сыр, 7 - пепперони: " + result)
    mydb.commit()

def create_order(prod_list,price,users_id,count):
    cursor = mydb.cursor()
    query = "insert into order_tb(ingredients_order,price_order,count_order,user_id)VALUES (%s,%s,%s,%s)"
    values = (prod_list,price,count,users_id[0])
    cursor.execute(query,values)
    print("Ваш заказ: " + prod_list+ price +" "+ count)
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
        print("Выберите действие: 1 - На склад,  2 - Смотреть историю покупок, q - Выход")
        choose = input()
        if(choose=="1"):
            print("Склад")
            get_store()
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
        if(int(discont) < 5000):
            print("У вас нет карты лояльности")
        elif(int(discont) >= 5000 and int(discont)<15000):
            print("У вас бронзовая карта лояльности")
        elif(int(discont) >= 15000 and int(discont)<25000):
            print("У вас серебряная карта лояльности")
        elif(int(discont) >= 25000):
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
            while(order):
                print("1 - лук, 2 - огурцы, 3 - томаты, 4 - баклажаны, 5 - охотничьи колбаски, 6 - сыр, 7 - пепперони, cl - очистка списка, 0 - закончить добавление ингредиентов")
                products = input()
                if(products == "1" and one):
                    one=False
                    prod_list+="-лук"
                    price+=43
                    print(prod_list)
                elif(products=="2" and two):
                    two=False
                    prod_list+="-огурцы"
                    price+=47
                    print(prod_list)
                elif(products=="3" and three):
                    three=False
                    prod_list+="-томаты"
                    price+=50
                    print(prod_list)
                elif(products=="4" and four):
                    four=False
                    prod_list+="-баклажаны"
                    price+=56
                    print(prod_list)
                elif(products=="5" and five):
                    five=False
                    prod_list+="-охотничьи_колбаски"
                    price+=60
                    print(prod_list)
                elif(products=="6" and six):
                    six=False
                    prod_list+="-сыр"
                    price+=48
                    print(prod_list)
                elif(products=="7" and seven):
                    seven=False
                    prod_list+="-пепперони"
                    price+=78
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