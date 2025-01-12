import csv

def max_city_temp(csv_filename, city):
    fp = open(csv_filename, 'r')
    data = csv.reader(fp)
    header = next(data)

    for row in data:
        highestnum = 0
        if row[0] == city:
            for entry in row[1:]:
                entry = float(entry)
                if entry > highestnum:
                    highestnum = entry
            return highestnum