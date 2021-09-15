from django.urls import path
from . import views


app_name='calender'
urlpatterns=[
    path("register/",views.CalendarView.as_view(),name="calender_register"),
    path("calender/",views.register_calender,name='register_calender'),
]