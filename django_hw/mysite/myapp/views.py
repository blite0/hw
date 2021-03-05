from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
    })


def first(request):
    return render(request, 'first.html')


def main_article(request):
    return render(request, 'article.html')


def second_arhive(request):
    return render(request, 'archive.html')


def article(request, article_id, name=''):
    return render(request, 'third_first.html', {'article_id': article_id,
                                                'name': name})
# Словарь называется контекст
# def first(request):
#     return HttpResponse("Hey! It's your first view!!")
#
#
# def main_article(request):
#     return HttpResponse('There will be a list with articles')
#
#
# def uniq_article(request):
#     return HttpResponse('This is uniq answer for uniq value')
#
#
# def article(request, article_id, name=''):
#     return HttpResponse(
#         "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
#             name) if name else "This is unnamed article"))
#
#
# def second_arhive(request):
#     return HttpResponse('This is archive')
#
#
# def users(request):
#     return HttpResponse("""1. User-Golova
#     2.User - Noga
#     3.User - Ruka
#     """)
#
#
# def users_number(request, user_number):
#     return HttpResponse(f'This number user{user_number}')
#
#
# def mobile_number(request):
#     return HttpResponse('This is correct mobile_number')
#
#
# def hw_five(request):
#     return HttpResponse('This is fifth work')
