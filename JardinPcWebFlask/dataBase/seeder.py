import sqlite3 as sql 

DB_PATH = "jardinPC.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute ("""CREATE TABLE IF NOT EXISTS jardinPC(
        code INTEGER, 
        image STRING,
        name STRING,
        price REAL,
        description TEXT)""")
    conn.commit()     
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor=conn.cursor()
    data=[(1, "CPU UNO", "Pentium 1", 10, "CPU Vieja"),
          (2, "CPU DOS", "LENOVO", 20, "CPU NUEVA"),
          (1, "CPU TRES", "MAC", 30, "CPU MUY NUEVA")]
    cursor.executemany("""INSERT INTO jardinPC VALUES (?, ?, ?, ?, ?)""", data)
    conn.commit()     
    conn.close()
        
if __name__ == "__main__":
     createDB()
     addValues()