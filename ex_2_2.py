from datetime import date, datetime, timedelta

# date -- год, месяц и день
s_date = input()
days = input()

f_date = datetime.strptime(s_date, "%Y %m %d")
f_date = f_date + timedelta(days=+int(days))

print(f_date.strftime("%Y %-m %-d"))
