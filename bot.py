from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import os
import re

# Your Bot Token Here
token = os.environ.get('TELEGRAM_TOKEN')

def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('pur', pur))
    updater.start_polling()
    updater.idle()

def get_url(api_url):
    contents = requests.get(api_url).json()
    if isinstance(contents, list):
        url = contents[0]['url']
    elif isinstance(contents, dict):
        url = contents['url']
    return url

def get_image_url(api_url):
    allowed_extension = ['jpg', 'png', 'jpeg']
    file_extension = ""
    while file_extension not in allowed_extension:
        url = get_url(api_url)
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

def bop(bot, update):
    dog_api = 'https://random.dog/woof.json'
    url = get_image_url(dog_api)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def pur(bot, update):
    cat_api = 'https://api.thecatapi.com/v1/images/search'
    url = get_image_url(cat_api)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


if __name__ == '__main__':
    main()