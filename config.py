from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3e72df6ef787df25f008e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3e72df6ef787df25f008e.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yasamakbuysa")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/yasamakbuysa")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7950993603").split()))


FAILED = "https://telegra.ph/file/3e72df6ef787df25f008e.jpg"
