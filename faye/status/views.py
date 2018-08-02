from django.http import HttpResponse, Http404
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404

from .models import StatusObject

def index(request):

	recent_status = StatusObject.objects.order_by('-pub_date')

	# pagination
	paginator     = Paginator(recent_status, 12)
	page          = request.GET.get('page')
	recent_status = paginator.get_page(page)

	return render(request, 'status/index.html', {'recent_status' : recent_status})
	
	# # deconstructed use of render
	# template = loader.get_template('status/index.html')
	# # for use of non-shortcut methods (better control)
	# context = {
	#   'recent_status' : recent_status,
	# }
	# return HttpResponse(template.render(context, request))

def individual(request, status_id):

	status = get_object_or_404(StatusObject, pk=status_id)

	# cited works
	cited_works = status.cited_works.all()

	return render(request, 'status/individual_status.html', {'status' : status, 'cited_works' : cited_works})