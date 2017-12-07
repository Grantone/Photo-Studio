from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from .views import tags

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^picture/', include('picture.urls'))
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)', views.post, name='post'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^tags/$', views.tag, name='tags'),
    url(r'^collections/(\d+)', views.collections, name='collections'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
