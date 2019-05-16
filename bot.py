from uwu import Uwu
import os

token = os.getenv('UWU_TOKEN')
redis_url = "redis://localhost:6379/0"
mongo_url = "mongodb://localhost:27017/uwu-bot"

bot = Uwu(redis_url=redis_url, mongo_url=mongo_url)

bot.run(token)
