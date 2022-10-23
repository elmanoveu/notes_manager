from django.contrib import admin
from django.urls import path, include
from tags.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tags.urls'))
]
