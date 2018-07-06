import json

from django.shortcuts import render
from .models import LibraryObject

def index(request):
	return render(request, 'library/index.html')

def individual(request):
	return render(request, 'library/index.html')