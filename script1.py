import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # cur.execute("INSERT INTO store VALUES ('wine glass',8,10.5)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('wine glass',8,10.5)")
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


# insert("water glass", 10, 5)
insert("coffee cup", 10, 5)


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # SAVING ALL THE DATA SET TO BE FETCHED INTO A VARIABLE CALLED ROWS AS THEY ARE IN ROWS FUNNY
    rows = cur.fetchall()
    conn.close()
    # we are just collecting/fetching data so no need of commit method
    return rows


print(view())
