from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('webusers', views.WebUserView)
router.register('tracks', views.TrackView)

urlpatterns = [
    path('', include(router.urls)),
]