from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/<int:id>', views.deleteObj),
    path('about', views.about, name = 'about'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('test/<int:id>/', views.test),
    path('Today', views.getCourentDate),
    path("Random", views.get_random_quote),
    path("products", views.get_products, name = 'products'),
    path("buyers", views.get_Buyers, name = 'buyers'),
    path("Restauran", views.restauranMain),
    path("Reastauran/add/Restauran", views.addRestauran),
    path("Homework7/3", views.homework7_3),
    path("Homework7/4", views.homework7_4),
    path("Homework7/5", views.homework7_5),
]