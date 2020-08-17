from telegram.ext import Updater, CommandHandler
import requests
import re
from flask import Flask, request
import os

server = Flask(__name__)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def boop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater("1190888035:AAGeJ9316R95NqJLFefV5vQA-UL4np11V2c")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('boop', boop))
    updater.start_polling()
    updater.idle()


def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_image_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://your_heroku_project.com/" +
                    "1190888035:AAGeJ9316R95NqJLFefV5vQA-UL4np11V2c")
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    main()
