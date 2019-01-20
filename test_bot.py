import telebot
import time
import random

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

ids = []
admin_id = 1

instruments = ["calm ", "kreak ", "palka ", "fierwerk ", "bint ", "pistol ", "iphone ", "shit_box ", "botinok ", "pehtkis ", "vodichka ", "cigarete " , "terrorists_win ", "pobegi ", "ice ", "kolonna ", "vodianoi_matras ", "sos ", "table ", "lopata ", "scarf "] 
tasks = [0, 1, 2, 3, 4 ,5, 6]

tasks[0] = "Вы идёте с другом, ничего не предвещает беды. Почти каждую неделю ходите этим маршрутом и ничего не меняется. Но не сегодня. Только подходите к одному из домов, как замечаете чёрный дым, исходящий со стороны двора, а когда подходите ещё ближе, понимаете, что горит урна. Пускай и незначительный, но это пожар, и оставлять дело просто так нельзя. Что Вы возьмёте в помощь?"
tasks[1] = " "
tasks[2] = " " 
tasks[3] = " "
tasks[4] = " "
tasks[5] = " "
tasks[6] = " "




num = 0

bot = telebot.TeleBot("763328845:AAHfQLpwfJhV6UFqQ_0_ld1cawn84HvoZhA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    #if message.chat.id != admin_id :
    ids.append(message.chat.id)
    bot.reply_to(message, "U were registered")

@bot.message_handler(commands=['admin_pass'])
def send_admin_message(message):
    admin_id = message.chat.id
    ids.pop(admin_id)
    bot.send_message(message.chat.id, "U're admin now!")

@bot.message_handler(commands=['card1'])
def send_message(message):
    bot.send_message(message.chat.id, "U use first card!")

@bot.message_handler(commands=['card2'])
def send_message(message):
    bot.send_message(message.chat.id, "U use second card!")

@bot.message_handler(commands=['card3'])
def send_message(message):
    bot.send_message(message.chat.id, "U use thirtd card!")

@bot.message_handler(commands=['task'])
def send_task_message(message):
    if message.chat.id == admin_id :
        num = random.randint(1,21)
        for i in ids :
            bot.send_message(i, tasks[0])
            #bot.send_message(i , "U have some instruments: " + instruments[num])


while True :
    try :
        bot.polling(none_stop = True)
    except :
        time.sleep(2)
