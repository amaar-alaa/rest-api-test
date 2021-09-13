from django.urls import path
from django.urls.conf import include
from .views import *
from rest_framework.routers import DefaultRouter
 
router=DefaultRouter()
router.register('hello-viewSet',HelloViewSet,basename='hello-viewset') 


urlpatterns = [
    path('hello-view/',HelloApiView.as_view()),
    path('',include(router.urls))
]
