#sifanx/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    #path('single/', views.single, name='single'),
    path('testimonial/', views.testimonialCreate.as_view(), name='testimonial'),
    path('feedback', views.feedbackCreate.as_view(), name='feedback'),
    path('thks', views.thks, name='thks'),
    path('see_testimonial', views.see_testimonial,name='see_testimonial'),
]