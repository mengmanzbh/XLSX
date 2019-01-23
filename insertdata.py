import pyexcel as p
import pymysql.cursors
if __name__ == '__main__':
	connection = pymysql.connect(host='123.58.7.80',
                             port=3306,
                             user='sk_admin',
                             password='skmm94bgsn',
                             db='tgapp_excel',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    records = p.iget_records(file_name="plane.xlsx")
    for record in records:
    	print(record['A'],record['B'],record['C'],record['D'],record['E'])
    	try:
    		with connection.cursor() as cursor:
    		# Create a new record
    		sql = "INSERT INTO `airport_city_triple_code` (`airport_code`, `airport_name`, `city_code`, `city_name`, `country`) VALUES (%s, %s, %s, %s, %s)"
    		cursor.execute(sql, (record['A'], record['B'], record['C'], record['D'], record['E']))
    	connection.commit()
        finally:
        	connection.close()