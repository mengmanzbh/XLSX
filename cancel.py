import pyexcel as p
import pymysql.cursors

if __name__ == '__main__':

    records = p.iget_records(file_name="cancel.xlsx")
    for record in records:
        print(record['A'],record['B'],record['C'],record['D'],record['E'])
        try:


        finally:
            print("********************")
            # connection.close()