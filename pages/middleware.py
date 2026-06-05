from django.shortcuts import redirect
from .functions import check_admin_auto_logout

class AdminAutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Middleware: request.user exists? {'user' in dir(request)}")  # Debugging
        if check_admin_auto_logout(request):  # Check if user should be logged out
            return redirect('/admin/logout/')  # Redirect to logout page
        return self.get_response(request)
