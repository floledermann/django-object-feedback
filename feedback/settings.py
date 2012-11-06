from django.conf import settings

RECIPIENTS = getattr(settings, 'FEEDBACK_RECIPIENTS', settings.MANAGERS)
FROM_EMAIL = getattr(settings, 'FEEDBACK_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)

NEXT_URL = getattr(settings, 'FEEDBACK_NEXT_URL', '')

