from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from todo_list.views import todo_list


urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('admin/', admin.site.urls),
    path('todo/', include('todo_list.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
