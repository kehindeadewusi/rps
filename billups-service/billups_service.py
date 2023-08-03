# from billups import dateutils, magic

# print(magic.secret_number_generator())
# print(dateutils.days_to_snake_day())
from billups.numbers.magic import secret_number_generator
from datetime import datetime
from billups.dates.dateutils import days_to_snake_day

print(days_to_snake_day(datetime.now()))

print(secret_number_generator())
