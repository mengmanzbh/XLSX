import pyexcel as p
if __name__ == '__main__':
    records = p.iget_records(file_name="plane.xls")
    for record in records:
    	print(record['1'],record['2'],record['3'],record['4'],record['5'])