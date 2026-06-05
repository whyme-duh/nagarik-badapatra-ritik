from django.conf import settings
from datetime import datetime, timedelta

def check_admin_auto_logout(request):
    """
    Logs out the user if they have been inactive for SESSION_COOKIE_AGE duration.
    """
    if not hasattr(request, 'user'):  # Ensure request.user exists
        return False

    if request.user.is_authenticated and request.path.startswith('/admin/'):
        last_activity = request.session.get('last_activity')

        if last_activity:
            last_activity_time = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
            timeout_seconds = settings.SESSION_COOKIE_AGE  # Default 5 minutes (300s)

            if datetime.now() - last_activity_time > timedelta(seconds=timeout_seconds):
                logout(request)
                request.session.flush()  # Clear session
                return True  # Indicate user should be logged out

        request.session['last_activity'] = str(datetime.now())  # Update last activity time

    return False  # No logout action needed
