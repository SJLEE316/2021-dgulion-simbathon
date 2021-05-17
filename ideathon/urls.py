from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='ideathon'
urlpatterns =[
    path('', views.main, name="main"),
    path('single_post/', views.single_post, name="single_post"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)