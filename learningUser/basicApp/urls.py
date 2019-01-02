from django.urls import re_path
from . import views

app_name = 'basicApp'
urlpatterns = [
    re_path('^register/$',views.register, name='register'),
]
