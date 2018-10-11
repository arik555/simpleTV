from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from livetv.views import starjalshatv_view, detail_starj, home, starj_add, starj_simple_view, starj_edit, starj_delete
from seriestv.views import episode_add, episode_edit, episode_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('starjalsha/', starjalshatv_view, name='starjalsha_home'),
    path('starjalsha/add/', starj_add, name='starjtv_add'),
    path('starjalshatv/listing', starj_simple_view, name='starj_simple_view'),
    path('starjalshatv/edit/<int:pk>', starj_edit, name='starj_edit'),
    path('starjalshatv/delete/<int:pk>', starj_delete, name='starj_delete'),
    path('episode/add/', episode_add, name='episodetv_add'),
    path('episode/edit/<int:epsd_id>', episode_edit, name='episode_edit'),
    path('episode/delelte/<int:epsd_id>', episode_delete, name='episode_delete'),
    path('starjalsha/special/<int:id>', detail_starj, name='detail_starj'),
    path('live/', include('livetv.urls')),
    path('movies/', include('movietv.urls')),
    path('series/', include('seriestv.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
