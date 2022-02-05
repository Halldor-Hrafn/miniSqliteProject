import tkinter as tk
from tkinter import ttk
from tkinter import *

import sqlite3
from sqlite3 import Error
from venv import create

def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print(sqlite3.version)
        print('Connection successful')
    except Error as e:
        print(e)
    return conn

def createTable(conn, createTable):
    try:
        c = conn.cursor()
        c.execute(createTable)
    except Error as e:
        print(e)
    return conn

def main():
    database = r'C:/programinngProjects/newSqliteProject/users.sqlite'

    createUsersTable =   '''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                firstName TEXT NOT NULL,
                                lastName TEXT NOT NULL
                            );'''

    createUsersGameTable='''CREATE TABLE IF NOT EXISTS gameUsers (
                                userId INTEGER NOT NULL,
                                gameId INTEGER NOT NULL
                            );'''

    createGameTable ='''CREATE TABLE IF NOT EXISTS games (
                            id INTEGER PRIMARY KEY,
                            gameName TEXT NOT NULL,
                            gameStudio
                        );'''

    conn = createConnection(database)

    if conn is not None:
        createTable(conn, createUsersTable)
        createTable(conn, createUsersGameTable)
        createTable(conn, createGameTable)
    else:
        print('Error, connection failed')

def insertUser(conn, user):
    sql ='''INSERT INTO users(firstName, lastName)
            VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def insertGameUser(conn, gameUser):
    sql ='''INSERT INTO gameUsers(userId, gameId)
            VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, gameUser)
    conn.commit()
    return cur.lastrowid

def insertGame(conn, game):
    sql ='''INSERT INTO games(gameName, gameStudio)
            VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, game)
    conn.commit()
    return cur.lastrowid

def masterUserInserter(firstName, lastName):
    database = r'C:/programinngProjects/newSqliteProject/users.sqlite'

    conn = createConnection(database)
    with conn:
        user = (firstName, lastName)
        insertUser(conn, user)

def masterGameUserInserter(gameId, userId):
    database = r'C:/programinngProjects/newSqliteProject/users.sqlite'

    conn = createConnection(database)
    with conn:
        ids = (gameId, userId)
        insertGameUser(conn, ids)

def masterGameInserter(gameName, gameStudio):
    database = r'C:/programinngProjects/newSqliteProject/users.sqlite'

    conn = createConnection(database)
    with conn:
        game = (gameName, gameStudio)
        insertGame(conn, game)

def userHandler():
    firstName = entry01.get()
    lastName = entry02.get()

    if len(firstName) == 0:
        print('Error, name invalid')
    elif len(lastName) == 0:
        print('Error, name invalid')
    else:
        masterUserInserter(firstName, lastName)

def gameUserHandler():
    gameId = entry03.get()
    userId = entry04.get()

    if isinstance(gameId, int) != True:
        print('Error, gameId is not a number')
    elif isinstance(userId, int) != True:
        print('Error, userId is not a number')
    else:
        masterGameUserInserter(gameId, userId)

def gameHandler():
    gameName = entry05.get()
    gameStudio = entry06.get()

    if len(gameName) == 0:
        print('Error, game name is invalid')
    elif len(gameStudio) == 0:
        print('Error, game studio name is invalid')
    else: masterGameInserter(gameName, gameStudio)

window = Tk()
window.geometry('300x220')

#Tab manager
masterTab = ttk.Notebook(window)

tab01 = ttk.Frame(masterTab)
tab02 = ttk.Frame(masterTab)
tab03 = ttk.Frame(masterTab)
tab04 = ttk.Frame(masterTab)

masterTab.add(tab01, text='Users')
masterTab.add(tab02, text='Users/Games')
masterTab.add(tab03, text='Games')
masterTab.add(tab04, text='Tables')

masterTab.pack(expand=1, fill='both')
#Tab manager [END]
#users tab
label01 = ttk.Label(tab01, text='first name')
label01.grid(column=0, row=0, sticky='W')

label02 = ttk.Label(tab01, text='last name')
label02.grid(column=0, row=1, sticky='W')

firstName = StringVar()
entry01 = ttk.Entry(tab01, textvariable=firstName)
entry01.grid(column=1, row=0)

lastName = StringVar()
entry02 = ttk.Entry(tab01, textvariable=lastName)
entry02.grid(column=1, row=1)

button01 = ttk.Button(tab01, text='Press me!', command=userHandler)
button01.grid(column=0, row=2, sticky='W')
#users tab [END]
#game/users tab
label03 = ttk.Label(tab02, text='user id')
label03.grid(column=0, row=0, sticky='W')

label04 = ttk.Label(tab02, text='game id')
label04.grid(column=0, row=1, sticky='W')

userId = IntVar()
entry03 = ttk.Entry(tab02, textvariable=userId)
entry03.grid(column=1, row=0, sticky='W')

gameId = IntVar()
entry04 = ttk.Entry(tab02, textvariable=gameId)
entry04.grid(column=1, row=1, sticky='W')

button02 = ttk.Button(tab02, text='Press me!', command=gameUserHandler)
button02.grid(column=0, row=2, sticky='W')
#game/users tab [END]
#games tab
label05 = ttk.Label(tab03, text='name')
label05.grid(column=0, row=0, sticky='W')

label06 = ttk.Label(tab03, text='studio')
label06.grid(column=0, row=1, sticky='W')

gameName = StringVar()
entry05 = ttk.Entry(tab03, textvariable=gameName)
entry05.grid(column=1, row=0, sticky='W')

gameStudio = StringVar()
entry06 = ttk.Entry(tab03, textvariable=gameStudio)
entry06.grid(column=1, row=1, sticky='W')

button03 = ttk.Button(tab03, text='Press me!', command=gameHandler)
button03.grid(column=0, row=2, sticky='W')
#games tab [END]
#create table tab
button04 = ttk.Button(tab04, text='Create tables', command=main)
button04.grid(column=0,row=0)
window.mainloop()