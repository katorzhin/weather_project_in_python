import telebot
import pyowm
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = pyowm.OWM('your token')
mgr = owm.weather_manager()
bot = telebot.TeleBot("your token")


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 5:
        answer += "Сейчас холодновато, одевайся теплее!"
    elif temp < 10:
        answer += "Сейчас прохладно, одевай курточку!"
    else:
        answer += "Температура норм,одевай что угодно:)"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
