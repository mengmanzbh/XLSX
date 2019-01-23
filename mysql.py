import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='123.58.7.80',
                             port=3306,
                             user='sk_admin',
                             password='skmm94bgsn',
                             db='tgapp_excel',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `airport_city_triple_code` (`airport_code`, `airport_name`, `city_code`, `city_name`, `country`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, ('1', '2', '3', '4', '5'))

    connection.commit()
finally:
    connection.close()