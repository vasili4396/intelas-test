from django.urls import path

from crawler import views

app_name = 'crawler'

urlpatterns = [
    path('', views.index, name='index'),
    path('crawl/', views.crawl, name='crawl'),
]
