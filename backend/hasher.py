import hashlib
import os


def make_new_hash(password):
	"""
		input: password
		return: salt, key

	"""

	salt = os.urandom(32)
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

	return salt, key


def make_hash(salt, password):

	"""
		input: salt, password
		return key

	"""
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)	

	return key