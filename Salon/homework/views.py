from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Human, Profession
from .forms import HumanForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'homework/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'homework/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Login')
