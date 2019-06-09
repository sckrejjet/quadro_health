from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='health-home'),
    path('about', views.about, name='health-about'),
    path('adding_page', views.adding_page),
    path('add_hospital', views.add_hospital),
    # path('adding_service', views.adding_service, name='Добавление услуги'),
    path('filtered_request', views.filtered_hospitals),
]