from django.urls import path
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
        path('relative/',views.Relative,name='relative'),
        path('other/',views.other,name='other'),
]
