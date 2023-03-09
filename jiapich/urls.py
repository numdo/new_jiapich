from django.urls import path
from jiapich import views

app_name = 'jiapich'
urlpatterns = [
    path('',views.lists,name = 'list'),
    path('<int:submitForm_id>/',views.detail,name='detail'),
    path('jiapich/form_insert/',views.form_create,name='form_create'),
]