import telebot
import time
from scrap import ProductDetails

bot_token = "1275471899:AAEovIzpmN1-oYBxxRM6ExsWUsqA6QkaYNc"

products={}

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message,"Welcome to Amazon price alert. Try using /set_alert link of the produt")

@bot.message_handler(func = lambda msg: msg.text is not None and 'set_alert' in msg.text)
def scrape(message):
    text=message.text
    try:
        link=text[text.find("https"):]
        new_product = ProductDetails(link)
        new_product.get_content()
        bot.reply_to(message,"You selected "+new_product.title+". Now price is at ₹" + new_product.product_price)
    except:
        bot.reply_to(message,"Try again")

while(True):
    try:
        bot.polling()
    except Exception:
        time.sleep(15)