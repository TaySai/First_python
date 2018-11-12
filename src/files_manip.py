import csv
with open('int.csv') as my_file:
    read = csv.reader(my_file)
    for row in read:
        print(row)
