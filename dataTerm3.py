import pyodbc
Y9T3topics = []
Y9T3hosts = []
Y9T3presenters = []
Y8T3topics = []
Y8T3hosts = []
Y8T3presenters = []
Y7T3topics = []
Y7T3hosts = []
Y7T3presenters = []
Y6T3topics = []
Y6T3hosts = []
Y6T3presenters = []

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Muhammad Aufa\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)

    cur = conn.cursor()
    cur.execute('SELECT * FROM Term3')

    for row in cur.fetchall():
        Y9T3topic = row[1]
        Y9T3host= row[2]
        Y9T3presenter = row[3]
        Y8T3topic = row[4]
        Y8T3host= row[5]
        Y8T3presenter = row[6]
        Y7T3topic = row[7]
        Y7T3host= row[8]
        Y7T3presenter = row[9]  
        Y6T3topic = row[10]
        Y6T3host= row[11]
        Y6T3presenter = row[12]
        # ----------------------------------------------------
        Y9T3topics.append(Y9T3topic)
        Y9T3hosts.append(Y9T3host)
        Y9T3presenters.append(Y9T3presenter)
        Y8T3topics.append(Y8T3topic)
        Y8T3hosts.append(Y8T3host)
        Y8T3presenters.append(Y8T3presenter)
        Y7T3topics.append(Y7T3topic)
        Y7T3hosts.append(Y7T3host)
        Y7T3presenters.append(Y7T3presenter)
        Y6T3topics.append(Y6T3topic)
        Y6T3hosts.append(Y6T3host)
        Y6T3presenters.append(Y6T3presenter)

except pyodbc.Error as e:
    print("Error in Connection",e)

# ALL TOPICS --------------------------------------------------------------------
Y9T3topic1 = Y9T3topics[0]
Y9T3topic2 = Y9T3topics[1]
Y9T3topic3 = Y9T3topics[2]
Y9T3topic4 = Y9T3topics[3]
Y9T3topic5 = Y9T3topics[4]
Y9T3topic6 = Y9T3topics[5]
Y9T3topic7 = Y9T3topics[6]
Y9T3topic8 = Y9T3topics[7]
Y9T3topic9 = Y9T3topics[8]
Y9T3topic10 = Y9T3topics[9]
Y9T3topic11 = Y9T3topics[10]
Y9T3topic12 = Y9T3topics[11]

Y8T3topic1 = Y8T3topics[0]
Y8T3topic2 = Y8T3topics[1]
Y8T3topic3 = Y8T3topics[2]
Y8T3topic4 = Y8T3topics[3]
Y8T3topic5 = Y8T3topics[4]
Y8T3topic6 = Y8T3topics[5]
Y8T3topic7 = Y8T3topics[6]
Y8T3topic8 = Y8T3topics[7]
Y8T3topic9 = Y8T3topics[8]
Y8T3topic10 = Y8T3topics[9]
Y8T3topic11 = Y8T3topics[10]
Y8T3topic12 = Y8T3topics[11]

Y7T3topic1 = Y7T3topics[0]
Y7T3topic2 = Y7T3topics[1]
Y7T3topic3 = Y7T3topics[2]
Y7T3topic4 = Y7T3topics[3]
Y7T3topic5 = Y7T3topics[4]
Y7T3topic6 = Y7T3topics[5]
Y7T3topic7 = Y7T3topics[6]
Y7T3topic8 = Y7T3topics[7]
Y7T3topic9 = Y7T3topics[8]
Y7T3topic10 = Y7T3topics[9]
Y7T3topic11 = Y7T3topics[10]
Y7T3topic12 = Y7T3topics[11]

Y6T3topic1 = Y6T3topics[0]
Y6T3topic2 = Y6T3topics[1]
Y6T3topic3 = Y6T3topics[2]
Y6T3topic4 = Y6T3topics[3]
Y6T3topic5 = Y6T3topics[4]
Y6T3topic6 = Y6T3topics[5]
Y6T3topic7 = Y6T3topics[6]
Y6T3topic8 = Y6T3topics[7]
Y6T3topic9 = Y6T3topics[8]
Y6T3topic10 = Y6T3topics[9]
Y6T3topic11 = Y6T3topics[10]
Y6T3topic12 = Y6T3topics[11]

# ALL HOSTS ------------------------------------------------------------------
Y9T3host1 = Y9T3hosts[0]
Y9T3host2 = Y9T3hosts[1]
Y9T3host3 = Y9T3hosts[2]
Y9T3host4 = Y9T3hosts[3]
Y9T3host5 = Y9T3hosts[4]
Y9T3host6 = Y9T3hosts[5]
Y9T3host7 = Y9T3hosts[6]
Y9T3host8 = Y9T3hosts[7]
Y9T3host9 = Y9T3hosts[8]
Y9T3host10 = Y9T3hosts[9]
Y9T3host11 = Y9T3hosts[10]
Y9T3host12 = Y9T3hosts[11]

Y8T3host1 = Y8T3hosts[0]
Y8T3host2 = Y8T3hosts[1]
Y8T3host3 = Y8T3hosts[2]
Y8T3host4 = Y8T3hosts[3]
Y8T3host5 = Y8T3hosts[4]
Y8T3host6 = Y8T3hosts[5]
Y8T3host7 = Y8T3hosts[6]
Y8T3host8 = Y8T3hosts[7]
Y8T3host9 = Y8T3hosts[8]
Y8T3host10 = Y8T3hosts[9]
Y8T3host11 = Y8T3hosts[10]
Y8T3host12 = Y8T3hosts[11]

Y7T3host1 = Y7T3hosts[0]
Y7T3host2 = Y7T3hosts[1]
Y7T3host3 = Y7T3hosts[2]
Y7T3host4 = Y7T3hosts[3]
Y7T3host5 = Y7T3hosts[4]
Y7T3host6 = Y7T3hosts[5]
Y7T3host7 = Y7T3hosts[6]
Y7T3host8 = Y7T3hosts[7]
Y7T3host9 = Y7T3hosts[8]
Y7T3host10 = Y7T3hosts[9]
Y7T3host11 = Y7T3hosts[10]
Y7T3host12 = Y7T3hosts[11]

Y6T3host1 = Y6T3hosts[0]
Y6T3host2 = Y6T3hosts[1]
Y6T3host3 = Y6T3hosts[2]
Y6T3host4 = Y6T3hosts[3]
Y6T3host5 = Y6T3hosts[4]
Y6T3host6 = Y6T3hosts[5]
Y6T3host7 = Y6T3hosts[6]
Y6T3host8 = Y6T3hosts[7]
Y6T3host9 = Y6T3hosts[8]
Y6T3host10 = Y6T3hosts[9]
Y6T3host11 = Y6T3hosts[10]
Y6T3host12 = Y6T3hosts[11]
# ALL PRESENTERS =========================================================================== 
Y9T3presenter1 = Y9T3presenters[0]
Y9T3presenter2 = Y9T3presenters[1]
Y9T3presenter3 = Y9T3presenters[2]
Y9T3presenter4 = Y9T3presenters[3]
Y9T3presenter5 = Y9T3presenters[4]
Y9T3presenter6 = Y9T3presenters[5]
Y9T3presenter7 = Y9T3presenters[6]
Y9T3presenter8 = Y9T3presenters[7]
Y9T3presenter9 = Y9T3presenters[8]
Y9T3presenter10 = Y9T3presenters[9]
Y9T3presenter11 = Y9T3presenters[10]
Y9T3presenter12 = Y9T3presenters[11]

Y8T3presenter1 = Y8T3presenters[0]
Y8T3presenter2 = Y8T3presenters[1]
Y8T3presenter3 = Y8T3presenters[2]
Y8T3presenter4 = Y8T3presenters[3]
Y8T3presenter5 = Y8T3presenters[4]
Y8T3presenter6 = Y8T3presenters[5]
Y8T3presenter7 = Y8T3presenters[6]
Y8T3presenter8 = Y8T3presenters[7]
Y8T3presenter9 = Y8T3presenters[8]
Y8T3presenter10 = Y8T3presenters[9]
Y8T3presenter11 = Y8T3presenters[10]
Y8T3presenter12 = Y8T3presenters[11]

Y7T3presenter1 = Y7T3presenters[0]
Y7T3presenter2 = Y7T3presenters[1]
Y7T3presenter3 = Y7T3presenters[2]
Y7T3presenter4 = Y7T3presenters[3]
Y7T3presenter5 = Y7T3presenters[4]
Y7T3presenter6 = Y7T3presenters[5]
Y7T3presenter7 = Y7T3presenters[6]
Y7T3presenter8 = Y7T3presenters[7]
Y7T3presenter9 = Y7T3presenters[8]
Y7T3presenter10 = Y7T3presenters[9]
Y7T3presenter11 = Y7T3presenters[10]
Y7T3presenter12 = Y7T3presenters[11]

Y6T3presenter1 = Y6T3presenters[0]
Y6T3presenter2 = Y6T3presenters[1]
Y6T3presenter3 = Y6T3presenters[2]
Y6T3presenter4 = Y6T3presenters[3]
Y6T3presenter5 = Y6T3presenters[4]
Y6T3presenter6 = Y6T3presenters[5]
Y6T3presenter7 = Y6T3presenters[6]
Y6T3presenter8 = Y6T3presenters[7]
Y6T3presenter9 = Y6T3presenters[8]
Y6T3presenter10 = Y6T3presenters[9]
Y6T3presenter11 = Y6T3presenters[10]
Y6T3presenter12 = Y6T3presenters[11]

