"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from drf_yasg.openapi import Info, Contact  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore

from app.transport.handlers.get_employees import GetDepartmentEmployees
from app.transport.handlers.get_department_tree import GetDepartmentTree


SchemaView = get_schema_view(
    info=Info(
        contact=Contact(email='bokailya@gmail.com'),
        default_version='v1',
        description='Traffic Light CPA test',
        title='Traffic Light CPA',
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/department-employees', GetDepartmentEmployees.as_view()),
    path('api/department-tree', GetDepartmentTree.as_view()),
    url(r'^swagger/$', SchemaView.with_ui('swagger')),
]
