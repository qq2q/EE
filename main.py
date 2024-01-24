import requests, telebot
from telebot import types
bot = telebot.TeleBot("6547250716:AAFG6fiOSe4rJtdoMe-SWR4dh5jeXCJ4h6s")
@bot.message_handler(commands=['start'])
def handle_start(message):
    data={'key':'6d37c130d54669c53bf9bd1e90ed2833','action':'balance'}
    res=requests.post('https://smmpanel.com/api/v2',data=data).json()
    balance=float(res['balance'])
    views=str(balance/0.0000001).split('.')[0]
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Programer', url="https://t.me/C35CS"))
    bot.reply_to(message,f'''- TikTok Views Bot

- Remain : {views} Views

- By : @DevEviI

- Channel : @DevEviI & @C35CS

- Send Video URL Here''',reply_markup=markup)
def gpt(text) -> str:
 data={'key':'6d37c130d54669c53bf9bd1e90ed2833','action':'add','service':768,'link':text,'quantity':1000}
 res=requests.post('https://smmpanel.com/api/v2',data=data)
 if 'order"' in res.text:
   s='[√] Done Send 1000 Views'
   return s
 else:
  msg=res.json()['error']
  return msg
S = ""
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg = gpt(message.text)
    if msg:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Programer', url="https://t.me/C35CS"))
        bot.reply_to(message, msg, reply_markup=markup)
    else:
        bot.reply_to(message, "حدث خطأ أعد المحاولة")
print(S)
bot.polling()
