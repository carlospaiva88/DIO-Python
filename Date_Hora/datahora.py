from datetime import date, datetime, timedelta

data = date(2023, 1, 30)
print(data)
print(data.today())

print('=' * 50)
d = datetime(2023, 1, 1) 
new_date = d + timedelta(days=10)
#print(new_date)


d = datetime(2023, 1, 1)
new_date = d + timedelta(days=10)
print(new_date)