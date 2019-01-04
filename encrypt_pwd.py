# This module is used to encrypt the passwords stored in the database

import bcrypt

def generate_salt():
    return bcrypt.gensalt()

def hash_string(string, salt):
    # Returns a plaintext string
    final = bcrypt.hashpw(string,salt).decode()
    return final

def check_hash(user_string, stored_string):
    pass