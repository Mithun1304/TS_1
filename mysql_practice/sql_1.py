import mysql.connector

#establishing the connection
mydb = mysql.connector.connect (
    user = 'root',
    password = 'venigalla123',
    host = '127,0,0,1',
    database = 'customer'
)
