from django.http import HttpResponse
from django.shortcuts import render


def do_sumTotal(value1, value2):
    return value1 + value2


def list_clients(request):
    return HttpResponse('Hello from client')


def test_function(request):
    tot = do_sumTotal(10,39)
    p_flag = False
    people = ['Tejas', 'Hiral', 'Deep']
    return render(request, 'example.html', {'total': tot, 'people': people, 'flag': p_flag})


def special_case_2013(request):
    return HttpResponse('case from 2013')


def special_case(request, year):
    return HttpResponse('case from %s' % year)


def special_case_year_month(request, year, month):
    return HttpResponse('::articles from year %s and month %s' %(year, month))


def greetings(request, name):
    return HttpResponse('Hello %s' % name)

