# This module is used to encrypt the passwords stored in the database

import bcrypt

def hash_string(string):
    # Returns a plaintext string
    final = bcrypt.hashpw(string,bcrypt.gensalt()).decode()
    return final

def check_hash(user_string, stored_hash):
    return bcrypt.checkpw(user_string.encode(),stored_hash)