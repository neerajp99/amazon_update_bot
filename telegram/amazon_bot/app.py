from flask import Flask, request
import telegram
from credentials import bot_user_name, bot_token, URL

# Globally create bot and token variables 
global BOT, TOKEN 
TOKEN = bot_token

# Initialse bot object
bot = telegram.Bot(token = TOKEN)

# Start the flask app 
app = Flask(__name__)

"""
	Home route to be called to get responses for messages sent to the bot.
"""
@app.route('/{}'.format(TOKEN), methods=['POST'])

# Method used to provide responses to specfic arguments 
def respond():
	# Get argument text as JSON and transform it into Telegram object 
	update_content = telegram.Update.de_json(request.get_json(force = True), bot)
	
	# Get chat and message ID from the update_context object 
	chat_id = update_context.message.chat.id 
	message_id = update_context.message.message_id

	# Encode the text from the update_context object
	encoded_text = update_context.text.encode('utf-8').decode()

	# Output to the console
	print("Received message: ", encoded_text) 

	if encoded_text == "/start":
		# Show the welcome message 
		welcome_message = " Welcome to the the Amazee Bot. I'm here to help you track amazon product prices for your convenience. " 

		# Send the message to the user 
		bot.sendMessage(chat_id = chat_id, text = welcome_message, reply_to_message_id = message_id)


if __name__ == '__main__':
   app.run(threaded=True)

