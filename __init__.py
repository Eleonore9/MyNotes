from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB' : "my_tumble_log"}
app.config["SECRET_KEY"] = 'K33pth1ss3cr3t'

db = MongoEngine(app)


def register_blueprints(app):
	from tumblelog.views import posts
	app.register_blueprint(posts)

register_blueprints(app)


if __name__ == "__main__":
	app.run()
