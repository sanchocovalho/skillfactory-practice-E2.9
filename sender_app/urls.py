from sender_app import views
from django.urls import path

app_name = 'sender_app'

urlpatterns = [
    path('', views.EmailSenderCreate.as_view(), name='email_create'),
    path('list/', views.EmailSenderList.as_view(), name="email_list"),
    path('update/', views.update_status, name="update_status"),
]
