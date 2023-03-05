# ====== 1 task =======
# Write a Python program to subtract five days from the current date.
from datetime import date, timedelta
today = date.today()
date_before_5days = today -\
                         timedelta(days = 5)
print('date_before_5days:', str(date_before_5days))