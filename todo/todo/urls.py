
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import *
router=DefaultRouter()
router.register("", TodoVS)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]