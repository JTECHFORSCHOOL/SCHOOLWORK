from datetime import datetime
file = open("today.txt", "r")
today_string = file.read()
file.close()
formatString = "%d %B %Y"
dateTimeOb = datetime.strptime(today_string, formatString)
dateObject = dateTimeOb.date()
print(today_string)
print(dateTimeOb)
print(dateObject)
