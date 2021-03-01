from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *

# 
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication


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