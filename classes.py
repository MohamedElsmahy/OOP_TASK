import re
import json

# class Object:
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__,
#             sort_keys=True, indent=4)

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
        else:
            self.__salary = salary

    ##email property
    @property
    def email(self):
        return self.__email
        # re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", self.email)

    @email.setter
    def email(self, email):
        self.__email = email
        email_pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        newemail = re.search(email_pattern, self.__email)
        return newemail
        # self.__email = self.__email.__dict__


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
    employeesNum = 0
    def __init__(self, name, employees=None):
        if employees is None:
            employees = []
        self.name = name
        self.employees = employees

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #         sort_keys=True, indent=4)

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum += num

    @staticmethod
    def calculate_lateness(mHours, distacne, velocity, tHours = 9):
        cal_time = velocity/distacne
        arrive_time = cal_time + mHours
        if arrive_time > tHours:
            return False
        else:
            return True

    def get_all_employees(self):
        return self.employees

    def get_employee(self, id):
        for emp in self.employees:
            if id == emp.id:
                return emp

    def Hire(self, *args):
        for emp in args:
            car = emp.car.__dict__
            emp.__dict__.update({'car': car})
            self.employees.append(emp.__dict__)
            # self.employees.append(car)

    def Fire(self, id):
        for emp in self.employees:
            if id == emp.id:
                self.employees.remove(emp)

    def Deduct(self, id, deduction):
        for emp in self.employees:
            if id == emp.id:
                emp.salary = emp.salary - deduction

    def Reward(self, id, reward):
        for emp in self.employees:
            if id == emp.id:
                emp.salary = emp.salary + reward

    def check_lateness(self, id, mHours):
        for emp in self.employees:
            if id == emp.id:
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

emp1 = Employee(1, 'BMW', 'mohamed@gmail.com', 200, 40, 'mohamed', 5000)
emp1.mood = 'happy'
emp2 = Employee(2, 'FIAT', 'smahy@gmail.com', 1200, 60, 'smahy', 10000)
emp2.mood = 'lazy'
emp4 = Employee(4, 'BYD', 'mooo@gmail.com', 4000, 80, 'mooo', 7000)
emp4.mood = 'lazy'
emp3 = Employee(3, 'KIA', 'tarek@gmail.com', 2000, 50, 'tarek', 8000)
# emp.SendEmail('mohamed@gmail.com', 'hello', 'hi mohamed', 'mohamed')
# print(emp.salary)
# print(emp.email)

# car1 = Car('KIA', 50, 80)
# car1.Run(50, 80)

office1 = Office('ITI')
office2 = Office('IT company')
# office1.employeesNum = 2
# office1.employeesNum = 1
office1.Hire(emp1, emp2, emp4)
office2.Hire(emp3)
g = office1.get_all_employees()
g1 = office2.get_all_employees()
print(g, '\n')
print(g1, '\n')

# Office.change_emps_num(5)
# print(Office.employeesNum)


# json data file about ITI office
# data = Office.toJSON(g)
data = g
with open('jsondata.txt', 'w') as outfile:
    for emp in data:
        json.dump(f'employee : {emp}', outfile)
        outfile.write('\n')

