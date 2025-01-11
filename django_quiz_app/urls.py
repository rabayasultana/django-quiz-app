# """
# URL configuration for django_quiz_app project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]




from django import views
from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', views.home, name='home'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('add/', views.add_question, name='add_question'),
    path('questions/', views.all_questions, name='all_questions'),
    # path('members/', views.members),
    # path('members/details/<int:id>', views.details, name='details'),
]

