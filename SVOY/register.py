class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == "__main__":
    database = Database()
    while True:
        choice = int(input("Привет, выбери действие: \n1 - Вход\n2 - регистрация\n"))
        if choice == 1:
            login = input("введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"ВОШЕЛ, {login}")
                    break
                else:
                    print("пароль не верен")
            else:
                print("пользователь не найден")
        if choice == 2:
            user = User(
                input("введите логин: "),
                password := input("введите пароль: "),
                password2 := input("повторите пароль: "),
            )
            if password == password2:
                print("регистрация завершена")
            if password != password2:
                print("пароли не совпадают, попробуйте еще")
                continue
            database.add_user(user.username, user.password)
