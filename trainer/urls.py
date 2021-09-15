from django.urls import path
from django.conf import urls
from django.conf import settings
from django.conf.urls import url
from .views import delete_trainer, edit_trainer, register_trainers, trainer_list, trainer_profile
from django.conf.urls.static import static
urlpatterns=[
    path("register/",register_trainers,name="register_trainers"), 
    path("register_list/",trainer_list,name="trainer_list"),
    path("edit/<int:id>",edit_trainer, name="edit_trainer"),
    path("profile/<int:id>",trainer_profile, name="trainer_profile"),
    path("delete/<int:id>/",delete_trainer,name="delete_trainer",)
]
