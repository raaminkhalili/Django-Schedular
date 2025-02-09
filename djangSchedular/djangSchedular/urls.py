
from django.contrib import admin
from django.urls import path ,include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',include('tasks.urls')),
    path('users/',include('users.urls')),
    path('', views.tasks, name="tasks"),


]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)