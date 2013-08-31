from django.conf.urls import patterns, url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
