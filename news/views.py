from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import render
from django.views import View
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter  # импортируем фильтр D4.2


# p = Paginator(Post, 1)

# page_obj = p.page(1)
# Create your views here.
# def news(reguest):
#
#     all_news = Post.objects.all()
#     print(all_news)
#     return render(reguest, 'news_all.html', context={'data': all_news})
#
# def news_sep(reguest):
#
#     sep_news = Post.objects.all()
#     print(sep_news)
#     return render(reguest, 'news_separately.html', context={'data': sep_news})

class PostForm:
    pass


class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'flatpages/news_search.html'  # указываем имя шаблона HTML, в котором все инструкции, как должны вывестись наши объекты
    context_object_name = 'news'  # 'это имя списка, в котором будут лежать все объекты
    queryset = Post.objects.order_by('-dateCreation')  # сортировка по дате в порядке убывания
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['choices'] = Post.TYPE_CHOICES
        context['form'] = PostForm()
        # context['value1'] = None
        return context

    def post(self, requests, *args, **kwargs):
        form = self.form_class(requests.POST)
        if form.is_valid():
            form.save()
        return super().get(requests, *args, **kwargs)


# дженерик для получения деталей о новости
class NewsDetail(DetailView):
    model = Post
    template_name = 'flatpages/news_separately.html'
    context_object_name = 'news_separately'
    queryset = Post.objects.all()

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы

class NewsCreateView(CreateView):
    template_name = 'flatpages/news_create.html'
    form_class = PostForm

# дженерик для редактирования объекта
class NewsUpdateView(UpdateView):
    template_name = 'flatpages/news_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

# дженерик для удаления новости
class NewsDeleteView(DeleteView):
    template_name = 'flatpages/news_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('news:news_all')  # не забываем импортировать функцию reverse_lazy из пакета django.urls





