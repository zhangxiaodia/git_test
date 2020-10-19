import csv
file = "/Users/admin/git_test/test_data/test.csv"
row = ["8", "8", "8"]
with open(file, 'a', newline="") as f:
     csv_writer = csv.writer(f, dialect="excel")
     csv_writer.writerow(row)

     csv_f = csv.reader(f)
     for i in csv_f:
         print(i)
     print(csv_f)
