
# 1) Вычислить площадь трапеции по известным сторонам и высоте; Реализовать класс для вычисления площади трапеции

class Trapezoid:
    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height

    def area(self):
        return (self.a + self.b) * self.height / 2
    
trapezoid = Trapezoid(3, 4, 5)
print('Площадь трапеции:', trapezoid.area())