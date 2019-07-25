from __future__ import unicode_literals
from django import template
from bookkeeping.models import BookChargeSheet
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag('head_tiles.html')
def get_story_item():
    print("getting book types")
    return_dict = {'book_types': BookChargeSheet.objects.all()}
    return return_dict