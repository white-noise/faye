# necessary imports
from django.http import HttpResponse, Http404
from django.template import loader

from django.shortcuts import render, get_object_or_404
from .models import LibraryObject

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):

	author_library = LibraryObject.objects.order_by('title')

	paginator     = Paginator(author_library, 8)
	page          = request.GET.get('page')
	page_library  = paginator.get_page(page)

	return render(request, 'library/index.html', {'page_library' : page_library})

def individual(request, library_id):

	# quick method to get book object if desired
	book = get_object_or_404(LibraryObject, pk=library_id)

	# debugging minimal HttpResponse
	response = "This is book number %s."
	return HttpResponse(response % library_id)