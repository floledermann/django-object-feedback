from django.shortcuts import redirect

from feedback import settings

def send_feedback(request):
    next = request.REQUEST.get('next', settings.NEXT_URL)
    return redirect(next)
