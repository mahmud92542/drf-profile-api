from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('profile',UserProfileViewSet)
router.register('feed',UserProfileFeedViewSet)

urlpatterns = [
	path('api/',include(router.urls)),
	path('login/',UserLoginApiView.as_view()) 
]