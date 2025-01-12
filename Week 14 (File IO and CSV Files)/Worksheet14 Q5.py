import csv

def hottest_city(csv_filename):
    fp = open(csv_filename, 'r')
    data = csv.reader(fp)
    header = next(data)
    hotlist = []
    hottest_city = ""
    highest_temp = 0
    for row in data:
        total = 0
        cols = 0
        for entry in row[1:]:
            if float(entry) > highest_temp:
                highest_temp = float(entry)
                hottest_city = row[0]
            elif float(entry) == highest_temp:
                hotlist.append(row[0])
    hotlist.append(hottest_city)
    return (highest_temp, hotlist)



