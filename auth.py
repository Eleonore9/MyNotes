from functools import wraps
from flask import request, Response

def check_auth(username, password):
	"""Takes in user's name and password
	and checks if the combination are valid""""
