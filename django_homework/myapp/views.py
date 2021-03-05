from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


# def index(request, article_id):
#     return render(request, 'index.html', {'num': article_id})
def index(request):
    return render(request, 'index.html')


def first(request):
    return render(request, 'first.html')


def main_article(request):
    return render(request, 'article.html')


def second_arhive(request):
    return render(request, 'archive.html')


def article(request, article_id, name=''):
    return render(request, 'third_first.html', {'article_id': article_id,
                                                'name': name})


def base(request):
    return render(request, 'base.html')
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
