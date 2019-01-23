import pyexcel as p
if __name__ == '__main__':
    records = p.iget_records(file_name="plane.xls")
    for record in records:
    	print(record['A'],record['B'],record['C'],record['D'],record['E'])