from calender.forms import CalenderRegistrationForm
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar
from.models import Event
from datetime import date

class CalendarView(generic.ListView):
    model = Event
    template_name = 'register_calender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def register_calender(request):
    if request.method == "POST":
        form=CalenderRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CalenderRegistrationForm()
    return render(request,"calender.html",{"form":form})

# Create your views here.
