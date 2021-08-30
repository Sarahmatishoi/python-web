from django.conf.urls import url
from django.urls import path
from . import views 
from.views import Calendar,CalendarView, register_calender


app_name='calender'
urlpattens=[
    path("register/",views.CalendarView.as_view(),name="calender_register"),
    path("calender/",views.register_calender,name='register_calender'),
]