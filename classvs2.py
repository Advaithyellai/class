import time
# {time.time()} prints [ unix time stamp ].  It presents seconds  between now and 1970
# now = time.time()
# print(now)
# begin = time.time()
# time.sleep(10)
# end = time.time()
# dif = end - begin
# print(dif)
import datetime
import math
st = time.time()
dob = datetime.datetime(2009, 2, 15)
today = datetime.datetime.now()
age = today - dob
a = datetime.timedelta(days = 365)
b = age/a
e = math.floor(b)
d = (b - e)*12
f = 18 - e
print("My age is %d[years] %d[months]." %(b, d))
print("The no. of years left to get my license is :", f)
et = time.time()
i = et - st
print("The time taken for this program to run = %s[seconds]. " %(i))
# # st = time.time() 
# # a = 0
# # for i in range (0, 100):
# #     a = a+1
# #     print(a)
# # et = time.time()
# # v = et - st
# # print("Duration: %s is the total time" %(v))
# # day = datetime.datetime.now()
# # days = datetime.timedelta(days = 1)
# # a = day -  days
# # print(a)
# # a = datetime.datetime(2018, 12, 8, 1, 4, 35, 555)
# # print(a)