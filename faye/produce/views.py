from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import WrittenObject, VisualObject
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):

	# take most recent of both objects
	recent_written = WrittenObject.objects.order_by('-pub_date')
	recent_visual  = VisualObject.objects.order_by('-pub_date')

	# leads to page allowing choice between media types
	context = {'recent_written' : recent_written, 'recent_visual': recent_visual}
	return render(request, 'produce/index.html', context)

def written(request):
	# leads to page of just written objects in a list
	menu_objects = WrittenObject.objects.all()
	heading      = 'written'
	return render(request, 'produce/menu_written.html', {'menu_objects' : menu_objects, 'heading': heading})

def visual(request):
	# leads to page of just visual objects in a list
	menu_objects = VisualObject.objects.all()
	heading      = 'visual'
	return render(request, 'produce/menu_visual.html', {'menu_objects' : menu_objects, 'heading': heading})

def written_individual(request, produce_id):
	# leads to page of individula written object
	written_object = get_object_or_404(WrittenObject, pk=produce_id)
	return render(request, 'produce/individual_written.html', {'written_object': written_object})

def visual_individual(request, produce_id):
	# leads to page of individula visual object
	visual_object = get_object_or_404(VisualObject, pk=produce_id)
	return render(request, 'produce/individual_visual.html', {'visual_object': visual_object})
