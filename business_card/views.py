from django.shortcuts import render
from .models import Benefits, Products, Delivery

from datetime import datetime

logo = {
    'title': 'TechTransInvest',
    'is_img': True,
    'src': '/static/business_card/images/logo.svg',
    'href': "/",
}

nav = [
    {'name': 'О нас', 'url': '#benefits'},
    {'name': 'Продукция', 'url': '#products'},
    {'name': 'Доставка', 'url': '#delivery'},
    {'name': 'Контакты', 'url': '#contacts'},

]



socials = [
    {
        "icon": "map",
        "label": "Найти нас",
        "size": "sm",
        "color": "#fff",
        "href": "https://yandex.ru/maps/?rtext=~59.221150%2C39.891226",
    },
    {
        "icon": "envelope",
        "label": "Написать нам",
        "size": "sm",
        "color": "#fff",
        "href": "mailto:textrans.invest@mail.ru",
    },
    {
        "icon": "phone",
        "label": "Позвонить нам",
        "size": "sm",
        "color": "#fff",
        "href": "tel:8(8172)70-10-61",
    },
]

contacts = {
    "address":
        {
            "title": "Адрес",
            "data": "Вологодская область, г. Вологда, ул. Каменный мост, д. 6, оф. 4",
        },
    "email":
        {
            "title": "Электронный адрес",
            "data": "textrans.invest@mail.ru",
        },
    "phone":
        {
            "title": "Телефон",
            "data": "8 (8172) 70-10-61",
        },
    "time":
        {
            "title": "Часы работы",
            "data":
                {
                    "workdays": "ПН - ПТ: 9:00 - 17:00",
                    "weekend": "СБ - ВС: Выходной",
                },
        },
},

requisites = [
    {
        "title": "Полное наименование",
        "subtitle": "Общество с ограниченной ответственностью «ТехТранс Инвест»",
    },
    {
        "title": "Сокращенное наименование",
        "subtitle": "ООО «ТехТранс Инвест»",
    },
    {
        "title": "ИНН/КПП",
        "subtitle": "3525289483/352501001",
    },
    {
        "title": "ОГРН",
        "subtitle": "1123525017681",
    },
    {
        "title": "Юридический (Физический) адрес",
        "subtitle": "160000, Вологодская обл., г. Вологда, ул. Каменный мост, д. 6, оф. 4",
    },
    {
        "title": "Банковские реквизиты",
        "subtitle": "Р/с: 407 028 104 84 00000 2087, в Ф. ОПЕРУ Банка ВТБ (ПАО) в г. Санкт-Петербурге, К/счет: 30101810200000000704, БИК: 044030704",
    },
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
    'delivery': {
        'title': 'Доставка',
        'subtitle': 'Обладая собственным автопарком автомобилей, а также успешно сотрудничая с транспортными компаниями, '
                    'мы можем решать любые логистические задачи, осуществляя доставку даже в небольшие населенные пункты',
    },
}

dialogs = {
    'delivery': {
        'dellin': {
            'name': 'Деловые линии',
            'class': 'dellin',
            'content':
                '''
            
                ''',
        },
        'pek': {
            'name': 'ПЭК',
            'class': 'pek',
            'content':
                '''

                ''',
        },
        'baikalsr': {
            'name': 'Байкал Сервис',
            'class': 'baikalsr',
            'content':
                '''

                ''',
        }
    }

}

copyright = {
    'year': '© ' + str(datetime.now().year) + ', ',
    'name': 'TechTransInvest',
    'link': 'https://ttinv.ru/',
}


def index(request):
    benefits = Benefits.objects.all()
    products = Products.objects.all()
    deliveries = Delivery.objects.all()
    data = {
        'title': 'ТехТрансИнвест',
        'logo': logo,
        'nav': nav,
        'socials': socials,
        'captions': captions,
        'benefits': benefits,
        'products': products,
        'contacts': contacts,
        'requisites': requisites,
        'copyright': copyright,
        'deliveries': deliveries,
    }
    return render(request, 'business_card/index.html', context=data)


def page_not_found(request, exception):
    data = {
        'title': 'Опс...',
        'nav': nav,
    }

    return render(request, 'business_card/page404.html', context=data)
