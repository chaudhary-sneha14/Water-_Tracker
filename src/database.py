import sqlite3
from datetime import datetime

DB_NAME="water_tracker.db"

def create_tables():
    conn=sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS water_intake(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        intake_ml INTEGER,
        date TEXT,
        time TEXT)
    """
    )

    conn.commit()
    conn.close()


def log_intake(user_id,intake_ml):
    conn=sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    cursor.execute("""
        INSERT INTO water_intake (user_id, intake_ml, date, time) VALUES(?, ?, ?, ?)
    """, (user_id, intake_ml, date, time))

    conn.commit()
    conn.close() 


def get_intake(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute("SELECT intake_ml, date, time FROM water_intake WHERE user_id = ?", (user_id,))
    
    records = cursor.fetchall()

    conn.close()     

    return records


create_tables()

# User enters 1500 ml
# ↓
# log_intake() saves it
# ↓
# analyze_intake() sends it to Gemini
# ↓
# AI returns feedback
# ↓
# get_intake() can show history later