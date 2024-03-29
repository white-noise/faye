from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import LibraryObject
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):

	# specify first and last name fields in library model for last name sorting
	author_library = LibraryObject.objects.order_by('lastname')

	# handling pagination
	paginator     = Paginator(author_library, 12)
	page          = request.GET.get('page')
	page_library  = paginator.get_page(page)

	return render(request, 'library/index.html', {'page_library' : page_library})

def individual(request, library_id):

	book = get_object_or_404(LibraryObject, pk=library_id)
	return render(request, 'library/individual_library.html', {'book': book})

def back(request):

	# return user to the page of reference (to keep pages returns neat)
	# try to capture the edge case for no access to referer

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))