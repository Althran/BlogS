from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
    path('about/', views.about, name='about'),
    path('<slug:post>/', views.post_detail, name='detail'),
]


