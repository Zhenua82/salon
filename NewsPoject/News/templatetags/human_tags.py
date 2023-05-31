from homework.models import Profession
from django import template
from django.db.models import Count, F
from django.core.cache import cache

register = template.Library()
@register.simple_tag(name='get_list_profession')
def get_profession():
    # return Profession.objects.all()
    return Profession.objects.annotate(cnt=Count('human'))

@register.inclusion_tag('homework/list_profession.html')
def show_professions(arg1='Перечень', arg2='профессий'):
    # professions = Profession.objects.all()
    # professions = Profession.objects.annotate(cnt=Count('human')).filter(cnt__gt=0)
    professions = cache.get('professions')
    if not professions:
        professions = Profession.objects.annotate(cnt=Count('human', filter=F('human__is_published'))).filter(cnt__gt=0)
        cache.set('professions', professions, 30)
    return {'professions': professions, 'arg1': arg1, 'arg2': arg2}
