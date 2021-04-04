import pyowm
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('f21d9c5796e745aa26efc9bcd5820f51')
mgr = owm.weather_manager()

place = input("Введите пожалуйста город? ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]
print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас в районе " + str(temp))

if temp < 5:
    print("Сейчас холодновато, одевайся теплее!")
elif temp < 10:
    print("Сейчас прохладно, одевай курточку!")
else:
    print("Температу температура норм,одевай что угодно:)")
