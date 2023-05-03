import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Muhammad Aufa\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("conencted looll")


except pyodbc.Error as e:
    print("Error in connection", e)