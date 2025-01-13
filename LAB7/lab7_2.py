class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        """Возвращает информацию о транспортном средстве"""
        return f"Марка: {self.make}, Модель: {self.model}"


# Класс наследующий от Vehicle
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        """Возвращает информацию о транспортном средстве, включая тип топлива"""
        base_info = super().get_info()  # Получение информации из базового класса
        return f"{base_info}, Тип топлива: {self.fuel_type}"


vehicle_make = input("Введите марку транспортного средства: ")
vehicle_model = input("Введите модель транспортного средства: ")

#объект базового класса Vehicle
vehicle = Vehicle(vehicle_make, vehicle_model)
print("\nИнформация о транспортном средстве:")
print(vehicle.get_info())

car_make = input("\nВведите марку автомобиля: ")
car_model = input("Введите модель автомобиля: ")
fuel_type = input("Введите тип топлива автомобиля: ")

car = Car(car_make, car_model, fuel_type)
print("\nИнформация о транспортном средстве:")
print(car.get_info())
