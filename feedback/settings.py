from django.conf import settings

RECIPIENTS = getattr(settings, 'FEEDBACK_RECIPIENTS', settings.MANAGERS)
NEXT_URL = getattr(settings, 'FEEDBACK_NEXT_URL', '')

