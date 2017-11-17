# from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^picture/', include('picture.urls'))
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)', views.post, name='post'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
