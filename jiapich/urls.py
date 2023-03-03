from django.urls import path
from jiapich import views

app_name = 'jiapich'
urlpatterns = [
    path('hello/', views.hello),
]