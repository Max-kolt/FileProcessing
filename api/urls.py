from django.urls import path, re_path
from .views import *


urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', load_file),
    path('files/', get_files)
]
