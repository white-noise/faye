from django.shortcuts import render

def index(request):
	return render(request, 'base/index.html')

def about(request):
	return render(request, 'base/about.html')

def contact(request):
	return render(request, 'base/contact_list.html')