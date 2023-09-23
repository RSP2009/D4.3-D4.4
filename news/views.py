# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


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
    model = Post
    template_name = 'news_all.html'  # 'default.html'  'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # context['value1'] = None
        return context

class NewsDetail(DetailView):
    model = Post
    template_name ='news_separately.html'
    context_object_name = 'news_separately'