# pages/context_processors.py
from .models import ContactInfo

def global_logo(request):
    contact_info = ContactInfo.objects.first()  # Get the first ContactInfo instance
    return {
        'global_logo': contact_info.logo.url if contact_info and contact_info.logo else None
    }
