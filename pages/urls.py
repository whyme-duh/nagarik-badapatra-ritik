# pages/urls.py
from django.urls import path
from .views import home, page_detail
from .views import contact_view
from .views import about
from .views import terms_view, privacy_view, faqs_view


urlpatterns = [
    path('', home, name='home'),
    path("terms/", terms_view, name="terms"),
     path("faqs/", faqs_view, name="faqs"),
    path("privacy/", privacy_view, name="privacy"),
    # path('contact/', contact, name='contact'),  # First contact view
    path('contact/', contact_view, name='contact'), 
     path("about/", about, name="about"),
    path('<slug:slug>/', page_detail, name='page_detail'),
]
