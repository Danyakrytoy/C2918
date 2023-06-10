import random
import string



def generate_password(parol):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(parol))
    return password



name = input("|------------🌹Регистрація🌹----------| \n|🥝Напишіть своє ім`я:🥝  ")
password1 = input("|🐸Придумайте пароль:🐸  ")

parol = int(input("|🍉Введіть довжину пароля яку хочете згенерувати:🍉 "))


password = generate_password(parol)
print("|🍎Згенерований пароль🍎:", password)
review = input("|🙃Залишіть ваш відгук:🙃 ")
print(f"|{name}! ☺️Дякую за відгук!☺️ ")

