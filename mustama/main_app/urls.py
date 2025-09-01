from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('app/about/',views.about,name='about'),
    path('record/index/',views.record_index,name='index'),
    path('record/myRecord/',views.record_myRecord,name='myRecord'),
    path('record/insert/',views.RecitationCreate.as_view(),name='insert'),
    path('accounts/signup/',views.signup,name='signup'),
    path('adminPage/approval/',views.approval,name='approval'),
    path('adminPage/approval/<int:record_id>/approve/',views.approve,name='approve'),
    path('adminPage/approval/<int:record_id>/reject/',views.reject,name='reject'),
    
]
