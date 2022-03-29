from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import *
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .filters import *
from .forms import PostForm  # импортируем нашу форму


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все
    # инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')
    paginate_by = 5
    comments = Comment.objects.all()
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

        # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. 
        # В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса 
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Post.objects.select_related().all()
        return context


class CommentList(ListView):
    model = Comment
    template_name = 'post.html'
    context_object_name = 'comments'


class CommentDetail(DetailView):
    model = Comment
    template_name = 'post.html'
    context_object_name = 'comment'


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts_search'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['time_now'] = datetime.utcnow()
#        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
#        return context
    
    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }
