from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .api_views import classify_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('simulate/', views.simulate, name='simulate'),
    path('conversations/', views.show_conversations, name='show_conversations'),
    path('classify/', views.classify, name='classify_hugging_face'),
    path('api/classify/', classify_api, name='classify_api'),
    path('classification-results/', views.classification_results, name='classification_results'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),  # Admin paneli yolu buraya eklenmeli
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
