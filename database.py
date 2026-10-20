import sqlite3

DB_NAME = "academy.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            xp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            user_id TEXT,
            lesson_id INTEGER,
            completed INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, lesson_id)
        )
    """)

    conn.commit()
    conn.close()


def register_user(user_id, username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username)
        VALUES (?, ?)
    """, (user_id, username))

    conn.commit()
    conn.close()


def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, username, xp, level FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def add_xp(user_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET xp = xp + ?
        WHERE user_id = ?
    """, (amount, user_id))

    conn.commit()
    conn.close()