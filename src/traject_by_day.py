from datetime import date
import calendar

def trajectByDay(my_date) :
    return calendar.day_name[date.fromisoformat(str(my_date)[:10]).weekday()]