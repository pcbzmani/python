import datetime

date = datetime.date(2018,5,5)

input_date1= datetime.datetime(2018,5,6,1,1,1,1)
dt = datetime.timedelta(days = 3, seconds =2, microseconds = 1, minutes = 2)
t = input_date1 - dt
dt = datetime.timedelta(days = 3, seconds =2, microseconds = 1, minutes = 2)
t= input_date1 - dt
day = t.day
year= t.year
month = t.month
minute= t.minute
Second= t.second
print(input_date)
print(input_date1)
print(t)
print(day)
print(year)
print(month)    
print(minute)
print(second)

s= "%a %b %d %H:%M:%S %Y"
x= datetime.datetime(y,m,d,ms,se,da,mi)
q= x.strftime(s)
z= datetime.datetime.strptime(q,s)
