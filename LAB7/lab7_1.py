class UserAccount:
    def __init__(self, username, email, password):
        self.username = username #имя пользователя
        self.email = email #электронная почта
        self.__password = password #приватный атрибут для пароля

    def set_password(self, new_password):
        """Метод для безопасного изменения пароля"""
        self.__password = new_password
        print("Пароль был изменён.")

    def check_password(self, password):
        """Метод для проверки пароля"""
        return self.__password == password

username = input("Введите имя пользователя: ")
email = input("Введите электронную почту: ")
password = input("Введите пароль: ")

#объект класса UserAccount
user1 = UserAccount(username, email, password)

new_password = input("Введите новый пароль: ")
user1.set_password(new_password)

check_password = input("Введите пароль для проверки: ")
if user1.check_password(check_password):
    print("Пароль верный!")
else:
    print("Пароль неверный.")
