"""clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import list_clients, test_function, special_case_2013, special_case, special_case_year_month, greetings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', test_function),
    path('articles/2013/', special_case_2013),
    path('articles/<int:year>/', special_case),
    path('articles/<int:year>/<int:month>/', special_case_year_month),
    path('clients/', list_clients),
    path('hello/<str:name>', greetings),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
