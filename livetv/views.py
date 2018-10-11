from django.shortcuts import render, get_object_or_404, redirect
from .models import Live, StarJalsha
from .forms import LiveForm, StarJalshaForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from seriestv.models import Episode
from movietv.models import Movie
from livetv.models import Live

def home(request):
	episodes = Episode.objects.order_by('-id')[:10]
	movies = Movie.objects.order_by('-id')[:10]
	lives = Live.objects.order_by('-id')[:10]
	context = { 'latest_episodes': episodes, 'latest_movies': movies, 'latest_livetv': lives}
	return render(request, 'index.html', context)


def livetv_view(request):
	x = 9
	if request.method == 'POST':
		qset = request.POST.get('qs')
		if qset == '':
			queryset_live = Live.objects.all()
		else:
			queryset_live = Live.objects.filter(channel_title__icontains=qset)
			x = 999999
	else:
		queryset_live = Live.objects.all()
	paginator = Paginator(queryset_live, x) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_live = paginator.get_page(page)
	context = { 'live_objects': queryset_live, 'title': 'SimpleTV | Live', }
	return render(request, 'livetvtemplate/mainindex.html', context)


def detail_live(request, slug=None, id=None):
	channel_obj = Live.objects.get(id=id)
	context = {'title': 'Simple TV | Live | '+channel_obj.channel_title, 'instance': channel_obj, 'channel': '1',}
	return render(request, 'livetvtemplate/livechanneldetailsindex.html', context)

# THIRD PARTY 

def starjalshatv_view(request):
	queryset_starjalsha = StarJalsha.objects.filter(activate=True)
	context = { 'starjalsha_objects': queryset_starjalsha, 'title': 'SimpleTV | Star Jalsha', }
	return render(request, 'livetvtemplate/star_mainindex.html', context)


def detail_starj(request, id=None):
	serial_obj = StarJalsha.objects.get(id=id)
	context = {'title': 'SimpleTV | StarJalsha | '+serial_obj.serial_name, 'instance': serial_obj, 'star': '1',}
	return render(request, 'livetvtemplate/starjalshadetailindex.html', context)


def livetv_add(request):
	if request.method == 'POST':
		form = LiveForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = LiveForm()
	context = {'form': form, 'header': 'Add Live Channel', 'title': 'SimpleTV | LiveTV | Add',}
	return render(request, 'commonformindex.html', context)


def starj_add(request):
	if request.method == 'POST':
		form = StarJalshaForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
	else:
		form = StarJalshaForm()
	context = {'form': form, 'header': 'Add StarJalsha Serial', 'title': 'SimpleTV | StarJalsha | Add',}
	return render(request, 'commonformindex.html', context)


def livetv_simple_view(request):
	paginator = Paginator(Live.objects.all(), 9) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_live = paginator.get_page(page)
	return render(request, 'livetvtemplate\livechannellisting.html', {'live_objects': queryset_live})

def livetv_edit(request, pk=None):
	instance = Live.objects.get(pk=pk)
	if request.method == 'POST':
		form = LiveForm(request.POST, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
	else:
		form = LiveForm(instance=instance)
	context = {'form': form, 'title': 'SimpleTV | LiveTV | Edit', 'header': 'Edit Live Channel'}
	return render(request, 'commonformindex.html', context)


def livetv_delete(request, pk=None):
	print('delete func')
	instance = Live.objects.get(pk=pk)
	instance.delete()
	return redirect('livetv_simple_view')


def starj_simple_view(request):
	paginator = Paginator(StarJalsha.objects.all(), 9) # Show 25 contacts per page
	page = request.GET.get('page')
	queryset_starjalsha = paginator.get_page(page)
	return render(request, 'livetvtemplate\starjalshalisting.html', {'starjalsha_objects': queryset_starjalsha})


def starj_edit(request, pk=None):
	instance = StarJalsha.objects.get(pk=pk)
	if request.method == 'POST':
		form = StarJalshaForm(request.POST, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
	else:
		form = StarJalshaForm(instance=instance)
	context = {'form': form, 'title': 'SimpleTV | StarJalsha | Edit', 'header': 'Edit Live Channel'}
	return render(request, 'commonformindex.html', context)


def starj_delete(request, pk=None):
	instance = StarJalsha.objects.get(pk=pk)
	instance.delete()
	return redirect('livetv_simple_view')

