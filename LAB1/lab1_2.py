num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num1 > num2:
    print(f"Большее число: {num1}")
elif num2 > num1:
    print(f"Большее число: {num2}")
else:
    print("Оба числа равны.")
