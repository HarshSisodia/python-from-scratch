from datetime import date#inbuilt module to get the date and time
import time #inbuilt module to get the time

timestamp=time.strftime("%H:%M:%S") #strftime is used to format the time in hours, minutes and seconds
currentDate= date.today()
D=currentDate.strftime("%d/%m/%Y") #strftime is used to format the date in day, month and year
print("Today's Date is: " + str(D))
print("The Current Time is: " + timestamp)

# a=int(time.strftime("%H"))
# print("The Time in Hours is: " + str(a))

# b=int(time.strftime("%M"))
# print("The Time in Minutes is: " + str(b))

# c=int(time.strftime("%S"))
# print("The Time in Seconds is: " + str(c))

if timestamp>="00:00:00" and timestamp<="12:00:00":
    print("Good Morning Sir. Today Date is " + str(D) + " and current time is: " + timestamp +" AM")

elif timestamp>="12:00:01" and timestamp<="15:00:00":
    print("Good Afternoon Sir. Today Date is " + str(D) + " and current time is: " + timestamp +" PM")

elif timestamp>= "15:00:01" and  timestamp<="19:00:00":
    print("Good Evening Sir. Today Date is " + str(D) + " and current time is: " + timestamp +" PM")

else:
    print("Good Night Sir. Today Date is " + str(D) + " and current time is: " + timestamp +" PM")
