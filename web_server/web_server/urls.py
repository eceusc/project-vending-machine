from web_server import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.root, name='root'),
    path('github_webhook' ,views.github_webhook, name='github_webhook'),
    path('admin/', admin.site.urls),
]
