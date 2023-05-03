import pyodbc
Y9T2topics = []
Y9T2hosts = []
Y9T2presenters = []
Y8T2topics = []
Y8T2hosts = []
Y8T2presenters = []
Y7T2topics = []
Y7T2hosts = []
Y7T2presenters = []
Y6T2topics = []
Y6T2hosts = []
Y6T2presenters = []

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Muhammad Aufa\Documents\pydb.accdb;'
    conn = pyodbc.connect(con_string)

    cur = conn.cursor()
    cur.execute('SELECT * FROM Term2')

    for row in cur.fetchall():
        Y9T2topic = row[1]
        Y9T2host= row[2]
        Y9T2presenter = row[3]
        Y8T2topic = row[4]
        Y8T2host= row[5]
        Y8T2presenter = row[6]
        Y7T2topic = row[7]
        Y7T2host= row[8]
        Y7T2presenter = row[9]  
        Y6T2topic = row[10]
        Y6T2host= row[11]
        Y6T2presenter = row[12]
        # ----------------------------------------------------
        Y9T2topics.append(Y9T2topic)
        Y9T2hosts.append(Y9T2host)
        Y9T2presenters.append(Y9T2presenter)
        Y8T2topics.append(Y8T2topic)
        Y8T2hosts.append(Y8T2host)
        Y8T2presenters.append(Y8T2presenter)
        Y7T2topics.append(Y7T2topic)
        Y7T2hosts.append(Y7T2host)
        Y7T2presenters.append(Y7T2presenter)
        Y6T2topics.append(Y6T2topic)
        Y6T2hosts.append(Y6T2host)
        Y6T2presenters.append(Y6T2presenter)

except pyodbc.Error as e:
    print("Error in Connection",e)

# ALL TOPICS --------------------------------------------------------------------
Y9T2topic1 = Y9T2topics[0]
Y9T2topic2 = Y9T2topics[1]
Y9T2topic3 = Y9T2topics[2]
Y9T2topic4 = Y9T2topics[3]
Y9T2topic5 = Y9T2topics[4]
Y9T2topic6 = Y9T2topics[5]
Y9T2topic7 = Y9T2topics[6]
Y9T2topic8 = Y9T2topics[7]
Y9T2topic9 = Y9T2topics[8]
Y9T2topic10 = Y9T2topics[9]
Y9T2topic11 = Y9T2topics[10]
Y9T2topic12 = Y9T2topics[11]

Y8T2topic1 = Y8T2topics[0]
Y8T2topic2 = Y8T2topics[1]
Y8T2topic3 = Y8T2topics[2]
Y8T2topic4 = Y8T2topics[3]
Y8T2topic5 = Y8T2topics[4]
Y8T2topic6 = Y8T2topics[5]
Y8T2topic7 = Y8T2topics[6]
Y8T2topic8 = Y8T2topics[7]
Y8T2topic9 = Y8T2topics[8]
Y8T2topic10 = Y8T2topics[9]
Y8T2topic11 = Y8T2topics[10]
Y8T2topic12 = Y8T2topics[11]

Y7T2topic1 = Y7T2topics[0]
Y7T2topic2 = Y7T2topics[1]
Y7T2topic3 = Y7T2topics[2]
Y7T2topic4 = Y7T2topics[3]
Y7T2topic5 = Y7T2topics[4]
Y7T2topic6 = Y7T2topics[5]
Y7T2topic7 = Y7T2topics[6]
Y7T2topic8 = Y7T2topics[7]
Y7T2topic9 = Y7T2topics[8]
Y7T2topic10 = Y7T2topics[9]
Y7T2topic11 = Y7T2topics[10]
Y7T2topic12 = Y7T2topics[11]

Y6T2topic1 = Y6T2topics[0]
Y6T2topic2 = Y6T2topics[1]
Y6T2topic3 = Y6T2topics[2]
Y6T2topic4 = Y6T2topics[3]
Y6T2topic5 = Y6T2topics[4]
Y6T2topic6 = Y6T2topics[5]
Y6T2topic7 = Y6T2topics[6]
Y6T2topic8 = Y6T2topics[7]
Y6T2topic9 = Y6T2topics[8]
Y6T2topic10 = Y6T2topics[9]
Y6T2topic11 = Y6T2topics[10]
Y6T2topic12 = Y6T2topics[11]

# ALL HOSTS ------------------------------------------------------------------
Y9T2host1 = Y9T2hosts[0]
Y9T2host2 = Y9T2hosts[1]
Y9T2host3 = Y9T2hosts[2]
Y9T2host4 = Y9T2hosts[3]
Y9T2host5 = Y9T2hosts[4]
Y9T2host6 = Y9T2hosts[5]
Y9T2host7 = Y9T2hosts[6]
Y9T2host8 = Y9T2hosts[7]
Y9T2host9 = Y9T2hosts[8]
Y9T2host10 = Y9T2hosts[9]
Y9T2host11 = Y9T2hosts[10]
Y9T2host12 = Y9T2hosts[11]

Y8T2host1 = Y8T2hosts[0]
Y8T2host2 = Y8T2hosts[1]
Y8T2host3 = Y8T2hosts[2]
Y8T2host4 = Y8T2hosts[3]
Y8T2host5 = Y8T2hosts[4]
Y8T2host6 = Y8T2hosts[5]
Y8T2host7 = Y8T2hosts[6]
Y8T2host8 = Y8T2hosts[7]
Y8T2host9 = Y8T2hosts[8]
Y8T2host10 = Y8T2hosts[9]
Y8T2host11 = Y8T2hosts[10]
Y8T2host12 = Y8T2hosts[11]

Y7T2host1 = Y7T2hosts[0]
Y7T2host2 = Y7T2hosts[1]
Y7T2host3 = Y7T2hosts[2]
Y7T2host4 = Y7T2hosts[3]
Y7T2host5 = Y7T2hosts[4]
Y7T2host6 = Y7T2hosts[5]
Y7T2host7 = Y7T2hosts[6]
Y7T2host8 = Y7T2hosts[7]
Y7T2host9 = Y7T2hosts[8]
Y7T2host10 = Y7T2hosts[9]
Y7T2host11 = Y7T2hosts[10]
Y7T2host12 = Y7T2hosts[11]

Y6T2host1 = Y6T2hosts[0]
Y6T2host2 = Y6T2hosts[1]
Y6T2host3 = Y6T2hosts[2]
Y6T2host4 = Y6T2hosts[3]
Y6T2host5 = Y6T2hosts[4]
Y6T2host6 = Y6T2hosts[5]
Y6T2host7 = Y6T2hosts[6]
Y6T2host8 = Y6T2hosts[7]
Y6T2host9 = Y6T2hosts[8]
Y6T2host10 = Y6T2hosts[9]
Y6T2host11 = Y6T2hosts[10]
Y6T2host12 = Y6T2hosts[11]
# ALL PRESENTERS =========================================================================== 
Y9T2presenter1 = Y9T2presenters[0]
Y9T2presenter2 = Y9T2presenters[1]
Y9T2presenter3 = Y9T2presenters[2]
Y9T2presenter4 = Y9T2presenters[3]
Y9T2presenter5 = Y9T2presenters[4]
Y9T2presenter6 = Y9T2presenters[5]
Y9T2presenter7 = Y9T2presenters[6]
Y9T2presenter8 = Y9T2presenters[7]
Y9T2presenter9 = Y9T2presenters[8]
Y9T2presenter10 = Y9T2presenters[9]
Y9T2presenter11 = Y9T2presenters[10]
Y9T2presenter12 = Y9T2presenters[11]

Y8T2presenter1 = Y8T2presenters[0]
Y8T2presenter2 = Y8T2presenters[1]
Y8T2presenter3 = Y8T2presenters[2]
Y8T2presenter4 = Y8T2presenters[3]
Y8T2presenter5 = Y8T2presenters[4]
Y8T2presenter6 = Y8T2presenters[5]
Y8T2presenter7 = Y8T2presenters[6]
Y8T2presenter8 = Y8T2presenters[7]
Y8T2presenter9 = Y8T2presenters[8]
Y8T2presenter10 = Y8T2presenters[9]
Y8T2presenter11 = Y8T2presenters[10]
Y8T2presenter12 = Y8T2presenters[11]

Y7T2presenter1 = Y7T2presenters[0]
Y7T2presenter2 = Y7T2presenters[1]
Y7T2presenter3 = Y7T2presenters[2]
Y7T2presenter4 = Y7T2presenters[3]
Y7T2presenter5 = Y7T2presenters[4]
Y7T2presenter6 = Y7T2presenters[5]
Y7T2presenter7 = Y7T2presenters[6]
Y7T2presenter8 = Y7T2presenters[7]
Y7T2presenter9 = Y7T2presenters[8]
Y7T2presenter10 = Y7T2presenters[9]
Y7T2presenter11 = Y7T2presenters[10]
Y7T2presenter12 = Y7T2presenters[11]

Y6T2presenter1 = Y6T2presenters[0]
Y6T2presenter2 = Y6T2presenters[1]
Y6T2presenter3 = Y6T2presenters[2]
Y6T2presenter4 = Y6T2presenters[3]
Y6T2presenter5 = Y6T2presenters[4]
Y6T2presenter6 = Y6T2presenters[5]
Y6T2presenter7 = Y6T2presenters[6]
Y6T2presenter8 = Y6T2presenters[7]
Y6T2presenter9 = Y6T2presenters[8]
Y6T2presenter10 = Y6T2presenters[9]
Y6T2presenter11 = Y6T2presenters[10]
Y6T2presenter12 = Y6T2presenters[11]

