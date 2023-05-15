import telegram
import time
import os
import random
from dotenv import load_dotenv
import argparse


def publish_to_telegram(tg_bot_token, tg_chat_id, args):
    bot = telegram.Bot(token=tg_bot_token)
    for root, dirs, files in os.walk("images"):
        while True:
            for file in files:
                bot.send_photo(chat_id=tg_chat_id, photo=open(f"images/{file}" , "rb"))
                if args.delay_time:
                    time.sleep(args.delay_time)
                else:
                    time.sleep(1440)
            random.shuffle(files)


def main():
    load_dotenv()
    tg_chat_id = os.getenv("TG_CHAT_ID")
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delay_time", type=int)
    args = parser.parse_args()
    publish_to_telegram(tg_bot_token, tg_chat_id, args)


if __name__ == "__main__":
    main()