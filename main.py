from urllib import response
import Constants as constants
from telegram.ext import *
import Responses as R
from footballdata import getNextFixturesList, getPrevFixturesList

print("Bot started...")

def checkInt(my_str):
    if my_str[0] in ('-', '+'):
        return my_str[1:].isdigit()
    return my_str.isdigit()

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")

def help_command(update, context):
    update.message.reply_text("If you need help you should ask for it on Google!")

def nexti_command(update, context):
    if(len(context.args) != 1 or not isinstance(context.args[0], str) or not checkInt(context.args[0])):
        update.message.reply_text("Command Usage: next_i num_of_matches")
        return
    fixtures_list = getNextFixturesList(context.args[0])
    for f in fixtures_list:
        update.message.reply_text(f.GetFixtures()+"\n")

def previ_command(update, context):
    if(len(context.args) != 1 or not isinstance(context.args[0], str) or not checkInt(context.args[0])):
        update.message.reply_text("Command Usage: next_i num_of_matches")
        return
    fixtures_list = getPrevFixturesList(context.args[0])
    for f in fixtures_list:
        update.message.reply_text(f.GetFixtures()+"\n")
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():

    #receive the updates from Telegram and deliver them to the dispatcher
    # updater = Updater(constants.TELEGRAM_API_KEY, use_context=True)
    updater = Updater("5542999003:AAFoaBSxmFklsV-8ooleMdT3UVrWEena39s", use_context=True)
    
    #Dispatcher that handles the updates and dispatches them to the handlers.
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("next_i", nexti_command, pass_args=True))
    dp.add_handler(CommandHandler("prev_i", previ_command, pass_args=True))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle() 

if __name__ == '__main__':
    main()