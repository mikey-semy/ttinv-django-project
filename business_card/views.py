from django.shortcuts import render

nav = [
    {'name': 'О нас', 'url': 'index'},
    {'name': 'Продукция', 'url': 'index'},
    {'name': 'Контакты', 'url': 'index'},
]

def index(request):
    data = {
        'title': 'ТехТрансИнвест',
        'nav': nav,
    }

    return render(request, 'business_card/index.html', context=data)


def page_not_found(request, exception):
    data = {
        'title': 'Опс...',
        'nav': nav,
    }

    return render(request, 'business_card/page404.html', context=data)
