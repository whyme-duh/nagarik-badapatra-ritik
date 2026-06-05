from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.views.generic.base import RedirectView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from .forms import PasswordResetFormWithCaptcha  # Commented out since CAPTCHA is removed
from django.contrib.auth.views import LoginView
# from .forms import AdminLoginForm  # Commented out since CAPTCHA is removed

urlpatterns = [
    # Admin login URL
    path("admin/login/", LoginView.as_view(), name='admin_login'),  # Removed custom form

    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico', permanent=True)),


    # Admin panel URL
    path('admin/', admin.site.urls),

    #-------------------------------------------------------------------
    # Newly added
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    #------------------------------------------------------------------

    # Password reset URLs
    path('password_reset/', PasswordResetView.as_view(
        # form_class=PasswordResetFormWithCaptcha,  # Commented out
        email_template_name="registration/password_reset_email.html",
        extra_context={'site_name': 'TechProgramming'}
    ), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Include pages URLs
    path('', include('pages.urls')),  # Include your app's URLs
]

admin.site.site_header = "Digital Nagarik Badapatra | Citizen Charter | Nepal"
admin.site.site_title = "Digital Nagarik Badapatra | Citizen Charter | Nepal"
admin.site.index_title = "Digital Nagarik Badapatra | Citizen Charter | Nepal"

# Serve media files in development (when DEBUG=True)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)