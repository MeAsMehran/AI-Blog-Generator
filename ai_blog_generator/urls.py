"""
URL configuration for ai_blog_generator project.

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
from django.urls import path , include
from blog import views
# from blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcomePage'),
    path('ai blog/', views.mainPage, name='aiBlogPage'),
    path('signup/', views.signupuser, name='signupPage'),
    path('login/', views.loginuser, name='loginPage'),
    path('logout/', views.logoutuser, name='logoutPage'),
    path('generate-blog/', views.generateBlog, name='generateBlogPage'),
    path('allBlogs/', views.allBlogs, name='allBlogsPage'),
    # path('blog/<int>', views.blogDetail, name='blogDetailsPage'),
    path('blog/', include('blog.urls')),

    
]
