from django.shortcuts import render, redirect
from .models import Series, Episode
from .forms import SeriesForm, EpisodeForm
from .utils import get_proper_series_data
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.

def detail_series(request, season=None, episode=None, id=None):
	episode_obj = Episode.objects.get(id=id)
	com_type = episode_obj.compatible
	stype = ''
	if com_type=='1':
		stype='Clappr'
	elif com_type=='2':
		stype=='YouTube'
	elif com_type=='3':
		stype='OpenLoad'
	elif com_type=='4':
		stype='RapidVideo'
	else:
		stype='NoFlag'
	context = {'title': 'Simple TV | Series | '+episode_obj.series.series_title+' | S'+episode_obj.series.series_season+'E'+episode_obj.episode_no+' | '+episode_obj.episode_title, 'instance': episode_obj, 'episode': '1', str(stype): '1'}
	return render(request, 'seriestvtemplate/seriestvdetailindex.html', context)


# def seriestv_view(request):
# 	series_set, total_items_count = get_proper_series_data(Series.objects.all(), Episode.objects.all())
# 	context = { 'series_objects': series_set, 'title': 'SimpleTV | Series', 'counter': total_items_count}
# 	return render(request, 'seriestvtemplate/mainindex.html', context)

def seriestv_view(request):
	x = 2
	if request.method == 'POST':
		qset = request.POST.get('qs')
		if qset == '':
			series_set = Series.objects.all()
		else:
			series_set = Series.objects.filter(series_title__icontains=qset)
			x = 999999
	else:
		series_set = Series.objects.all()
	paginator = Paginator(series_set, x) # Show 25 contacts per page
	page = request.GET.get('page')
	series_set = paginator.get_page(page)
	#series_set, total_items_count = get_proper_series_data(Series.objects.all(), Episode.objects.all())
	context = { 'series_objects': series_set, 'title': 'SimpleTV | Series',}
	return render(request, 'seriestvtemplate/mainindex.html', context)


def seriestv_view_tweak(request, lang_id=None):
	series_set = Series.objects.filter(series_language__iexact=lang_id)
	paginator = Paginator(series_set, 2) # Show 25 contacts per page
	page = request.GET.get('page')
	series_set = paginator.get_page(page)
	#series_set, total_items_count = get_proper_series_data(Series.objects.all(), Episode.objects.all())
	context = { 'series_objects': series_set, 'title': 'SimpleTV | Series',}
	return render(request, 'seriestvtemplate/mainindex.html', context)

def series_add(request):
	if request.method == 'POST':
		form = SeriesForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = SeriesForm()
	context = {'form': form, 'header': 'Add Series'}
	return render(request, 'commonformindex.html', context)


def episode_add(request):
	if request.method == 'POST':
		form = EpisodeForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = EpisodeForm()
	context = {'form': form, 'header': 'Add Episode','title': 'SimpleTV | Series | Add'}
	return render(request, 'commonformindex.html', context)

def series_simple_view(request):
	paginator = Paginator(Series.objects.all(), 2) # Show 25 contacts per page
	page = request.GET.get('page')
	series_set = paginator.get_page(page)
	return render(request, 'seriestvtemplate\serieslisting.html', {'series_objects' : series_set})

def series_edit(request, series_id=None):
	instance = Series.objects.get(id=series_id)
	if request.method == 'POST':
		form = SeriesForm(request.POST, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
	else:
		form = SeriesForm(instance=instance)
	context = {'form': form, 'title': 'SimpleTV | Series | Edit', 'header': 'Edit Series'}
	return render(request, 'commonformindex.html', context)

def episode_edit(request, epsd_id=None):
	instance = Episode.objects.get(id=epsd_id)
	if request.method == 'POST':
		form = EpisodeForm(request.POST, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
	else:
		form = EpisodeForm(instance=instance)
	context = {'form': form, 'title': 'SimpleTV | Episode | Edit', 'header': 'Edit Episode'}
	return render(request, 'commonformindex.html', context)

def episode_delete(request, epsd_id=None):
	instance = Episode.objects.get(id=epsd_id)
	instance.delete()
	return redirect('series_simple_view')


def series_delete(request, series_id=None):
	instance = Series.objects.get(id=series_id)
	instance.delete()
	return redirect('series_simple_view')
