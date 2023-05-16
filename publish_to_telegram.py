import telegram
import time
import os
import random
from dotenv import load_dotenv
import argparse


def publish_to_telegram(tg_bot_token, tg_chat_id, delay_time):
    bot = telegram.Bot(token=tg_bot_token)
    for root, dirs, files in os.walk("images"):
        while True:
            for file in files:
                bot.send_photo(chat_id=tg_chat_id, photo=open(f"images/{file}" , "rb"))
                time.sleep(delay_time)
            random.shuffle(files)


def main():
    load_dotenv()
    tg_chat_id = os.getenv("TG_CHAT_ID")
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    parser = argparse.ArgumentParser(description="Publish photos to Telegram.")
    parser.add_argument("-d", "--delay_time", default=1440, type=int, help="Time between sending photos.")
    args = parser.parse_args()
    publish_to_telegram(tg_bot_token, tg_chat_id, args.delay_time)


if __name__ == "__main__":
    main()
