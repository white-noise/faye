from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import WrittenObject, VisualObject
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):

	# take most recent of both objects (can also specify meta class for 'latest')
	recent_written = WrittenObject.objects.order_by('-pub_date')
	recent_visual  = VisualObject.objects.order_by('-pub_date')

	# leads to page allowing choice between media types
	context = {'recent_written' : recent_written, 'recent_visual': recent_visual}
	return render(request, 'produce/index.html', context)

def written(request):
	# leads to page of just written objects in a list
	menu_objects = WrittenObject.objects.order_by('-pub_date')
	heading      = 'written'
	return render(request, 'produce/menu_written.html', {'menu_objects' : menu_objects, 'heading': heading})

def visual(request):
	# leads to page of just visual objects in a list
	menu_objects = VisualObject.objects.order_by('-pub_date')
	heading      = 'visual'
	return render(request, 'produce/menu_visual.html', {'menu_objects' : menu_objects, 'heading': heading})

def written_individual(request, produce_id):
	# leads to page of individula written object
	written_object = get_object_or_404(WrittenObject, pk=produce_id)
	cited_works    = written_object.cited_works.all()

	return render(request, 'produce/individual_written.html', {'written_object': written_object, 'cited_works' : cited_works})

def visual_individual(request, produce_id):
	# leads to page of individula visual object
	visual_object = get_object_or_404(VisualObject, pk=produce_id)
	cited_works   = visual_object.cited_works.all()

	return render(request, 'produce/individual_visual.html', {'visual_object': visual_object, 'cited_works' : cited_works})

def hypertext_individual(request, hypertext_id):

	def_str = 'produce/hypertext_files/ht_%s.html'%(hypertext_id)

	return render(request, def_str, {})
