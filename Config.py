import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("10612241"))
    API_HASH = os.environ.get("81c931f5a5cf6ba07da1bcc799e7f40d")
    BOT_TOKEN = os.environ.get("5092676724:AAGKKruSPwhzKy5VtN0Jp11iwHk-tU7F8do")
    BOT_USERNAME = os.environ.get("Miracbeybot")
    BOT_NAME = os.environ.get("Miracbeybot")
    BOT_ID = int(os.environ.get("862341989"))
    SUDO_USERS = os.environ.get("5092676724").split()
    SUPPORT_CHAT = os.environ.get("@KadimmTayfaa")
    OWNER_ID = int(os.environ.get("5092676724"))
    OWNER_USERNAME = os.environ.get("@beylerbeyiniz")
