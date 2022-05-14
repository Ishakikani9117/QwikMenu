"""eventmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# from django.conf.urls import url
from enroll import views
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$' , views.index, name='index'),
    re_path(r'^index.html' , views.index, name='index'),
    re_path(r'^login_page.html', views.log, name="log"), 
    re_path(r'^createacc.html', views.create, name="create"), 
    re_path(r'^order.html', views.order_now, name="create"), 
    re_path(r'^add_item.html', views.add, name="add"),
    re_path(r'^dashboard.html', views.dashbrd, name="dashbrd"),
    re_path(r'^delete_item.html', views.delt, name="delt"),
    re_path(r'^web.html', views.webb, name="webb"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)