
# 1) Разработайте класс «Услуги», который содержит закрытые свойства: дата, код
# услуги, наименование услуги, цена (руб.) услуги, количество услуг на дату.
# Разработанный класс должен содержать конструктор, а также метод вычисления
# стоимости каждого произведенного вида услуг и вывода исходных данных и результата.
# Напишите программу, которая создает и инициализирует два объекта
# разработанного класса, вычисляет и выводит результат.

class Service:
    
    def __init__(self, date, code, name, price, quantity):
        self.date = date
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f'Дата: {self.date}\nКод услуги: {self.code}\nНаименование услуги: {self.name}\nЦена: {self.price}\nКоличество: {self.quantity}'
    
service = Service('09.01.2025', 123, 'Удаление мозга', 1000000, 1)
service2 = Service('02.03.3213', 124, '+iq', 99999, 1)

print(service)
print(f'Стоимость услуги: {service.calculate_cost()} рублей')

print(service2)
print(f'Стоимость услуги: {service2.calculate_cost()} рублей')