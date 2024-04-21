from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')

urlpatterns = [
    path('',views.mainpage, name='mainpage'),
    path('catalog/',views.catalog,name='catalog'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)