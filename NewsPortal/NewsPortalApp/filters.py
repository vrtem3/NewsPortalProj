from django_filters import FilterSet
from .models import *
 
 
# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'date_create': ['gte'],
        }

