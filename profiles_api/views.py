from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import status, viewsets


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
	"Handle creating & updating profiles"
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
