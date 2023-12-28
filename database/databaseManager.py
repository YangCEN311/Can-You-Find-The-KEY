import sqlite3

class dbManager:
    path = ".\database\example.db"
    def __init__(self):
        #create database
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scoreboard (
                id INTEGER PRIMARY KEY,
                username TEXT,
                score INT
            )
        ''')
        conn.commit()
        conn.close()
        
    def insert(self, username, score):
        #insert data
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        
        #delete the lowest score, if the data count is over 50
        cursor.execute("SELECT COUNT(*) FROM scoreboard")
        data_count = cursor.fetchone()[0]
        if(data_count >= 50):
            cursor.execute("DELETE FROM scoreboard WHERE score = (SELECT MIN(score) FROM scoreboard")
            
        cursor.execute("INSERT INTO scoreboard (username, score) VALUES (?, ?)", (f"{username}", f"{score}"))
        conn.commit()
        conn.close()

    def search(self):
        #search data, and sort it, then return it
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM scoreboard ORDER BY score DESC")
        conn.commit()
        sorted_users = cursor.fetchall()
        return sorted_users


