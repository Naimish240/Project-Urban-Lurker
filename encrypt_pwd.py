#!/usr/bin/env python

# This module is used to encrypt the passwords stored in the database

import bcrypt

def hash_string(string):
    # Returns a plaintext string
    final = bcrypt.hashpw(string.encode(),bcrypt.gensalt()).decode()
    return final

def check_hash(user_string, stored_hash):
    # Assumes stored hash to be passed in plain text
    return bcrypt.checkpw(user_string.encode(),stored_hash.encode())