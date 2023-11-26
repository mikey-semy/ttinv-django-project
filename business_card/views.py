from django.shortcuts import render
from .models import Benefits

logo = {
    'title': 'TechTransInvest',
    'is_img': True,
    'src': '/static/business_card/images/logo.svg',
    'href': "/"
}

nav = [
    {'name': 'О нас', 'url': 'index'},
    {'name': 'Продукция', 'url': 'index'},
    {'name': 'Контакты', 'url': 'index'},
]

captions = {
    'benefits': {
            'title': 'Наши преимущества',
            'subtitle': 'Мы всегда выстраиваем долгосрочные и взаимовыгодные отношения и будем рады видеть Вашу компанию в числе наших партнёров!',
    },
    'brands': {
            'title': 'Бренды',
            'subtitle': '',
    },
    'contacts': {
            'title': 'Контакты',
            'subtitle': '',
    },
    'products': {
            'title': 'Продукция',
            'subtitle': '',
    },
}


def index(request):
    benefits = Benefits.objects.all()
    data = {
        'title': 'ТехТрансИнвест',
        'logo': logo,
        'nav': nav,
        'captions': captions,
        'benefits': benefits,
    }
    return render(request, 'business_card/index.html', context=data)


def page_not_found(request, exception):
    data = {
        'title': 'Опс...',
        'nav': nav,
    }

    return render(request, 'business_card/page404.html', context=data)
