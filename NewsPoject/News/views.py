from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
            # return redirect('Login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        # form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'News/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'News/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Login')

class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/home_news_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')

class NewsByCategory(ListView):
    model = News
    template_name = 'News/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')
class ViewNews(DetailView):
    model = News
    context_object_name = 'news_i'
    template_name = 'News/view_news.html'
class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    login_url = '/admin/'
    # redirect_field_name = "redirect_to"

def test(request):
    news = News.objects.all()
    paginator = Paginator(news, 2)
    page_num = request.GET.get('page', 1)
    page_news = paginator.get_page(page_num)
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'page_obj': page_news
    }
    return render(request, 'News/index.html', context=context)

# def test(request):
#     objects = ['ohn', 'kjidsa', 'bbfk', 'hfhh', 'nbbkn', 'bdvkdj']
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'News/test.html', {'page_obj': page_objects})


# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, 'News/index.html', context=context)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, 'News/category.html', context=context)

# def view_news(request, news_id):
#     # news_i = News.objects.get(pk=news_id)
#     news_i = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_i': news_i
#     }
#     return render(request, 'News/view_news.html', context=context)

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'News/add_news.html', {'form': form})
