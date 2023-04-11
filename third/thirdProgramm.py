import firebase_admin
from firebase_admin import credentials, auth

# initialize Firebase app with credentials
cred = credentials.Certificate("/Users/ivan/Documents/PythonTest/third/pythonproject-35b85-firebase-adminsdk-4yyrf-f41a51cf95.json")
firebase_admin.initialize_app(cred)

def register_user(email, password):
    try:
        # create new user with email and password
        user = auth.create_user(email=email, password=password)

        # print success message and return user uid
        print("Успешная регистрация пользвоателя:", user.uid)
        return user.uid

    except auth.EmailAlreadyExistsError:
        print("Почта уже зарегистрирована")
        return None

    except Exception as e:
        print("Ошибка регистрации:", e)
        return None
    
print("Выберите действие:  ")
print("\t 1 - Регистрация")
print("\t 2 - Авторизация")
ChooseAction = input()

if ChooseAction == "1":
    email_User = input("Введите email: ")
    password_User = input("Введите пароль: ")
    uid = register_user(email_User, password_User)
    if uid:
        print("New user UID:", uid)
    else:
        print("Registration failed.")

elif ChooseAction == "2":
    email = input("Введите email: ")
    password = input("Введите пароль: ")
    try:
        # authenticate user with email and password
        user = auth.get_user_by_email(email)
        auth_user = auth.authenticate_user(email=email, password=password)
        if auth_user:
            print("Авторизация успешна")
            # do something after successful authentication
        else:
            print("Неверный email или пароль")
    except auth.InvalidIdTokenError:
        print("Недействительный токен")
    except auth.UserNotFoundError:
        print("Пользователь не найден")
    # except auth.WrongPasswordError:
    #     print("Неверный пароль")
    except Exception as e:
        print("Ошибка авторизации:", e)
    
