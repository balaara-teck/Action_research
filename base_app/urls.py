from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, StaticViewSitemap

sitemaps = {
    'posts': PostSitemap,
    'static': StaticViewSitemap,
}



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
    path('load-more/', views.load_more_files, name='load_more_files'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("files/<int:pk>/", views.File_detail, name="file_detail")

]


urlpatterns += [
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
