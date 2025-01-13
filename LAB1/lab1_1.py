#ввод числа
number = int(input("Введите число: "))

if number > 0:
#от 1 до введенного числа
    for i in range(1, number + 1):
        print(i)
else:
    print("Пожалуйста, введите положительное число")
