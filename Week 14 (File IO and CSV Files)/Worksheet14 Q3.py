import csv

def sort_records(csv_filename, new_filename):
    oldfile = open(csv_filename, 'r')
    data = csv.reader(oldfile)
    header = next(data)
    data = sorted(data, key=lambda item: item[0])

    newfile = open(new_filename, 'w')
    writer = csv.writer(newfile)
    writer.writerow(header)

    for row in data:
        writer.writerow(row)
