import random


# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160, name=None):
#         self.name = name
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height += height
#
#
# vasya = Student(height=180, name='Vasya')
# mari = Student(name='Mari')
# vova = Student(height=200, name='Vova')
#
# mari.grow(height=15)
#
# print(vasya.height, vasya.name)
# print(mari.height, mari.name)
# print(vova.height, vova.name)
# print(Student.amount_of_students)
#
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('Hello Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(F'Gladness = {self.gladness}')
        print(F'Progress = {round(self.progress, 2)}')

    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + 'life.'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
