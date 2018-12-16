import datetime
import time
import math
dob = datetime.datetime(2009, 2, 15)
today = datetime.datetime.today()
age = today - dob
print (age)
a =  datetime.timedelta(days = 365)
print (a)
b = age/a
print (b)

years = math.floor(b)
months = (b - years)*12

print ("I am %d years and %d months old" %(years, months))

