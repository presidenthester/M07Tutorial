from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', include('blog.urls')),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
]