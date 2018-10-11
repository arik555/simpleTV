from django.urls import path
from .views import (detail_series, seriestv_view, 
	series_add, seriestv_view_tweak, series_simple_view, series_edit, series_delete)

urlpatterns = [
	path('', seriestv_view, name='seriestv_home'),
	path('language/type/<int:lang_id>/', seriestv_view_tweak, name='seriestv_view_tweak'),
	path('S<int:season>E<int:episode>/<int:id>/', detail_series, name='detail_series'),
	path('add/', series_add, name='seriestv_add'),
	path('listing/', series_simple_view, name='series_simple_view'),
	path('edit/<int:series_id>', series_edit, name='series_edit'),
	path('delete/<int:series_id>', series_delete, name='series_delete'),
	# path('', episode_add, name='episode_add'),

] 