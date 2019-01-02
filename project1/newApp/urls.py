from django.urls import re_path
from newApp import views
urlpatterns = [
    re_path(r'^$',views.help, name = 'help' )
]
