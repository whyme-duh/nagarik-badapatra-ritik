from django.contrib import admin
from .models import Page, File, ContactInfo, AboutUs, TermsAndConditions, PrivacyPolicy, WelcomeText,FaQs

admin.site.register(TermsAndConditions)
admin.site.register(FaQs)
admin.site.register(PrivacyPolicy)
admin.site.register(AboutUs)
admin.site.register(ContactInfo)
admin.site.register(WelcomeText)  # Register the new model

class FileInline(admin.TabularInline):
    model = File
    extra = 1

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [FileInline]

admin.site.register(Page, PageAdmin)
