# necessary imports
from django.http import HttpResponse, Http404
from django.template import loader

# cosmetic imports
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

# if you use the shortcut specified, remove above and
# from django.shortcuts import render, get_object_or_404

# eventually one can even abstract this in order to 
# see generic IndexView, and generic DetailView
# for displaying list of objects versus particular objects

# load relevant models from the in-directory models file
from .models import StatusObject

def index(request):

	# do all processing in script first, then pass as context to template
	recent_status = StatusObject.objects.order_by('-pub_date')

	# handle pagination (2 per page)
	paginator     = Paginator(recent_status, 2)
	page          = request.GET.get('page')
	recent_status = paginator.get_page(page)

	return render(request, 'status/index.html', {'recent_status' : recent_status})
	# # template = loader.get_template('status/index.html')
	# # for use of non-shortcut methods (better control)
	# # maps template variable names to python objects
	# context = {
	# 	'recent_status' : recent_status,
	# }
	# # then the template object takes context and request to render
	# return HttpResponse(template.render(context, request))
	# # because this is so idiomatic, can also just run
	# # where we have removed explicit template call: only call context
	# # return render(request, 'status/index.html', context)

# auxilliary views for a status's own page
def individual(request, status_id):
	# try and catch exception for view
	# right now the django 404 page pops up
	try:
		status = StatusObject.objects.get(pk=status_id)
	except StatusObject.DoesNotExist:
		raise Http404("Status does not exist.")

	# replace this with reasonable render
	response = "This is status number %s."
	return HttpResponse(response % status_id)

	# or, for the purpose of expediency
	# status = get_object_or_404(StatusObject, pk=status_id)