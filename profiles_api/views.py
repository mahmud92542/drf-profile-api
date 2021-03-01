from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *

#import
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
#user auth
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
	"Handle creating & updating profiles"
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	"authentication"
	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
	"handle creating user authentication tokens"
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
