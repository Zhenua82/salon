from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Human, Profession, Review
from .forms import HumanForm, UserRegisterForm, UserLoginForm, ReviewForm
from django.contrib import messages
from django.contrib.auth import login, logout

def home(request):
    human = Human.objects.filter(is_published=True)
    human_2 = Human.objects.all()
    professions = Profession.objects.all()
    paginator = Paginator(human, 10)
    page_num = request.GET.get('page', 1)
    page_human = paginator.get_page(page_num)
    context = {
        'human_2': human_2,
        'human': human,
        'title': 'Стрижки и маникюр',
        'title2': 'Наши мастера:',
        'page_obj': page_human
    }
    return render(request, 'homework/home.html', context=context)
class get_profession(ListView):
    model = Human
    template_name = 'homework/home.html'
    context_object_name = 'human'
    allow_empty = True
    paginate_by = 20
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Profession.objects.get(pk=self.kwargs['profession_id']).title
        context['human_2'] = Human.objects.all()
        return context

    def get_queryset(self):
        return Human.objects.filter(profession_id=self.kwargs['profession_id'], is_published=True).select_related('profession')

class human_1(DetailView):
    model = Human
    context_object_name = 'human_i'
    template_name = 'homework/human_1.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['human_2'] = Human.objects.all()
        return context

class review(ListView):
    model = Review
    context_object_name = 'review'
    template_name = 'homework/review.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['human_2'] = Human.objects.all()
        return context
class add_human(LoginRequiredMixin, CreateView):
    # form_class = HumanForm
    # template_name = 'homework/add_human.html'
    # login_url = '/admin/'
    form_class = ReviewForm
    template_name = 'homework/add_human.html'
    login_url = '/admin/'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['human_2'] = Human.objects.all()
        return context

def register(request):
    human_2 = Human.objects.all()
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
    return render(request, 'homework/register.html', {'form': form, 'human_2': human_2})

def user_login(request):
    human_2 = Human.objects.all()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'homework/login.html', {'form': form, 'human_2': human_2})

def user_logout(request):
    logout(request)
    return redirect('Login')

