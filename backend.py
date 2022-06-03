import sqlite3

db = "books.db"

def connect():
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()

# my book list

# list = [
#         ("The Gift", "Eger Edith", 2020, 9781846046278),
#         ("Man's Search For Meaning", "Viktor E. Frankl", 2019,9781846041242),
#         ("12 Rules for Life. An antidote to chaos", "Jordan B. Peterson", 2019, 9780141988511),
#         ("The Choice", "Edith Eger", 2018, 9781846045127),
#         ("The 4-Hour Work Week", "Ferriss Timothy", 2020, 9781785043031),
#         ("The Power of Habit", "Charles Duhigg", 2019, 9781847946249),
#         ("Sapiens. A brief history of humankind", "Yuval Noah Harari", 2015, 9780099590088),
#         ("Brave New World", "Aldous Huxley", 2013, 9780099477464)
#         ]
#
# for i in list:
#     insert(i[0],i[1],i[2],i[3])

