from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
#from django.contrib.admin import admin

from todo import views

app_name = 'todo'
urlpatterns = [
    #url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^detail/([a-zA-Z0-9_.-]*)/$', views.detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
