"""uniformauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aduploadapp/', include('aduploadapp.urls')), # https://127.0.0.1./aduploadapp/
]


# 사용자가 접속할 때, 프로젝트 루트라 할 수 있는 uniformauto/uniformauto/urls.py 를 먼저 읽고 
# 그 다음 해당 URL을 우선 해석한 후 특정앱의 Url.py 로 다시 전달한다.
