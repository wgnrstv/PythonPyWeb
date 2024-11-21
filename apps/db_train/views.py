from django.db.models import Count, Max
from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        self.answer2 = Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries').first()
        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка']).distinct()
        self.answer4 = Author.objects.filter(gender='ж').count()

        total_authors = Author.objects.count()
        agree_authors = Author.objects.filter(status_rule=True).count()
        self.answer5 = (agree_authors / total_authors) * 100 if total_authors > 0 else 0

        self.answer6 = Author.objects.filter(authorprofile__stage__gte=1, authorprofile__stage__lte=5)
        self.answer7 = Author.objects.order_by('-age').first()
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()
        self.answer9 = Author.objects.filter(age__lt=25)
        self.answer10 = Author.objects.annotate(count=Count('entries')).values('username', 'count')

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
