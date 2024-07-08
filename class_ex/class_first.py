# class MyClass:
#     def __init__(self, name, id_num, sex, group):
#         self.name = name
#         self.id_num = id_num
#         self.sex = sex
#         self.group = group

#     def __str__(self):
#         msg = "Our class " + f"{self.id_num}" + "rd student is " + self.name
#         return msg
    
#     def print_name(self, nick_name):
#         print(f"우리반 {self.id_num}학생이 {self.name}입니다. His nickname is {nick_name}")
    
#     def print_sex(self):
#         print(f"His sex is {self.sex}")
    
#     def change_num(self):
#         if self.id_num == 2:
#             self.id_num = self.group


# stu1 = MyClass("김민우", 2, "male", 3)

# print("Student name is ", stu1.name)
# print("Number is ", stu1.id_num)

# stu1.change_num()
# stu1.print_name("minu")
# # print(stu1)
# # stu1.print_name("Minu")
# # stu1.print_sex()

# class Calculator:
#     def __init__(self):
#         pass
    
#     def add(self, num1, num2):
#         return num1 + num2
    
#     def subtract(self, num1, num2):
#         return num1 - num2
    
#     def multiply(self, num1, num2):
#         return num1 * num2
    
#     def divide(self, num1, num2):
#         return num1 / num2
    
# cal = Calculator()
# print(cal.add(3, 5))         
# print(cal.subtract(5, 3)) 
# print(cal.multiply(3, 5))
# print(cal.divide(6, 3))

# class Robot:
#     def __init__(self, name, robo_type):
#         self.name = name
#         self.robo_type = robo_type
#         self.result = 0
    
#     def get_description(self):
#         print(f"{self.name}: {self.robo_type}")
    
#     def increase(self, dist):
#         self.result += dist
#         print(f"Drive distance is {self.result} km")
    
    

# my_robot = Robot("Robbi", "agv")
# my_robot.get_description()
# my_robot.increase(10)
# my_robot.increase(5)

# class Father:
#     def __init__(self, surname, given_name):
#         self.surname = surname
#         self.given_name = given_name
    
#     def get_marry(self, ox):
#         if ox:
#             print("Married Man")
#         else:
#             print("Not Married Man")
    
#     def __str__(self):
#         msg = "His name is " + self.surname + self.given_name
#         return msg

# class Son(Father):
#     def __init__(self, surname, given_name, mother):
#         self.mother = mother
#         super().__init__(surname, given_name)
        
# father = Father("Kim", "Minwoo")
# father.get_marry(True)
# print(father)

# myson = Son("Kim", "Lee", "Suzy")
# myson.get_marry(False) 
# print(myson)
# print(myson.mother)

class Employee:
    def __init__(self, name, age, Salary):
        self.name  = name
        self.age = age
        self.Salary = Salary
    
    def increase_pay(self, num1):
        self.Salary = self.Salary * num1

class Developer(Employee):
    def __init__(self, name, age, Salary, strong):
        super().__init__(name, age, Salary)
        self.strong = strong
    
emp1 = Employee("KMW", 24, 5000)
emp2 = Employee("KMH", 26, 8000)
print(emp1.Salary)
print(emp2.Salary)
emp1.increase_pay(1.2)
emp2.increase_pay(1.3)
print(emp1.Salary)
print(emp2.Salary)
dev1 = Developer("JYW", 30, 10000, ["Design", "Python"])
dev1.increase_pay(1.5)
print(dev1.Salary)