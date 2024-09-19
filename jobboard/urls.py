# jobboard/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from jobs import views as job_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Homepage URL pattern
    path('', job_views.homepage, name='homepage'),

    # Admin URL pattern
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', job_views.signup, name='signup'),
    path('accounts/profile/', job_views.profile, name='profile'),

    # Jobs app URLs
    path('jobs/', include('jobs.urls')),  # Include jobs app URLs under 'jobs/' path
]

# Serve media files in development (if MEDIA_URL and MEDIA_ROOT are set in settings.py)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
