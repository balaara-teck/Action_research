from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import FileModel  # replace with your blog model name

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return FileModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # make sure your model has updated_at or date field

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ['home', 'about']  # replace with your named URLs

    def location(self, item):
        return reverse(item)
