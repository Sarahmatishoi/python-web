from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet, TrainerViewSet, CourseViewSet,EventViewSet

router=routers.DefaultRouter()
router.register("students/",StudentViewSet)
router.register("trainer/",TrainerViewSet)
router.register("courses/",CourseViewSet)
router.register("calender/",EventViewSet)


urlpatterns=[
    path("",include(router.urls)),
]