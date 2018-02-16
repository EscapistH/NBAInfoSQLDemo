# encoding:utf-8

import sqlite3


def create_sql():
    conn = sqlite3.connect('playerinfo.db')
    cursor = conn.cursor()
    cursor.execute(
        'create table playerinfo (id int primary key, name varchar (20), team varchar(20), number varchar(20), '
        'seat varchar(20), hight varchar(20))')
    cursor.close()
    conn.commit()
    conn.close()


def insert_player(idn, name, team, number, seat, hight):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('insert into playerinfo values (?, ?, ?, ?, ?, ?)', (idn, name, team, number, seat, hight))
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def delete_player(name):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('delete from playerinfo where name = ?', name)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def change_team(new, name):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('update playerinfo set team = ? where name = ?', (new, name))
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def change_number(new, name):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('update playerinfo set number = ? where name = ?', (new, name))
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def change_seat(new, name):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('update playerinfo set seat = ? where name = ?', (new, name))
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def change_hight(new, name):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('update playerinfo set hight = ? where name = ?', (new, name))
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def search_player(name):
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('select * from playerinfo where name=?', (name,))
        values = cursor.fetchall()
        print(values)
    finally:
        cursor.close()
        conn.close()


def search_all():
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        cursor.execute('select * from playerinfo')
        values = cursor.fetchall()
        for value in values:
            print(value)
    finally:
        cursor.close()
        conn.close()


def get_row():
    try:
        conn = sqlite3.connect('playerinfo.db')
        cursor = conn.cursor()
        row = cursor.rowcount
        return row
    finally:
        cursor.close()
        conn.close()
