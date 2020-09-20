import psycopg2


def create_table():
    # conn = psycopg2.connect("lite.db")
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='Post_Gres@1234' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # cur.execute("INSERT INTO store VALUES ('wine glass',8,10.5)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='Post_Gres@1234' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('wine glass',8,10.5)")
    # cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    cur.execute("INSERT INTO store VALUE('%s', '%s', '%s')" %
                (item, quantity, price))
    conn.commit()
    conn.close()


# insert("water glass", 10, 5)
# insert("wine glass", 10, 5)
# insert("coffee cup", 10, 5)


def view():
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # SAVING ALL THE DATA SET TO BE FETCHED INTO A VARIABLE CALLED ROWS AS THEY ARE IN ROWS FUNNY
    rows = cur.fetchall()
    conn.close()
    # we are just collecting/fetching data so no need of commit method
    return rows


# for deleting a record from the creating database

def delete(item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    # cur.execute("SELECT * FROM store")
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    # rows = cur.fetchall()
    conn.commit()
    conn.close()
    # return rows

# another func to update the records in the database


def update(quantity, price, item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()


# update(11, 6, "water glass")
# delete("coffee cup")
# print(view())
create_table()
insert("Apple", 10, 15)
