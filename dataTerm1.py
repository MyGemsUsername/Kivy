import pyodbc
Y9T1topics = []
Y9T1hosts = []
Y9T1presenters = []
Y8T1topics = []
Y8T1hosts = []
Y8T1presenters = []
Y7T1topics = []
Y7T1hosts = []
Y7T1presenters = []
Y6T1topics = []
Y6T1hosts = []
Y6T1presenters = []

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Muhammad Aufa\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)

    cur = conn.cursor()
    cur.execute('SELECT * FROM Term1')

    for row in cur.fetchall():
        Y9T1topic = row[1]
        Y9T1host= row[2]
        Y9T1presenter = row[3]
        Y8T1topic = row[4]
        Y8T1host= row[5]
        Y8T1presenter = row[6]
        Y7T1topic = row[7]
        Y7T1host= row[8]
        Y7T1presenter = row[9]  
        Y6T1topic = row[10]
        Y6T1host= row[11]
        Y6T1presenter = row[12]
        # ----------------------------------------------------
        Y9T1topics.append(Y9T1topic)
        Y9T1hosts.append(Y9T1host)
        Y9T1presenters.append(Y9T1presenter)
        Y8T1topics.append(Y8T1topic)
        Y8T1hosts.append(Y8T1host)
        Y8T1presenters.append(Y8T1presenter)
        Y7T1topics.append(Y7T1topic)
        Y7T1hosts.append(Y7T1host)
        Y7T1presenters.append(Y7T1presenter)
        Y6T1topics.append(Y6T1topic)
        Y6T1hosts.append(Y6T1host)
        Y6T1presenters.append(Y6T1presenter)


except pyodbc.Error as e:
    print("Error in Connection",e)

# ALL TOPICS --------------------------------------------------------------------
Y9T1topic1 = Y9T1topics[0]
Y9T1topic2 = Y9T1topics[1]
Y9T1topic3 = Y9T1topics[2]
Y9T1topic4 = Y9T1topics[3]
Y9T1topic5 = Y9T1topics[4]
Y9T1topic6 = Y9T1topics[5]
Y9T1topic7 = Y9T1topics[6]
Y9T1topic8 = Y9T1topics[7]
Y9T1topic9 = Y9T1topics[8]
Y9T1topic10 = Y9T1topics[9]
Y9T1topic11 = Y9T1topics[10]
Y9T1topic12 = Y9T1topics[11]
Y9T1topic13 = Y9T1topics[12]
Y9T1topic14 = Y9T1topics[13]

Y8T1topic1 = Y8T1topics[0]
Y8T1topic2 = Y8T1topics[1]
Y8T1topic3 = Y8T1topics[2]
Y8T1topic4 = Y8T1topics[3]
Y8T1topic5 = Y8T1topics[4]
Y8T1topic6 = Y8T1topics[5]
Y8T1topic7 = Y8T1topics[6]
Y8T1topic8 = Y8T1topics[7]
Y8T1topic9 = Y8T1topics[8]
Y8T1topic10 = Y8T1topics[9]
Y8T1topic11 = Y8T1topics[10]
Y8T1topic12 = Y8T1topics[11]
Y8T1topic13 = Y8T1topics[12]
Y8T1topic14 = Y8T1topics[13]

Y7T1topic1 = Y7T1topics[0]
Y7T1topic2 = Y7T1topics[1]
Y7T1topic3 = Y7T1topics[2]
Y7T1topic4 = Y7T1topics[3]
Y7T1topic5 = Y7T1topics[4]
Y7T1topic6 = Y7T1topics[5]
Y7T1topic7 = Y7T1topics[6]
Y7T1topic8 = Y7T1topics[7]
Y7T1topic9 = Y7T1topics[8]
Y7T1topic10 = Y7T1topics[9]
Y7T1topic11 = Y7T1topics[10]
Y7T1topic12 = Y7T1topics[11]
Y7T1topic13 = Y7T1topics[12]
Y7T1topic14 = Y7T1topics[13]

Y6T1topic1 = Y6T1topics[0]
Y6T1topic2 = Y6T1topics[1]
Y6T1topic3 = Y6T1topics[2]
Y6T1topic4 = Y6T1topics[3]
Y6T1topic5 = Y6T1topics[4]
Y6T1topic6 = Y6T1topics[5]
Y6T1topic7 = Y6T1topics[6]
Y6T1topic8 = Y6T1topics[7]
Y6T1topic9 = Y6T1topics[8]
Y6T1topic10 = Y6T1topics[9]
Y6T1topic11 = Y6T1topics[10]
Y6T1topic12 = Y6T1topics[11]
Y6T1topic13 = Y6T1topics[12]
Y6T1topic14 = Y6T1topics[13]

# ALL HOSTS ------------------------------------------------------------------
Y9T1host1 = Y9T1hosts[0]
Y9T1host2 = Y9T1hosts[1]
Y9T1host3 = Y9T1hosts[2]
Y9T1host4 = Y9T1hosts[3]
Y9T1host5 = Y9T1hosts[4]
Y9T1host6 = Y9T1hosts[5]
Y9T1host7 = Y9T1hosts[6]
Y9T1host8 = Y9T1hosts[7]
Y9T1host9 = Y9T1hosts[8]
Y9T1host10 = Y9T1hosts[9]
Y9T1host11 = Y9T1hosts[10]
Y9T1host12 = Y9T1hosts[11]
Y9T1host13 = Y9T1hosts[12]
Y9T1host14 = Y9T1hosts[13]

Y8T1host1 = Y8T1hosts[0]
Y8T1host2 = Y8T1hosts[1]
Y8T1host3 = Y8T1hosts[2]
Y8T1host4 = Y8T1hosts[3]
Y8T1host5 = Y8T1hosts[4]
Y8T1host6 = Y8T1hosts[5]
Y8T1host7 = Y8T1hosts[6]
Y8T1host8 = Y8T1hosts[7]
Y8T1host9 = Y8T1hosts[8]
Y8T1host10 = Y8T1hosts[9]
Y8T1host11 = Y8T1hosts[10]
Y8T1host12 = Y8T1hosts[11]
Y8T1host13 = Y8T1hosts[12]
Y8T1host14 = Y8T1hosts[13]

Y7T1host1 = Y7T1hosts[0]
Y7T1host2 = Y7T1hosts[1]
Y7T1host3 = Y7T1hosts[2]
Y7T1host4 = Y7T1hosts[3]
Y7T1host5 = Y7T1hosts[4]
Y7T1host6 = Y7T1hosts[5]
Y7T1host7 = Y7T1hosts[6]
Y7T1host8 = Y7T1hosts[7]
Y7T1host9 = Y7T1hosts[8]
Y7T1host10 = Y7T1hosts[9]
Y7T1host11 = Y7T1hosts[10]
Y7T1host12 = Y7T1hosts[11]
Y7T1host13 = Y7T1hosts[12]
Y7T1host14 = Y7T1hosts[13]

Y6T1host1 = Y6T1hosts[0]
Y6T1host2 = Y6T1hosts[1]
Y6T1host3 = Y6T1hosts[2]
Y6T1host4 = Y6T1hosts[3]
Y6T1host5 = Y6T1hosts[4]
Y6T1host6 = Y6T1hosts[5]
Y6T1host7 = Y6T1hosts[6]
Y6T1host8 = Y6T1hosts[7]
Y6T1host9 = Y6T1hosts[8]
Y6T1host10 = Y6T1hosts[9]
Y6T1host11 = Y6T1hosts[10]
Y6T1host12 = Y6T1hosts[11]
Y6T1host13 = Y6T1hosts[12]
Y6T1host14 = Y6T1hosts[13]
# ALL PRESENTERS =========================================================================== 
Y9T1presenter1 = Y9T1presenters[0]
Y9T1presenter2 = Y9T1presenters[1]
Y9T1presenter3 = Y9T1presenters[2]
Y9T1presenter4 = Y9T1presenters[3]
Y9T1presenter5 = Y9T1presenters[4]
Y9T1presenter6 = Y9T1presenters[5]
Y9T1presenter7 = Y9T1presenters[6]
Y9T1presenter8 = Y9T1presenters[7]
Y9T1presenter9 = Y9T1presenters[8]
Y9T1presenter10 = Y9T1presenters[9]
Y9T1presenter11 = Y9T1presenters[10]
Y9T1presenter12 = Y9T1presenters[11]
Y9T1presenter13 = Y9T1presenters[12]
Y9T1presenter14 = Y9T1presenters[13]

Y8T1presenter1 = Y8T1presenters[0]
Y8T1presenter2 = Y8T1presenters[1]
Y8T1presenter3 = Y8T1presenters[2]
Y8T1presenter4 = Y8T1presenters[3]
Y8T1presenter5 = Y8T1presenters[4]
Y8T1presenter6 = Y8T1presenters[5]
Y8T1presenter7 = Y8T1presenters[6]
Y8T1presenter8 = Y8T1presenters[7]
Y8T1presenter9 = Y8T1presenters[8]
Y8T1presenter10 = Y8T1presenters[9]
Y8T1presenter11 = Y8T1presenters[10]
Y8T1presenter12 = Y8T1presenters[11]
Y8T1presenter13 = Y8T1presenters[12]
Y8T1presenter14 = Y8T1presenters[13]

Y7T1presenter1 = Y7T1presenters[0]
Y7T1presenter2 = Y7T1presenters[1]
Y7T1presenter3 = Y7T1presenters[2]
Y7T1presenter4 = Y7T1presenters[3]
Y7T1presenter5 = Y7T1presenters[4]
Y7T1presenter6 = Y7T1presenters[5]
Y7T1presenter7 = Y7T1presenters[6]
Y7T1presenter8 = Y7T1presenters[7]
Y7T1presenter9 = Y7T1presenters[8]
Y7T1presenter10 = Y7T1presenters[9]
Y7T1presenter11 = Y7T1presenters[10]
Y7T1presenter12 = Y7T1presenters[11]
Y7T1presenter13 = Y7T1presenters[12]
Y7T1presenter14 = Y7T1presenters[13]

Y6T1presenter1 = Y6T1presenters[0]
Y6T1presenter2 = Y6T1presenters[1]
Y6T1presenter3 = Y6T1presenters[2]
Y6T1presenter4 = Y6T1presenters[3]
Y6T1presenter5 = Y6T1presenters[4]
Y6T1presenter6 = Y6T1presenters[5]
Y6T1presenter7 = Y6T1presenters[6]
Y6T1presenter8 = Y6T1presenters[7]
Y6T1presenter9 = Y6T1presenters[8]
Y6T1presenter10 = Y6T1presenters[9]
Y6T1presenter11 = Y6T1presenters[10]
Y6T1presenter12 = Y6T1presenters[11]
Y6T1presenter13 = Y6T1presenters[12]
Y6T1presenter14 = Y6T1presenters[13]

