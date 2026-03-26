import sqlite3, hashlib

def get_db()
    conn = sqlite3.connect("loja_users.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    return
