import mysql.connector
'''
conn = mysql.connector.connect(user='UserName1', password='135792468', host='127.0.0.1', database='db1')

if conn.is_connected():
    print('Connected to MySQL database')

cursor = conn.cursor()

#query = "INSERT INTO `db1`.`hospitals` (`Name`, `addr`) VALUES ('Name06', 'addr6')"
#cursor.execute(query)

cursor.execute("SELECT * FROM db1.hospitals")

row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()


conn.close()

'''


def get_hospitals_with_service(service):
    conn = mysql.connector.connect(user='UserName1', password='135792468', host='127.0.0.1', database='db1')

    result_hosps = []

    if conn.is_connected():
        print('Connected to MySQL database')
    else:
        return []

    cursor = conn.cursor()

    if service != '':
        # cursor.execute(f"SELECT * FROM db1.hospitals WHERE db1.hospitals.service = '{service}'")
        cursor.execute(f'''SELECT *
FROM db1.hospitals h
WHERE h.id in (SELECT hs.id_hosp 
FROM db1.hosp_serv hs 
WHERE hs.id_serv = (SELECT s.id 
FROM db1.services s 
WHERE s.name = "{service}"));''')
    else:
        cursor.execute("SELECT * FROM db1.hospitals")

    row = cursor.fetchone()

    if row is None:
        print('None row')
        return []

    while row is not None:
        print(row)
        result_hosps.append({'id': row[0], 'name': row[1], 'addr': row[2], 'geoX': row[3], 'geoY': row[4]})
        row = cursor.fetchone()

    # cursor.close()

    conn.close()

    return result_hosps


def add_hospital_to_db(values):
    conn = mysql.connector.connect(user='UserName1', password='135792468', host='127.0.0.1', database='db1')

    if conn.is_connected():
        print('Connected to MySQL database')

    cursor = conn.cursor()

    insert_query = f"INSERT INTO `db1`.`hospitals`(`name`, `addr`) VALUES('{values['name']}', '{values['addr']}');"

    cursor.execute(insert_query)

    conn.commit()

    # cursor.close()

    conn.close()


def add_service_to_db(values):
    conn = mysql.connector.connect(user='UserName1', password='135792468', host='127.0.0.1', database='db1')

    if conn.is_connected():
        print('Connected to MySQL database')

    cursor = conn.cursor()

    insert_query = f"INSERT INTO `db1`.`services`(`name`) VALUES('{values['name']}');"

    cursor.execute(insert_query)

    conn.commit()

    # cursor.close()

    conn.close()
