from django.contrib import admin
from django.urls import path
from . import views as model_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', model_views.home, name = 'model-home'),
    path('home/', model_views.home, name = 'model-home'),
    path('results/', model_views.results, name = 'model-results')
]