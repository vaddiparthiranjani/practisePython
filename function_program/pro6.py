# to extract year, month, date and time using Lambda.
import datetime

now =datetime.datetime.now()
print(now)

year =lambda x:x.year
month =lambda x:x.month
day = lambda x:x.day

time1 = lambda x:x.time()

print("year : ", year(now))
print("month :", month(now))
print("day :", day(now))

print("time :",time1(now))

