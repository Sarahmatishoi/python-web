from django.urls import path
from django.conf import urls
from django.conf import settings
from django.conf.urls import url
from .views import register_trainers, trainer_list
from django.conf.urls.static import static
urlpatterns=[
    path("register/",register_trainers,name="register_trainers"), 
    path("register_list/",trainer_list,name="trainer_list"),

]