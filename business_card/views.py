from django.shortcuts import render

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

benefits = [
    {
        'img': {
                'url': ''
                },
        'title': 'Осуществляем консультации по подбору',
        'subtitle': 'А также проводим консультации по условиям работы и выявлению причин выхода из строя подшипников и узлов',
    },
    {
        'title': 'Опыт работы более 8 лет',
        'subtitle': 'За это время зарекомендовала себя как надёжный поставщик подшипников и элементов промышленных трансмиссий для различных отраслей промышленности',
    },
    {
        'title': 'Доставка собственным транспортом',
        'subtitle': 'Осуществляем достувку даже в небольшие населенные пункты!',
    },
]
def index(request):
    data = {
        'title': 'ТехТрансИнвест',
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
