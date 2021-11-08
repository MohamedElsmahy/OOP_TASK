import re

class Person:
    moods = ('happy', 'tired', 'lazy')

    def __init__(self, name, money, mood='tired', healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self.__health_Rate

    @healthRate.setter
    def healthRate(self, healthRate):
        if healthRate < 0:
            self.__health_Rate = 0
        elif healthRate >= 100:
            self.__health_Rate = 100
        else:
            self.__health_Rate = healthRate

    def Sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        elif hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def Eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def Buy(self, items):
        # items = int(items)
        for i in range(items):
            self.money = self.money - 10


class Employee(Person):
    def __init__(self, id, car, email, salary, distancToWork, name, money):
        super().__init__(name, money)
        self.id = id
        self.car = Car(car, fuelRate=100, velocity=100)
        self.email = email
        self.salary = salary
        self.distancToWork = distancToWork

    ##salary property
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if abs(salary) < 1000:
            self.__salary = 1000

    ##email property
    @property
    def email(self):
        return self.__email
        # re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", self.email)

    @email.setter
    def email(self, email):
        self.__email = email
        email_pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        self.__email = re.match(email_pattern, self.__email)

    def Work(self, hours):
        if hours == 8:
            print('happy')
        elif hours < 8:
            print('tired')
        else:
            print('lazy')

    def Drive(self, distance):
        Car.Run()
        self.distancToWork = distance

    def Refuel(self, gasAmount):
        self.car.fuelRate += gasAmount

    def SendEmail(self, to, subject, msg, reciver_name):
        try:
            email_file = open("email.txt", "a")
        except:
            print("file not found")
        else:
            email_file.write(
                f'to : {to}\nsubject : {subject}\nmsg : {msg}\nreciver name : {reciver_name}\n__________________\n')


class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def Hire(self):
        pass

    def Fire(self):
        pass

    def calculate_lateness(self):
        pass

    def Deduct(self):
        pass

    def Reward(self):
        pass


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelRate):
        if fuelRate < 0:
            self.__fuelRate = 0
        elif fuelRate > 100:
            self.__fuelRate = 100
        else:
            self.__fuelRate = fuelRate

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity < 0:
            self.__velocity = 0
        elif velocity > 100:
            self.__velocity = 100
        else:
            self.__velocity = velocity

    def Run(self, distance, velocity):
        fuel_rate = self.fuelRate
        self.velocity = velocity
        self.fuelRate = self.fuelRate - distance
        if self.fuelRate == 0:
            distance = distance - fuel_rate
        self.Stop(distance)

    def Stop(self, distance):
        self.velocity = 0
        if distance == 0:
            print("you are arrived")
        else:
            print(f'remainig {distance} kilometer to arrive your destination')


man = Person('samy', 2000, 'tired', 500)
# man = moods(0)
# man.Eat(2)
# print(man.healthRate)
# man.Buy(5)
# print(man.money)

emp = Employee(1, 'BMW', 'mohamed@gmail.com', 200, 40, 'mohamed', 5000)
# emp.SendEmail('mohamed@gmail.com', 'hello', 'hi mohamed', 'mohamed')
# print(emp.salary)
# print(emp.email)

car1 = Car('KIA', 50, 80)
# car1.Run(50, 80)