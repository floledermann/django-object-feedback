from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.validators import validate_email

from django.contrib.sites.models import Site

from cloudless.models import Page

from feedback import settings

def send_feedback(request):
    from_email = request.REQUEST.get('email', '')
    try:
        validate_email(from_email)
    except:
        from_email = settings.FROM_EMAIL

    try:
        subject = Page.objects.get(id=int(request.REQUEST.get('feedback_subject', ''))).title
    except Exception, ex:
        subject = 'General Inquiry'

    send_mail('%s Inquiry: %s' % (Site.objects.get_current().name, subject),'', from_email, [a[1] for a in settings.RECIPIENTS])
    next = request.REQUEST.get('next', settings.NEXT_URL)
    return redirect(next)
