from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("read/<str:pk>", views.File_reader, name="read"),
    path("pricing", views.Pricing, name="pricing"),
    path('contact/', views.contact_view, name='contact'),
    path("donate/", views.donate_view, name="donate"),
    path("about/", views.about_view, name="about"),
    path('coming-soon/', views.under_development_view, name='under_development'),
    path('search/', views.search_files, name='search_files'), 
    path('search/<str:category>/', views.search_files, name='search_files'),
    path('all_topics/', views.all_topics, name='all_topics'),
    path('field_topic/<str:field>/', views.field_topics, name='field_topic'),


]
