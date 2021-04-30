from django.urls import path
from . import views

app_name="compilerhome"

urlpatterns=[
    path('',views.render_home,name='home')
]