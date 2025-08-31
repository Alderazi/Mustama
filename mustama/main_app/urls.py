from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('app/about/',views.about,name='about'),
    path('record/index',views.record_index,name='index'),
    path('record/myRecord',views.record_myRecord,name='myRecord')
]
