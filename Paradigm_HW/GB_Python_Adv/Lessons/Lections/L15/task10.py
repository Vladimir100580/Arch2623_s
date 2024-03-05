from datetime import datetime

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)

print(dt)
# 2007-06-15 02:14:00.000024
print(dt.timestamp())
# 1181862840.000024
print(dt.isoformat())
# 2007-06-15T02:14:00.000024
print(dt.weekday())
# 4  # <- пятница (дни недели от 0 (пон) до 6 (вос))
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))
# Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.

t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)

print(f'{new_dt}\n{one_more_hour}')
