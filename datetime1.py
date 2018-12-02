from datetime import datetime, timedelta
import calendar
from dateutil.relativedelta import relativedelta

#
date_now = datetime.now()

#
date_yesterday = date_now - timedelta(days=1)

#
if date_now.month > 1:
    days_in_month = calendar.monthrange(date_now.year, date_now.month-1)[1]
else:
    days_in_month = calendar.monthrange(date_now.year-1, date_now.month)[1]
date_month_ago = date_now - timedelta(days=days_in_month)

#
date_month_ago2 = date_now - relativedelta(months=1)

#
date_str = "01/01/17 12:10:03.234567"
format_date_str = datetime.strptime(date_str, "%d/%m/%y %H:%M:%S.%f")

print("Вчера:", date_yesterday.strftime('%d.%m.%Y %H:%M'))
print("Сегодня:", date_now.strftime('%d.%m.%Y %H:%M'))
print("Месяц назад:", date_month_ago.strftime('%d.%m.%Y %H:%M'))
print("Месяц назад dateutil:", date_month_ago2.strftime('%d.%m.%Y %H:%M'))
print('Формат строки:', format_date_str.strftime('%d.%m.%Y %H:%M'))
