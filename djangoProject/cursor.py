import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="",
    db="bookshop"
)
c = db.cursor()
c.execute("INSERT INTO books (title, in_stock, descr, price, picture) VALUES (%s, %s, %s, %s, %s);", ('Book', 0, 'very interesting book', 100, 'pic.jpg'))
db.commit()
c.close()
db.close()