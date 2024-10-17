# com a biblioteca Pytz

from datetime import datetime

import pytz

data = datetime.now(pytz.timezone('Europe/Oslo'))

print(data)


# sem a biblioteca pytz

from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))
print(data_oslo)
print(data_sp)