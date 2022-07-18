from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

#from .models import
#from .serializers import

# Create your views here.

def front(request):
    context = {}
    return render(request, 'index.html', context)