from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat


from django.contrib.sites.models import Site

from cloudless.models import Page

from feedback import settings

def send_feedback(request):
    from_email = request.REQUEST.get('email', None)
    try:
        validate_email(from_email)
    except:
        from_email = settings.FROM_EMAIL

    try:
        subject = Page.objects.get(id=int(request.REQUEST.get('feedback_subject', ''))).title
    except Exception, ex:
        subject = _('General Inquiry')

    keys = request.POST.keys()
    keys.remove('feedback_subject')
    keys.sort()
    body = '\n'.join(['%s: %s' % (a.lstrip('0123456789_-'), request.REQUEST.get(a, '')) for a in keys])

    send_mail(string_concat(Site.objects.get_current().name,' ',_('Inquiry: '), subject), body, from_email, [a[1] for a in settings.RECIPIENTS])
    next = request.REQUEST.get('next', settings.NEXT_URL)
    return redirect(next)
