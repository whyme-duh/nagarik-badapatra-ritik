# pages/views.py
from django.shortcuts import render, get_object_or_404
from .models import Page
from .models import ContactInfo
from .models import AboutUs  # Import the model that holds About Us content
from .models import TermsAndConditions, PrivacyPolicy, FaQs

from .models import WelcomeText  # Import the model that holds the welcome text


def terms_view(request):
    terms = TermsAndConditions.objects.first()  # Get the first Terms & Conditions entry
    return render(request, "pages/terms.html", {"terms": terms})

def faqs_view(request):
    faqs_data = FaQs.objects.first()  # Fetch the first FAQ entry
    return render(request, "pages/faqs.html", {"FaQs": faqs_data})

def privacy_view(request):
    privacy = PrivacyPolicy.objects.first()  # Get the first Privacy Policy entry
    return render(request, "pages/privacy.html", {"privacy": privacy})
def about(request):
    about_data = AboutUs.objects.first()  # Fetch first entry or modify logic if needed
    return render(request, "pages/about.html", {"about": about_data})


def contact_view(request):
    contact = ContactInfo.objects.first()  # Get the first contact info
    return render(request, 'pages/contact.html', {'contact': contact})

def home(request):
    contact_info = ContactInfo.objects.first()  
    logo_url = contact_info.logo.url if contact_info and contact_info.logo else None  

    welcome_content = WelcomeText.objects.first()  # Fetch welcome title & text

    return render(request, 'pages/home.html', {
        'logo_url': logo_url,
        'welcome_title': welcome_content.title if welcome_content else "Welcome to Nagarik Badapatra Nepal",
        'welcome_text': welcome_content.text if welcome_content else "Welcome to our website!"
    })

# def contact(request):
#     return render(request, 'pages/contact.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})
