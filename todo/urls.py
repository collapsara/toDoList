from django.contrib import admin
from django.urls import path, include
from .views import TaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

