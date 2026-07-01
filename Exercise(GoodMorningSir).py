from datetime import date#inbuilt module to get the date and time
import time #inbuilt module to get the time

timestamp=time.strftime("%H:%M:%S") #strftime is used to format the time in hours, minutes and seconds
currentDate= date.today()
a=currentDate.strftime("%d/%m/%Y") #strftime is used to format the date in day, month and year
print("Today's Date is: " + str(a))
print("The Current Time is: " + timestamp)

a=time.strftime("%H")
print("The Time in Hours is: " + a)

b=time.strftime("%M")
print("The Time in Minutes is: " + b)

c=time.strftime("%S")
print("The Time in Seconds is: " + c)

if timestamp>="00:00:00" and timestamp<="12:00:00":
    print("Good Morning Sir!")

elif timestamp>="12:00:01" and timestamp<="15:00:00":
    print("Good Afternoon Sir!")

elif timestamp>= "15:00:01" and  timestamp<="19:00:00":
    print("Good Evening Sir!")

else:
    print("Good Night Sir!")
