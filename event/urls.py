from trainer.views import register_trainers
from django.urls import path
from django.conf import urls 
from django.conf import settings
from django.conf.urls import url
from .views import event_list, register_event
from django.conf.urls.static import static
urlpatterns=[
    path("register/",register_event,name="register_event"),
    path("register_list/",event_list,name="event_list"),

]