import csv
BlackList = []
with open('list.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
                BlackList.append(', '.join(row))
