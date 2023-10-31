# import pyodbc

# # Connexion à la base de données SQL Server

# DSN = 'Driver={SQL Server};Server=DESKTOP-6RB7ER5\\SQLEXPRESS;Database=product;Trusted_Connection=yes;'
# conn = pyodbc.connect(DSN)
# print(conn)


# def getData(DSN):
#     print("Read")
#     cursor = DSN.cursor()
#     cursor.execute("select * from Product")
#     for row in cursor:
#         print(f'(row)')


# def insertData(DSN):
#     print("Insert")
#     cursor = DSN.cursor()
#     cursor.execute(
#         'insert into Product (Nom,Descriptions,StockActuel,PrixUnitaire) values (?,?,?,?)'
#         ('Ram','Delhi',2,4))
    
#     DSN.commit()

# insertData(DSN)
# getData(DSN)