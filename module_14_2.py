import sqlite3

with open('not_telegram.db', 'a'):
    pass

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))
cursor.execute('DELETE FROM users WHERE id % 3 = 1')
cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances/total_users)

connect.commit()
connect.close()