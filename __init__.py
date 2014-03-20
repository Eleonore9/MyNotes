from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB' : "my_tumble_log", 'alias' : 'default'}
app.config["SECRET_KEY"] = 'K33pth1ss3cr3t'

db = MongoEngine(app)


def register_blueprints(app):
	#Prevents circular imports
	from tumblelog.views import posts
	from tumbleblog.admin import admin
	app.register_blueprint(posts)
	app.register_blueprint(admin)

register_blueprints(app)

if __name__ == "__main__":
	app.run()
