import csv
import datetime

crime_dict = {}

with open('Crimes.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        date = datetime.datetime.strptime(row[2], "%m/%d/%Y %H:%M:%S %p")
        if date > datetime.datetime.strptime("01/01/2015 00:00:00 AM", "%m/%d/%Y %H:%M:%S %p") and date < datetime.datetime.strptime("01/01/2016 00:00:00 AM", "%m/%d/%Y %H:%M:%S %p"):
            if row[5] not in crime_dict:
                crime_dict[row[5]] = 1
            else:
                crime_dict[row[5]] += 1

print(max(crime_dict, key=(lambda k: crime_dict[k])))