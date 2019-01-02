from django.urls import path
# from django.urls import re_path
from firstDjangoApp import views


urlpatterns = [
    path('',views.initialize),
]
