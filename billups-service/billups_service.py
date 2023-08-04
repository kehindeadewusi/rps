from datetime import datetime
from billups.numbers.magical.magic import secret_number_generator
from billups.numbers.stately.state import state_num
from billups.dates.dateutils import days_to_snake_day

print(days_to_snake_day(datetime.now()))
print(secret_number_generator())
print(state_num("akwa-ibom"))
