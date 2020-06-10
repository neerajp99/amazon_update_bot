import telebot
import time
from scrap import ProductDetails
import threading

bot_token = "YOUR BOT TOKEN GOES HERE"

# Dictionary containing all user searches with content
products = {}

# Initialise telegram bot with the token
bot = telebot.TeleBot(token = bot_token)

"""
    Trigger function when user enters /start
"""
@bot.message_handler(commands = ['start'])
def welcome(message):
    # Welcome message whenever user starts using the bot
    bot.reply_to(message, "Welcome to Amazon price alert. Try using /set_alert link of the produt")

    # Multithreading program for checking the price change 
    def automatatic_price_check(username):
        threading.Timer(10.0, automatatic_price_check, args = (username,)).start()
        # Run if the current product is searched by an already defined user
        if username in products:
            for product in products[username]:
                temp = product.product_price
                product.get_content()
                # If the temporary variable is empty
                if temp != product.product_price:
                    bot.send_message(username, "Your product" + product.product_name + "is now priced at ₹" + product.product_price)
                # else:
                #     bot.send_message(username, "No change bro!!!")
    automatatic_price_check(message.chat.id)

"""
    Trigger function when user adds an item for search using /set_alert <item link>
"""
@bot.message_handler(func = lambda msg: msg.text is not None and 'set_alert' in msg.text)
def scrape(message):
    text = message.text
    try:
        link = text[text.find("https"):]
        username = message.chat.id
        new_product = ProductDetails(link, username)

        # If user has already requested a product, append the product details
        if username in products:
            products[username].append(new_product)
        # Otherwise, create a new array and add the product details
        else:
            products[username] = [new_product]
        new_product.get_content()
        bot.reply_to(message,"You selected " + new_product.product_name + ". Now price is at ₹" + new_product.product_price)
    except Exception as e:
        bot.reply_to(message,"Try again")
        # print("Oops!", e, "occurred.")

while(True):
    try:
        bot.polling()
    except Exception:
        time.sleep(15)