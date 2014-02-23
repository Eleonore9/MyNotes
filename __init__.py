from flask import Flask
from flask.ext.mongoengine import MongoEngine
print 'init 1'
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB' : "my_tumble_log", 'alias' : 'default'}
app.config["SECRET_KEY"] = 'K33pth1ss3cr3t'
print 'init 2'

db = MongoEngine(app)
print 'init 3'


def register_blueprints(app):
	from tumblelog.views import posts
	app.register_blueprint(posts)

register_blueprints(app)
print 'init 4'

if __name__ == "__main__":
	app.run()
