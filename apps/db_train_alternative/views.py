from django.http import JsonResponse
from django.views import View
from .models import Author
from django.views.decorators.csrf import csrf_exempt
import json


class AuthorREST(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, id=None):
        if id is None:
            data = []
            for author in Author.objects.all():
                data_author = {'id': author.id,
                               'name': author.name,
                               'email': author.email}
                data.append(data_author)
        else:
            author = Author.objects.filter(id=id)
            if author:
                author = author.first()
                data = {'id': author.id,
                        'name': author.name,
                        'email': author.email}
            else:
                return JsonResponse(
                    {'error': f'Автора с id={id} не найдено!'},
                    status=404,
                    json_dumps_params={"ensure_ascii": False, "indent": 4}
                )
        return JsonResponse(data, safe=False, json_dumps_params={
            "ensure_ascii": False,
            "indent": 4
        })

    def post(self, request):
        try:
            data = json.loads(request.body)
            author = Author(name=data['name'], email=data['email'])
            author.clean_fields()
            author.save()
            response_data = {
                'message': f'Автор успешно создан',
                'id': author.id,
                'name': author.name,
                'email': author.email
            }
            return JsonResponse(
                response_data, status=201,
                json_dumps_params={"ensure_ascii": False, "indent": 4}
            )
        except Exception as e:
            return JsonResponse(
                {'error': str(e)}, status=400,
                json_dumps_params={"ensure_ascii": False, "indent": 4}
            )

    def put(self, request, id):
        try:
            author = Author.objects.get(id=id)
            data = json.loads(request.body)
            author.name = data['name']
            author.email = data['email']
            author.clean_fields()
            author.save()

            response_data = {
                'message': f'Данные автора успешно изменены',
                'id': author.id,
                'name': author.name,
                'email': author.email
            }
            return JsonResponse(
                response_data,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
        except Author.DoesNotExist:
            return JsonResponse(
                {'error': 'Автор не найден'},
                status=404,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
        except Exception as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )

    def patch(self, request, id):
        try:
            author = Author.objects.get(id=id)
            data = json.loads(request.body)

            for key, value in data.items():
                setattr(author, key, value)
            author.clean_fields()
            author.save()

            response_data = {
                'id': author.id,
                'name': author.name,
                'email': author.email
            }
            return JsonResponse(
                response_data,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
        except Author.DoesNotExist:
            return JsonResponse(
                {'error': f'Автор с id={id} не найден'},
                status=404,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
        except Exception as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )

    def delete(self, request, id):
        try:
            author = Author.objects.get(id=id)
            author.delete()
            return JsonResponse(
                {'message': 'Автор успешно удалён'},
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
        except Author.DoesNotExist:
            return JsonResponse(
                {'error': 'Автор не найден'},
                status=404,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
        except Exception as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
                json_dumps_params={"ensure_ascii": False, "indent": 4},
            )
