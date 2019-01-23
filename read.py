import pyexcel as p
if __name__ == '__main__':
    records = p.iget_records(file_name="plane.xlsx")
    for record in records:
        print(record['airplane'], record['airname'], record['citycode'], record['cityname'])