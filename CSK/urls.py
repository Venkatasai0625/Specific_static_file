from django.urls import path
from CSK.views import *
app_name='CSK'
urlpatterns = [
    path('yellow/',yellow,name='yellow'),
]
