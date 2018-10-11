from django.urls import path
from .views import ( 
	livetv_view, detail_live, livetv_add, 
	livetv_simple_view, livetv_edit, livetv_delete
	)

urlpatterns = [
	path('', livetv_view, name="livetv_home"),
	path('add/', livetv_add, name="livetv_add"),
	path('listing/', livetv_simple_view, name='livetv_simple_view'),
	path('edit/<int:pk>', livetv_edit, name='livetv_edit'),
	path('delete/<int:pk>', livetv_delete, name='livetv_delete'),
	path('<slug:slug>/<int:id>', detail_live, name='detail_live'),
 #    path('zeecinema/live', zeecinema),
 #    path('zeebangla/live', zeebangla),
	# path('timesnow/live', timesnow),
	# path(),

]