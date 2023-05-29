import mysql.connector
from termcolor import colored, cprint

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="solyankaDB"
)


# users_id = 0

def register_user(Name_User,Login, password):
  cursor = mydb.cursor()
  query = "INSERT INTO Users (Name_User,Role_User,Login, Pass) VALUES (%s,2, %s, %s)"
  values = (Name_User,Login, password)
  cursor.execute(query, values)
  mydb.commit()


def check_login(username, password):
    cursor = mydb.cursor()
    query = "SELECT Id_Users FROM Users WHERE Login = %s AND Pass = %s"
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Проверка, найдена ли запись с заданными логином и паролем
    if result:
        # users_id = result 
        mydb.commit()
        return "True"
    else:
        return "False"
    
def get_orders(users_id):
    cursor = mydb.cursor()
    query = "SELECT Dish.Name_Ingridient FROM Dish JOIN Cart ON Cart.Dish_Id = Dish.Id_Dish where Users_Id  = %d"
    values = (users_id)
    cursor.execute(query,values)
    result = cursor.fetchall()
    print(result)
    mydb.commit()


print("Выберите действие:  ")
print(colored("\t 1 - Регистрация",'red',attrs=['bold']))
print(colored ("\t 2 - Авторизация",'red',attrs=['bold']))
ChooseAction = input()

if ChooseAction == "1":
    print(colored ("Регистрация",'red',attrs=['bold']))
    NameUser = input("Введите Имя пользователя: ")
    loginUser = input("\t Введите Логин: ")
    PassUser = input("\t Введите Пароль: ")
    register_user(NameUser,loginUser,PassUser)

elif ChooseAction == "2":
    print(colored ("Авторизация",'red',attrs=['bold']))
    loginUser = input("\t Введите Логин: ")
    PassUser = input("\t Введите Пароль: ")
    if check_login(loginUser, PassUser):
        print(colored ("Авторизация успешна",'green',attrs=['bold']))
        print("Выберите действие: ")
        print("1 - Сбор блюда")
        print("2 - Корзина и баланс")
        print("3 - тд тп")
        print("4 - тдп тп")
        a = input()
        if a == "1":
            print("Пока что ничего")
        elif a == "2":
             users_id = 2 
             get_orders(users_id);
             print("Пока что ничего")
    else:
        print("Неверный логин или пароль.")