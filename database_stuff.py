#!/usr/bin/env python
# Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;
import pyodbc

conn = pyodbc.connect("TheUrbanLurker.db")

c = conn.cursor()

def initialize():
    # name: username, pwd: password, regno: regno, hostel: hostel name
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pwd TEXT, regno TEXT, hostel TEXT)")
    # owner: name, file_name: name of file, file_size: size of file
    c.execute("CREATE TABLE IF NOT EXISTS files (owner TEXT, file_name TEXT, file_size TEXT)")

def insert_into_users(name, pwd, regno, hostel):
    # Inserts values into the table users
    c.execute("INSERT INTO users VALUES ('{}','{}','{}','{}')".format(name,pwd,regno,hostel))
    conn.commit()

def check_username(name):
    # Function to check if username exists or not
    c.execute("SELECT name FROM users WHERE name = '{}'".format(name))
    if c.fetchone():
        return False
    return True

def retrieve_pwd(name):
    # Function to access the hash
    # It returns the salted hash in plaintext
    c.execute("SELECT pwd FROM users WHERE name = '{}'".format(name))
    pwd = str(c.fetchone())
    return pwd

def insert_into_files(owner, file_name, file_size):
    # Inserts values into the table files
    c.execute("INSERT INTO files VALUES ('{}','{}','{}')".format(owner,file_name,file_size))
    conn.commit()

def find_persons_with_file(file_to_find):
    # Executes command to select the owner and file size where the file name contains the substring
    c.execute("SELECT owner, file_size FROM files WHERE file_name LIKE '%{}%'".format(file_to_find))

    # Creates two empty lists to store the values obtained from the query
    owner = []
    file_size = []

    # Appends the stuff to the corresponding lists
    for row in c.fetchall():
        owner.append(row[0])
        file_size.append(row[1])

    return {"owner" : owner, "file_size" : file_size}

def find_hostel(user):
    # Function to find the hostel of the user
    c.execute("SELECT hostel FROM users WHERE name = '{}'".format(user))
    return str(c.fetchone())

def user_files(user):
    # Function to pull list of files the person has added to the database
    c.execute("SELECT file_name,file_size FROM files WHERE owner = '{}'".format(user))

    # List of files the owner has
    l = []
    for row in c.fetchall():
        l.append(row[0])
    
    # Returning list of all the files the user has provided
    return l

def add_files(user,files_to_add,file_size, category, ext):
    # all parameters passed are lists, adds them to the list
    for i in range(len(files_to_add)):
        insert_into_files(user,files_to_add[i],file_size[i])

def delete_files(user,files):
    # Verify with user before running this function
    for i in files:
        c.execute("DELETE FROM files WHERE owner = '{}' and file_name = '{}'".format(user,i))
        c.commit()

if __name__ == '__main__':
    initialize()    # always run
    # Sample IO
    insert_into_users("naimish","asdf","jkl;","asdf")
    insert_into_files("naimish","asdf","qwer")
    c.close()
    conn.close()
