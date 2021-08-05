from django.urls import path
from  xabarlar.views import Asosiysahifa

urlpatterns=[
    path('',Asosiysahifa.as_view(),name='asosiy')
]