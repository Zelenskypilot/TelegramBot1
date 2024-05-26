from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Token for accessing the Telegram Bot API
TOKEN = '7207778038:AAH2P5Kx3Me1zF6_c0VgZmJnt3bLDIlbcBM'

# Command handler for /start command
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Hello {user.first_name}! Welcome to the Loan Airtime Bot. "
                              "Select your desired loan amount below:")

    keyboard = [
        [
            InlineKeyboardButton("500 Tsh", callback_data='500'),
            InlineKeyboardButton("1000 Tsh", callback_data='1000'),
            InlineKeyboardButton("2000 Tsh", callback_data='2000')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose your loan amount:', reply_markup=reply_markup)

# Callback handler for button clicks
def button(update, context):
    query = update.callback_query
    loan_amount = int(query.data)
    user = query.from_user
    query.answer()
    query.edit_message_text(f"Dear {user.first_name}, your loan request of {loan_amount} Tsh has been received. "
                            "The airtime will be credited to your account shortly.")

# Command handler for /help command
def help(update, context):
    update.message.reply_text('This bot allows you to request a loan airtime. Simply click on the desired loan amount.')

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Register button callback handler
    dp.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
