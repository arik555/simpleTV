from django.urls import path
from .views import (
	detail_movie, movietv_view, movietv_add, movietv_view_tweak, 
	movietv_view_date_tweak, movie_simple_view, movie_edit, movie_delete
	)
urlpatterns = [
	path('', movietv_view, name='movietv_home'),
	path('language/type/<int:lang_id>', movietv_view_tweak, name='movietv_view_tweak'),
	path('orderby/old/<int:dated>', movietv_view_date_tweak, name='movietv_view_date_tweak'),
	path('<int:id>/', detail_movie, name='detail_mov'),
	path('add/', movietv_add, name="movietv_add"),
	path('listing/', movie_simple_view, name='movie_simple_view'),
	path('edit/<int:pk>', movie_edit, name='movie_edit'),
	path('delete/<int:pk>', movie_delete, name='movie_delete'),
]