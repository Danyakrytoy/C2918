import random
# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#
#
# class Auto:
#
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human):
#         self.passengers.append(human)
#
#     def print_passengers_names(self):
#         if self.passengers != []:
#             print(f'Names of {self.brand} passengers: ')
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f'There are no passenger in {self.brand} passengers: ')
#
#
# vasya = Human("Vasya")
# petya = Human("Petya")
#
# car = Auto("Vercedes")
#
# car.add_passenger(vasya)
# car.add_passenger(petya)
# car.print_passengers_names()

#__________________________SIMS______________________________________________

class Human:
    def __init__(self, name="Human", job=None, home = None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eaten(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.satiety = 100
            self.satiety = 100
            return
        self.satiety += 6
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Yay! Delicacies')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness += 10
        self.home.mess += 5

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self,day):
        day = f"Today {day} of {self.name} 's life"
        print(f"{day:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}","\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fatigue - {self.car.fatigue}")
        print(f"Strength - {self.car.strength}")


    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead..")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False

    def live(self,day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a item {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)

        if self.satiety < 20:
            print("I`ll go eat")
            self.eaten()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess... \n So I will wash yourself")
                self.wash_yourself()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start play")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
        elif dice == 1:
            print("Let`s chill")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("wash yourself")
            self.clean_home()
        elif dice == 4:
            print("Time to treats!")
            self.shopping(manage="delicacies")



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fatigue = brand_list[self.brand]['fatigue']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fatigue >= self.consumption:
            self.fatigue -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "catches mice": {"salary": 50, "gladness_less": 10},
    "catches fish": {"salary": 40, "gladness_less": 3},

}
brands_of_car = {
    "skate": {"fatigue": 90, "strength": 100, "consumption": 6},
    "box": {"fatigue": 50, "strength": 40, "consumption": 10},
    "cart": {"fatigue": 70, "strength": 150, "consumption": 8},

}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

kasper = Human(name="Cat")
for day in range(1, 20):
    if kasper.live(day) == False:
        break