# Каждый из объектов позволяет прочитать хранимые свойства
# обратившись к ним по имени через точечную нотацию.

from datetime import time, date, datetime, timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)

delta = timedelta(weeks=53, hours=73, minutes=101, seconds=303, milliseconds=60)

print(f'{d.month}')  # 6
print(f'{t.second}')  # 0
print(f'{dt.hour}')  # 2
print(f'{delta.days}')  # 374
