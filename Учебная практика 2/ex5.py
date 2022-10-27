# 1) На междугородной АТС информация о разговорах содержит дату разговора, код
# и название города, время разговора, тариф, номер телефона абонента.
# Реализовать класс для хранения информации о разговоре.


class Call:

    def __init__(self, date, code, city, time, tariff, number):
        self.date = date
        self.code = code
        self.city = city
        self.time = time
        self.tariff = tariff
        self.number = number
        
    def calculate_cost(self):
        return self.time * self.tariff

    def __str__(self):
        return f'Дата: {self.date}\nКод: {self.code}\nГород: {self.city}\nВремя: {self.time}\nТариф: {self.tariff}\nНомер: {self.number}'


call = Call('01.01.2020', 123, 'Москва', 10, 10, 1234567890)
print(call)
print(f'Стоимость разговора: {call.calculate_cost()} рублей')