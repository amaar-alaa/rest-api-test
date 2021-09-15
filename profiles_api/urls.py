from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter
 
router=DefaultRouter()
router.register('hello-viewSet',views.HelloViewSet,basename='hello-viewset') 
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeddItemViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
