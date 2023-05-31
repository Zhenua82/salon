from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Human, Profession
from .forms import HumanForm

# class home(ListView):
#     model = Human
#     context_object_name = 'human'
#     template_name = 'homework/home.html'
#     extra_context = {'title': 'Список'}
#     # paginate_by = 3
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Список людей'
#         return context
#     def get_queryset(self):
#         # return Human.objects.filter(is_published=True).select_related('profession')
#         return Human.objects.filter().select_related('profession')

def home(request):
    human = Human.objects.filter(is_published=True)
    human_2 = Human.objects.all()
    professions = Profession.objects.all()
    paginator = Paginator(human, 3)
    page_num = request.GET.get('page', 1)
    page_human = paginator.get_page(page_num)
    context = {
        'human_2': human_2,
        'human': human,
        'title': 'Список людей',
        'title2': 'Список людей:',
        'page_obj': page_human
    }
    return render(request, 'homework/home.html', context=context)
class get_profession(ListView):
    model = Human
    template_name = 'homework/home.html'
    context_object_name = 'human'
    allow_empty = True
    paginate_by = 2
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Profession.objects.get(pk=self.kwargs['profession_id']).title
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id'], is_published=True).select_related('profession')

class human_1(DetailView):
    model = Human
    context_object_name = 'human_i'
    template_name = 'homework/human_1.html'

class add_human(LoginRequiredMixin, CreateView):
    form_class = HumanForm
    template_name = 'homework/add_human.html'
    login_url = '/admin/'
    # redirect_field_name = "redirect_to"

# def home(request):
#     human = Human.objects.all()
#     professions = Profession.objects.all()
#     context = {
#         'human': human,
#         'title': 'Список людей',
#         'title2': 'Список людей:',
#
#     }
#     return render(request, 'homework/home.html', context=context)

# def get_profession(request, profession_id):
#     human = Human.objects.filter(profession_id=profession_id)
#     professions = Profession.objects.all()
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'human': human,
#         'profession': profession
#     }
#     return render(request, 'homework/profession.html', context=context)

# def human_1(request, human_id):
#     # human_i = Human.objects.get(pk=human_id)
#     human_i = get_object_or_404(Human, pk=human_id)
#     context = {
#         'human_i': human_i
#     }
#     return render(request, 'homework/human_1.html', context=context)

# def add_human(request):
#     if request.method == 'POST':
#         form = HumanForm(request.POST)
#         if form.is_valid():
#             # human = Human.objects.create(**form.cleaned_data)
#             human = form.save()
#             return redirect(human)
#     else:
#         form = HumanForm()
#     return render(request, 'homework/add_human.html', {'form': form})