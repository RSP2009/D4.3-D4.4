
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.views import View
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter  # импортируем фильтр D4.2

p = Paginator(Post, 1)

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

class NewsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'flatpages/news_search.html'  # указываем имя шаблона HTML, в котором все инструкции, как должны вывестись наши объекты
    context_object_name = 'news' # 'это имя списка, в котором будут лежать все объекты
    queryset = Post.objects.order_by('-dateCreation')  # сортировка по дате в порядке убывания
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset = self.get_queryset())
        # context['value1'] = None
        return context

class NewsDetail(DetailView):
    model = Post
    template_name ='flatpages/news_separately.html'
    context_object_name = 'news_separately'

