from django.conf import settings

def analytics(request):
    """Adds the setting ANALYTICS_TRACKING_ID to the template context."""
    return {
        'ANALYTICS_TRACKING_ID': getattr(
            settings, 'ANALYTICS_TRACKING_ID', 'UA-XXXXXXX-XX'),
    }


def i18n_extended(request):
    context_extras = {}
    context_extras['SITE_URL'] = settings.SITE_URL.split("http:")[1]

    return context_extras
