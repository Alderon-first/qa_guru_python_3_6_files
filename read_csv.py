import csv
with open('resources/username.csv') as csvfile:
    reader = csv.reader(csvfile)
    print(reader)
    headers = next(reader)
    print(headers)
    csvfile = csv.reader(csvfile)
    for r in csvfile:
        print(r)
