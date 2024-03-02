from datetime import datetime

currentDate = datetime.now()

strDate = currentDate.strftime("%d %B %Y")

file = open("today.txt", "w")

file.write(strDate)

file.close()
