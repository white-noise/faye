from django.shortcuts import render
from django.http import FileResponse, Http404

def index(request):
	return render(request, 'base/index.html')

def about(request):
	return render(request, 'base/about.html')

def contact(request):
	return render(request, 'base/contact_list.html')

def cv(request):
	try:
		return FileResponse(open('static/base/img/zane_rossi_cv.pdf', 'rb'), content_type='application/pdf')
	except FileNotFoundError:
		raise Http404()