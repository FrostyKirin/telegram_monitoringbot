# coding=utf-8

#Codé par Hugo Waltsburger, 06.08.2018
#Contact : hugo.waltsburger@larez.fr

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from queries_template import *
from routine import routine

# Ici, je définis le niveau de logging. Par défaut, info est un bon choix
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

logger = logging.getLogger(__name__)


# Ici, nous définissons les différentes fonctions du bot. Ces fonctions seront appelées sur /"nom de la fonction" 

def start(bot, update,job_queue):
    """Envoie un message lorsque la commande /start est envoyée sur un chan"""
    update.message.reply_text("""Bonjour ! Je suis le bot de monitoring d\'Unchartech.    
            \nMa fonction est de vous apporter des updates réguliers sur l\'état de l\'infrastructure, ainsi que diverses statistiques. 
            \nVous pouvez dès maintenant et à tout moment utiliser /help pour obtenir un résumé de mes fonctionnalités. A très vite ! """)

def start_routine(bot,update, job_queue):
    bot.send_message(chat_id='insert-conversation-identifier-here', text='Lancement de la routine de diagnostic')
    job_queue.run_repeating(routine_launcher, 60, context=update.message.chat_id)

def help(bot, update):
    """Envoie le message suivant lorsque la commande /help est envoyée sur un chan"""
    update.message.reply_text("""Vous pouvez m\'envoyer diverses requêtes, qui apparaîtront comme suggestions si vous tapez "/" dans votre barre de message
            \nMes fonctionnalités sont les suivantes : \n
            
            /test : Je vous réponds si je suis actuellement en fonctionnement ! 
            /ratio : Je vous renvoie les divers ratios que je suis capable de vous fournir
            /infra : Je vous renvoie un checkup de l\'infrastructure""")
def test(bot,update):
    update.message.reply_text('Je fonctionne parfaitement!')

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text("Je suis désolé, je ne comprends pas ce que vous désirez")


def error(bot, update, error):
    """Loggue les erreurs d'Update"""
    logger.warning('Update "%s" caused error "%s"', update, error)

def get_all(bot, update): #Cette fonction renvoie la totalité des ratios
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_net_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_gross_exposure(bot, update):
    message=sql_query('SELECT version()')
    update.message.reply_text(message)

def get_non_eur_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_small_cap_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_eur_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_opc_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_max_perc_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_pea_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_non_cash_equity_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_derivatives_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_cash_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_cash_loan_exposure(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_srri(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def get_id_fund(bot, update):
    message = sql_query('SELECT version()')
    update.message.reply_text(message)

def stats(bot, update):
    message = sql_query('SELECT version()') 
    update.message.reply_text(message)

def routine_launcher(bot, job):
    message = routine()
    bot.send_message(chat_id=-300418520,text=message)

#def callback(bot, update, job_queue)
#    bot.send_message(chat_id=-300418520, text="Whatever.")

def main():
    """Démarre le bot"""
    # La commande suivant créé l'event handler ; elle créé le lien entre l'API Telegram et l'instance locale, via un token donné par le "botfather"
    # L'updater lit en permanence le flux de messages sur les chans
    updater = Updater("insert-bot-token-here")
    # On définit une queue pour pouvoir faire tourner des actions à intervalles réguliers
    j=updater.job_queue
    # Le dispatcher s'occupe de parser le contenu des messages feedés par l'Updater, notamment via / 
    dp = updater.dispatcher
    # Les commandes suivantes définissent les fonctions appelées lorsqu'un utilisateur rentre une commande
    dp.add_handler(CommandHandler("start", start,pass_job_queue=True))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("stats",stats))
    dp.add_handler(CommandHandler('start_routine', start_routine, pass_job_queue = True))
    dp.add_handler(CommandHandler('timer',routine_launcher, pass_job_queue=True))
    dp.add_handler(CommandHandler('get_all',get_all))
    dp.add_handler(CommandHandler('get_net_exposure',get_net_exposure))
    dp.add_handler(CommandHandler('get_gross_exposure',get_gross_exposure))
    dp.add_handler(CommandHandler('get_non_eur_exposure',get_non_eur_exposure))
    dp.add_handler(CommandHandler('get_small_cap_exposure', get_small_cap_exposure))
    dp.add_handler(CommandHandler('get_eur_exposure', get_eur_exposure))
    dp.add_handler(CommandHandler('get_opc_exposure', get_opc_exposure))
    dp.add_handler(CommandHandler('get_max_perc_exposure', get_max_perc_exposure))
    dp.add_handler(CommandHandler('get_pea_exposure', get_pea_exposure))
    dp.add_handler(CommandHandler('get_non_cash_equity_exposure', get_non_cash_equity_exposure))
    dp.add_handler(CommandHandler('get_derivatives_exposure', get_derivatives_exposure))
    dp.add_handler(CommandHandler('get_cash_exposure', get_cash_exposure))
    dp.add_handler(CommandHandler('get_cash_loan_exposure',get_cash_loan_exposure))
    dp.add_handler(CommandHandler('get_srri', get_srri))
    dp.add_handler(CommandHandler('get_id_fund', get_id_fund))
    # Définit la réponse aux messages qui ne sont pas destinés au bot (messages ne commençant pas par '/')
    # dp.add_handler(MessageHandler(Filters.text, echo))
    # Logging des erreurs
    dp.add_error_handler(error)
    # Démarrage du bot
    updater.start_polling()
    # Lance le bot jusqu'à-ce que l'utilisateur rentre ctrl+C
    updater.idle()
    
        

if __name__ == '__main__':
        main()
        
