from django.contrib import admin
from django.urls import path, re_path
from quest import views as quesr_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', quesr_views.index)
]
