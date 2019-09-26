from flask import Flask
from config import Config

print(2)
app = Flask(__name__)
app.config.from_object(Config)
print(3)
from app import routes, bot
