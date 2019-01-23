import pyexcel as p
if __name__ == '__main__':
    records = p.iget_records(file_name="plane.csv")
    for record in records:
    	print(record)