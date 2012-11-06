from django import template
from django.db.models import Q

from cloudless.models import Page

register = template.Library()

class FeedbackSubjectsNode(template.Node):

    def __init__(self, var_name):
         self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Page.objects\
                                        .filter(Q(feedback_subject=True) | Q(parent__children_feedback_subject=True)).distinct()
        return ''


def do_feedback_subjects(parser, token):
    try:
        tag_name, _as, var_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly two arguments" % token.contents.split()[0]
    if _as != 'as':
        raise TemplateSyntaxError(_("first argument to %s tag must be 'as'") % tag_name)

    return FeedbackSubjectsNode(var_name)

register.tag('feedback_subjects', do_feedback_subjects)
