from django.urls import path
from jiapich import views
from .views import MyFormWizardView

app_name = 'jiapich'
urlpatterns = [
    path('',views.lists,name = 'list'),
    path('<int:submitForm_id>/',views.detail,name='detail'),
    path('jiapich/form_insert/',views.form_create,name='form_create'),
    path('my-form/', MyFormWizardView.as_view()),
]