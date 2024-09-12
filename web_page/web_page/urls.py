"""
URL configuration for web_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dataworks_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createcategory/', views.create_category, name='createcategory'),
    path('categorylist', views.category_list, name='category_list'),
    path('createcourse/', views.create_course, name='create_course'),
    path('courselist/', views.course_list, name='course_list'),
    path('create_course_types/', views.create_course_type,name='create_course_types'),
    path('course_types_list/', views.course_types_list,name='course_types_list'),
    path('course_by_type/<int:pk>/',views.course_by_type, name='course_by_type'),
    path('course_type/<int:course_type_id>/', views.course_type_detail, name='course_type_detail'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/update/', views.update_course),
    path('courses/<int:pk>/delete/', views.delete_course),
    path('enrollment-success/', views.enrollment_success, name='enrollment_success'),
    path('category_course/', views.category_course, name='category_course'),
    path('foundations_test/', views.foundations_test, name='foundations_test'),
    path('foundations_test/<int:course_type_id>/', views.foundations_test, name='foundations_test_filtered'),
    path('corporate/', views.corporate_view, name='corporate'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog_list/', views.blog_list_view, name='blog_list'),
    path('blog_header/', views.blog_header_view, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)