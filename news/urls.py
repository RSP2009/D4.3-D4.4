from django.urls import path
from .views import NewsList, NewsDetail

app_name = 'news'
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view(), name='News'),
    path('news/<int:pk>', NewsDetail.as_view()),

]
