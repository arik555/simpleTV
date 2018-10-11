from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.core.paginator import Paginator
# Create your views here.

def detail_movie(request, id=None):
	movie_obj = Movie.objects.get(id=id)
	com_type = movie_obj.compatible
	stype = ''
	if com_type=='1':
		stype='Clappr'
	elif com_type=='2':
		stype=='YouTube'
	elif com_type=='3':
		stype='OpenLoad'
	else:
		stype='NoFlag'
	# print(stype, com_type)
	context = {'title': 'Simple TV | Movie | '+movie_obj.movie_title, 'instance': movie_obj, 'movie': '1', str(stype): '1'}
	return render(request, 'movietvtemplate/moviedetailindex.html', context)

def movietv_view(request):
	x = 9
	if request.method == 'POST':
		qset = request.POST.get('qs')
		if qset == '':
			queryset_movie = Movie.objects.all().order_by('-movie_year')
		else:			
			queryset_movie = Movie.objects.filter(movie_title__icontains=qset)
			x = 999999
	else:
		queryset_movie = Movie.objects.all().order_by('-movie_year')
	paginator = Paginator(queryset_movie, x) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_movie = paginator.get_page(page)
	context = { 'movie_objects': queryset_movie, 'title': 'SimpleTV | Movies', }
	return render(request, 'movietvtemplate/mainindex.html', context)

def movietv_view_tweak(request, lang_id=None):
	queryset_movie = Movie.objects.filter(movie_language__iexact=lang_id).order_by('-movie_year')
	paginator = Paginator(queryset_movie, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_movie = paginator.get_page(page)
	context = { 'movie_objects': queryset_movie, 'title': 'SimpleTV | Movies', }
	return render(request, 'movietvtemplate/mainindex.html', context)

def movietv_view_date_tweak(request, dated=None):
	queryset_movie = Movie.objects.all().order_by('movie_year')
	paginator = Paginator(queryset_movie, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_movie = paginator.get_page(page)
	context = { 'movie_objects': queryset_movie, 'title': 'SimpleTV | Movies', }
	return render(request, 'movietvtemplate/mainindex.html', context)

def movietv_add(request):
	if request.method == 'POST':
		form = MovieForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = MovieForm()
	context = {'form': form, 'header': 'Add Movie', 'title': 'SimpleTV | ADD CONTENT'}
	return render(request, 'commonformindex.html', context)


def movie_simple_view(request):
	paginator = Paginator(Movie.objects.all(), 25) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_movie = paginator.get_page(page)
	return render(request, 'movietvtemplate\movielisting.html', {'movie_objects': queryset_movie})

def movie_edit(request, pk=None):
	instance = Movie.objects.get(id=pk)
	if request.method == 'POST':
		form = MovieForm(request.POST, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
	else:
		form = MovieForm(instance=instance)
	context = {'form': form, 'title': 'SimpleTV | Movie | Edit', 'header': 'Edit Movie'}
	return render(request, 'commonformindex.html', context)

def movie_delete(request, pk=None):
	instance = Movie.objects.get(id=pk)
	instance.delete()
	return redirect('movie_simple_view')
