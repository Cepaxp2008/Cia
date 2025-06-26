# Задание 1:
# Создайте класс Rectangle, который будет содержать
# атрибуты width и height и методы area() и perimeter().
# Создайте класс Square, который будет наследовать
# класс Rectangle и содержать только атрибут side (а не
# width и height).

# class Rectangle :
#     def __init__(self , width , height):
#         self.width = width
#         self.height = height
#     def area(self , width , height) :
#         return width * height
#     def perimeter(self , width , height) :
#         return width * 2 + height * 2
# class Square(Rectangle):
#     def __init__(self , side) :
#         self.side = side
#     def area(self , side) :
#         return side ** 2
#     def perimeter(self , side) :
#         return side * 4
# a = Rectangle(2 , 4)
# b = Square(4)
# print("Площадь прямоугольника: ", a.area(a.width , a.height) , "\n"
#       , "Периметр прямоугольника" , a.perimeter(a.width , a.height))
# print("Площадь квадрата" , b.area(b.side) , "\n "
# "Периметр квадрата" , b.perimeter(b.side))

# Задание 2:
# Создайте класс Person, который будет содержать
# атрибуты name, age, gender и метод introduce(), который
# будет выводить на экран информацию о человеке.
# Создайте класс Employee, который будет наследовать
# класс Person и содержать атрибуты salary и position, а
# также метод work(), который будет выводить на экран
# информацию о работе сотрудника.

# class Person :
#     def __init__(self , name , age , gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def introduce(self , name , age , gender) :
#         print("Имя: " , self.name , "Возраст: " , self.age , "пол: " ,
#               self.gender)
# class Employee(Person) :
#     def __init__(self , name , age , gender , salary , position):
#         super().__init__(name , age , gender)
#         self.salary = salary
#         self.position = position
#     def work(self , name , salary , position):
#         print("Имя сотрудника: " , self.name ,
#               "Зарплата сотрудника: " , self.salary ,
#               "позиция в компании: " , self.position)
# a = Person("Bob" , 46 , "мужской")
# b = Employee("Ann" , 29 , "Женский" ,
#              400 , "менеджер")
# a.introduce(a.name , a.age , a.gender)
# b.work(b.name , b.salary , b.position)