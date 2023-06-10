import random

class User:
    def __init__(self, name):
        self.name = name

class TravelProject:
    def __init__(self, user):
        self.user = user
        self.countries = ['Франції', 'Турції', 'Єгипті', 'Японії', 'Австралії', 'Україні']

    def random_country(self):
        return random.choice(self.countries)

    def country_activities(self, country):
        activities = [
            '🏝️Відвідування музеїв🏝️ ', "🏝️Пам`ятки міст🏝️", '🏝️Національна кухня🏝️', '🏝️Відвідування міських пляжів🏝️', '🏝️Купівля сувенірів🏝️', '🏝️Єкскурсії по країні🏝️', '🏝️Прийняти учать у різних видах водного спорту🏝️',   '🏝️Відвідати аквапарк!🏝️'
        ]

        print(f'{country}:')
        days = random.randint(7, 14)
        print(f'{self.user.name} 🤑Ви вибрали путівку на: {days} днів🤑!')
        for day in range(1, days + 1):
            activity = random.choice(activities)
            print(f'-----------------👐👐Day {day} of {self.user.name} life👐👐:------------------- \n                ~~~{activity}~~~')
        print('-' * 30)

    def travel(self):
        live = self.random_country()
        if live == 'Україні':
            print(f'{self.user.name}, 🤯ви і так в Україні🤯!')
            return

        print(f'{self.user.name}, ~~~~~😙Ваш літак приземлився в {live}😙~~~~~.')
        self.country_activities(live)
        print('________😱Ваш час вичерпано, ви повертаєтесь в Україну😱_________.')





user = User(name='Danya')
project = TravelProject(user=user)
project.travel()