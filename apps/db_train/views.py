from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        # Находим автора с наибольшей самооценкой
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        # Автор с наибольшим количеством опубликованных статей
        self.answer2 = Author.objects.annotate(article_count=Count('entries')).order_by('-article_count').first()

        # Статьи с тегами 'Кино' или 'Музыка'
        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка']).distinct()

        # Количество авторов женского пола
        self.answer4 = Author.objects.filter(gender='Ж').count()

        # Процент авторов, согласившихся с правилами при регистрации
        total_authors = Author.objects.count()
        agreed_authors = Author.objects.filter(status_rule=True).count()
        self.answer5 = (agreed_authors / total_authors * 100) if total_authors > 0 else 0

        # Авторы со стажем от 1 до 5 лет
        self.answer6 = Author.objects.filter(authorprofile__experience__gte=1, authorprofile__experience__lte=5)

        # Автор с наибольшим возрастом
        self.answer7 = Author.objects.order_by('-age').first()

        # Количество авторов, указавших номер телефона
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()

        # Авторы младше 25 лет
        self.answer9 = Author.objects.filter(age__lt=25)

        # Количество статей, написанных каждым автором
        self.answer10 = Author.objects.annotate(article_count=Count('entries')).values('username', 'article_count')


        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
