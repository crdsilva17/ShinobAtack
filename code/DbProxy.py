import sqlite3


class DbProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS dados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        date TEXT NOT NULL)
        '''
                          )

    def save(self, score_dct: dict):
        self.conn.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dct)
        self.conn.commit()

    def retrieve_top10(self) -> list:
        return self.conn.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.conn.close()
