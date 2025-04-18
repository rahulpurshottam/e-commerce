"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from mysite import views  
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  
    # path('saveform/', views.saveForm, name="submitform"),
    path('payment-processing/<int:product_id>', views.checkout, name='payment'),
    path('payment-processing/', views.checkout, name='payment'),
    path('contact/', views.contactUs, name='contact'),
    # path('success/', views.order,name='order'),
    path('', views.LOGIN, name='login'),
    path('login/', views.LOGIN ,name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('home/', views.homePage, name='home'),  
    path('save-order/', views.save_order, name='save_order'),
    path('contact/', views.contactUs, name='contact'),
    # path('success/', views.success, name='success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



