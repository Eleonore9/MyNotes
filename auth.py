from functools import wraps
from flask import request, Response

def check_auth(username, password):
	"""Takes in user's name and password 
	and checks if the combination are valid"""
	return username == 'admin' and password == 'secret'

def authenticate():
	"""Sends a 401 response that enables
	basic auth"""
	return Response(
		'Could not verify your access level for that URL.\n'
		'You have to login with proper credentials', 401,
		{'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
	"""Creates a requires_auth decorator to decorate any view
	that needs authentification"""
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated
