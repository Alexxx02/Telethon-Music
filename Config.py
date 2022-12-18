import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28182720"))
    API_HASH = os.environ.get("API_HASH", "5360e97ddd3e771e124aa50c6c33ec3a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5870406957:AAEdvFwNYdsXjaukiBNiaBPdobnQR1pmIrg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHoBu4N_YhWb4aIntn88FKKeAzRQI85tEVwfWIm7sJWmUB3NiJVZvCu3Jy95S2oUPDh3LCnkLSmPHPantQ8mHh9cQ0D7ihGZy9m0UtkuMmXLY13f6z7pUQ6NYOsZAnwZ0zwjn9PAo1Cehcl-enE3MT3hKKoC-cr-WSThCenGPte74jEqHZ2ZUOeBQikNvEanYzSJ-Hv5sUEh5oqT9CJSnV1ZDnmgDjgNFE0fc1bCebmzZ6v_rIC16B_Di6OZPizTpVn3a8F280pdZuqopxzYjVwOchIFX7QGcQTw-e8XBDzahfekoR-XAnwjQKx6F5Zc5e_ol99WKx-7ntYeWNabXbu6MJI=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5746950993")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
