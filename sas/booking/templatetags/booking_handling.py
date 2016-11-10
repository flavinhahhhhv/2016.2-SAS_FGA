from django import template
from django.utils.translation import ugettext_lazy as _
import datetime

register = template.Library()


@register.filter(name='get_timetable')
def get_timetable(booking):
    weekdays = [0, 1, 2, 3, 4, 5, 6]
    timetable = []
    # ASSUMED FIRST 7 SEVEN ITEMS CAN IDENTIFY TIMETABLE
    book_times = booking.time.all().order_by('date_booking')[:7]
    for book_time in book_times:
        try:
            weekdays.remove(book_time.date_booking.weekday())
            weekday = _(book_time.date_booking.strftime("%A"))
            weekday_time = (book_time.start_hour, book_time.end_hour)
            timetable.append((weekday, weekday_time))
        except ValueError:
            break
    return timetable
