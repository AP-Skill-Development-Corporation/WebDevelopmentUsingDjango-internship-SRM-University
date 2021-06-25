from django.shortcuts import render


def index(request):
    return render(request, 'demo.html', {})

def say_hi(request, name):
    name_ = name.title()

    return render(request, 'say_hi.html',{'name': name_,
            'college': 'SRM'})

def table(request, num):
    l = []

    for i in range(1,11):
        l.append(i*num)
    return render(request,'table.html',{'num':num, 'list': l})