from django_filters import FilterSet
from .models import Post

#создаём фильтр
class PostFilter(FilterSet):
    # здесь в мета-классе надо предоставить модель и указать поля, по которым будет фильтроваться информация о постах
    class Meta:
        model = Post
        # поля, которые будем фильтровать (имена беруться из моделей)
        # fields = {'author', 'dateCreation', 'title'}
        fields = {
            'author': ['exact'], # что-то похожее...
            'title': ['icontains'],
            'dateCreation': ['gt']  # дата должна быть больше или равна той, что указал пользователь
        }
