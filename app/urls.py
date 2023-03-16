from django.urls import path
from app.views import *

app_name='six'

urlpatterns=[
    path('csk/',csk,name='csk')
]