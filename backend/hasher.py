import hashlib
import os



salt = os.urandom(32) # Remember this
print(salt)
password = 'password123'

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
print(key)