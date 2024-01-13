import sqlite3
# maak connectie met databse, asl die nog niet bestaat maak die aan
con = sqlite3.connect('school.db')
cur = con.cursor()  # een cursor object aanmaken om sql querys uit te voeren
cur.execute('''
CREATE TABLE IF NOT EXISTS Students(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT,
            LastName TEXT
)
''')  # table aanmaken

data = [
    ('Oscar', 'Alexander'),
    ('Max', 'Verstappen'),
    ('Kamar', 'La')
]

cur.executemany('''
INSERT INTO Students (FirstName,LastName)
VALUES (?,?)
''', data)  # zet de data in de table

# sla ze op en sluit de verbinding
con.commit()
con.close()

print('done')
