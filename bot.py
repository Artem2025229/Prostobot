from config import token 
import telebot
import random
import time
from datetime import datetime


# Старт
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот с 10 функциями. Напиши /help, чтобы узнать, что я умею.")

# Помощь
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    /hello - Приветствие
    /fortune - Предсказание 
    /date - Сегодняшняя дата
    /dice - Бросить игральный кубик
    /coin - Бросить монетку
    /time - Текущее время
    /random - Случайное число от 1 до 100
    /photo - Случайное фото
    /echo - Эхо отправленого сообщения
    /info - Информация о пользователе
    /reverse - Переворот текста
    """
    bot.reply_to(message, help_text)

# Приветствие
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет, как дела? ")

# Предсказание
@bot.message_handler(commands=['fortune'])
def send_fortune(message):
    fortunes = [
        "В ближайшие 10 лет космический туризм станет доступен не только миллионерам, но и среднему классу.",
        "Искусственный интеллект будет помогать людям писать книги и сценарии так же, как сейчас помогает с кодом.",
        "К 2050 году население Земли превысит 9 миллиардов человек.",
        "Игры будущего будут использовать нейроинтерфейсы — управление напрямую мыслями.",
        "Города начнут активно строить вертикальные фермы, чтобы обеспечивать жителей свежей едой прямо в мегаполисах."
    ]
    random_fortune = random.choice(fortunes)
    bot.reply_to(message, f"Вот твое предсказание: \n\n {random_fortune} ")

# Кубик
@bot.message_handler(commands=['dice'])
def roll_dice(message):
    dice_message = bot.send_dice(message.chat.id)
    time.sleep(4)
    result = dice_message.dice.value
    bot.reply_to(message, f"Ваше число: **{result}**!")

# Монетка
@bot.message_handler(commands=['coin'])
def flip_coin(message):
    result = random.choice(["Орел", "Решка"])
    bot.reply_to(message, f"Монетка подброшена... Выпало: **{result}**!")

# Часы
@bot.message_handler(commands=['time'])
def get_time(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, f"Текущее время: **{current_time}**")


# Дата
@bot.message_handler(commands=['date'])
def get_date(message):
    today = datetime.now().strftime("%d.%m.%Y")
    bot.reply_to(message, f"Сегодняшняя дата: **{today}**")

# Факт
@bot.message_handler(commands=['fact'])
def get_fact(message):
    facts = [
        "Самый тяжёлый элемент в таблице Менделеева — оганессон (Og), открытый в 2002 году.",
        "В нашей галактике Млечный Путь больше звёзд, чем песчинок на всех пляжах Земли.",
        "У гигантских кальмаров глаза размером с футбольный мяч — это самые большие глаза в животном мире.",
        "Литий, используемый в батареях, настолько лёгкий металл, что может плавать на воде.",
        "Первая видеоигра в истории — «Tennis for Two» (1958), созданная на осциллографе."
    ]
    bot.reply_to(message, random.choice(facts))


# Число
@bot.message_handler(commands=['random'])
def get_random_number(message):
    random_num = random.randint(1, 100)
    bot.reply_to(message, f"Случайное число от 1 до 100: **{random_num}**")

# Фото
@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_url = "https://picsum.photos/200/300" 
    bot.send_photo(message.chat.id, photo_url)


 # Информация
@bot.message_handler(commands=['info'])
def get_user_info(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    bot.reply_to(message, f"Ваш ID: `{user_id}`\nВаше имя: **{first_name}**", parse_mode='Markdown')


# Реверс
@bot.message_handler(commands=['reverse'])
def reverse_text(message):
    text = message.text.replace('/reverse ', '', 1)
    reversed_text = text[::-1]
    bot.reply_to(message, reversed_text)


# Эхо
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


print("Бот запущен. Напиши /help, чтобы начать.")

bot_infinity.polling()