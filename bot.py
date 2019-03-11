from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )



def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def learn_constellation(bot, update):
    get_planet = update.message.text.split()[1]
        
    import ephem

    if get_planet == 'Mars':
        planet = ephem.Mars('2019/09/12')
        constellation = 'Планета находится в созвездии {}'.format(ephem.constellation(planet))
        update.message.reply_text(constellation)
    else:
        error_text = 'Может все-таки Mars???'
        update.message.reply_text(error_text) 
   


def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

    

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', learn_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()