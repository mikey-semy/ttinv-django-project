from django.shortcuts import render
from .models import Benefits, Products, Delivery, Brands, Requisites, Catalog, CatalogGroups
from datetime import datetime

logo = {
    'title': 'TechTransInvest',
    'is_img': True,
    'src': '/static/business_card/images/logo.svg',
    'url': "/",
}

nav = {
    'index': [
        {'name': 'О нас', 'url': '#benefits'},
        {'name': 'Продукция', 'url': '#products'},
        {'name': 'Доставка', 'url': '#delivery'},
        {'name': 'Контакты', 'url': '#contacts'},
    ],
    'catalogs': [
        {'name': 'Подшипники', 'url': '#', 'dropdown': True,
         'dropdown_items': [
                {'name': 'Общие каталоги', 'url': '#common'},
                {'name': 'Шариковые подшипники', 'url': '#ball'},
                {'name': 'Роликовые подшипники', 'url': '#'},
                {'name': 'Игольчатые подшипники', 'url': '#'},
                {'name': 'Шарнирные наконечники, шарнирные головки, сферические подшипники скольжения', 'url': '#'},
                {'name': 'Корпусные подшипники, разъемные корпуса', 'url': '#'},
                {'name': 'Втулки скольжения', 'url': '#'},
                {'name': 'Подшипники - Подшипниковые узлы AGRI HUB', 'url': '#'},
            ],
        },
        {'name': 'Приводные ремни', 'url': '#'},
        {'name': 'Смазочные материалы', 'url': '#'},
        {'name': 'Муфты', 'url': '#'},
        {'name': 'Инструменты', 'url': '#'},
    ],
    'pnf': [
        {'name': 'Назад', 'url': '/'},
    ]
}


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

contacts = [
        {
            "name": "address",
            "itemprop": "",
            "icon": {
                "name": "location-dot",
                "size": "xl",
                "color": "#000",
            },
            "title": "Адрес",
            "data": {
                "index": "160000",
                "region": "Вологодская область",
                "city": "г.Вологда",
                "street": "ул.Каменный мост, д. 6, оф. 4",
            },
            "href": "https://yandex.ru/maps/?rtext=~59.221150%2C39.891226"
        },
        {
            "name": "email",
            "itemprop": "email",
            "icon": {
                "name": "envelope",
                "size": "xl",
                "color": "#000",
            },
            "title": "Электронный адрес",
            "data": "textrans.invest@mail.ru",
            "href": "mailto:textrans.invest@mail.ru"
        },
        {
            "name": "phone",
            "itemprop": "telephone",
            "icon": {
                "name": "phone",
                "size": "xl",
                "color": "#000",
            },
            "title": "Телефон",
            "data": "8 (8172) 70-10-61",
            "href": "tel:8(8172)70-10-61",
        },
        {
            "name": "schedule",
            "itemprop": "",
            "icon": {
                "name": "clock",
                "size": "xl",
                "color": "#000",
            },
            "title": "Режим работы",
            "data":
                {
                    "workdays": "ПН - ПТ: 9:00 - 17:00",
                    "weekend": "СБ - ВС: Выходной",
                },
        },
        {
            "name": "requisities",
            "itemprop": "",
            "icon": {
                "name": "file-lines",
                "size": "xl",
                "color": "#000",
            },
            "title": "",
            "data": "Реквизиты",
            "onclick": "showModal(this.dataset.modal)",
        },
]

captions = {
    'benefits': {
        'title': 'Наши преимущества',
        'subtitle': 'Мы всегда выстраиваем долгосрочные и взаимовыгодные отношения и будем рады видеть Вашу компанию в числе наших партнёров!',
    },
    'brands': {
        'title': 'Бренды',
        'subtitle': 'У нас вы можете приобрести продукцию следующих брендов',
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
    'request': {
        'title': 'Запрос',
        'subtitle': '',
    },
}

catalog_groups = [
        {
            'name': 'common',
            'caption': 'Общие каталоги',
            'items': 
            [
                {
                    'name': 'SKF',
                    'image': 'https://technobearing.ru/upload/iblock/2f3/commonSKF.jpg',
                    'link': 'https://technobearing.ru/d/877366/d/obshchiykatalogskf-min_1.pdf',
                },
                {
                    'name': 'NSK',
                    'image': 'https://technobearing.ru/upload/iblock/640/commonNSK.jpg',
                    'link': 'https://technobearing.ru/d/877366/d/obshchiykatalognsk.pdf',
                },
            ]
        },
        {
            'name': 'ball',
            'caption': 'Шариковые подшипники',
            'items': 
            [
                {
                    'name': 'SKF',
                    'img': '',
                    'link': '',
                },
            ]
        },
]


copyright = {
    'year': '© ' + str(datetime.now().year) + ', ',
    'name': 'TechTransInvest - Поставщик подшипников и элементов промышленных трансмиссий',
    'link': 'https://ttinv.ru/',
}


def index(request):
    benefits = Benefits.objects.all()
    products = Products.objects.all()
    deliveries = Delivery.objects.all()
    brands = Brands.objects.all()
    requisites = Requisites.objects.all()

    data = {
        'page': 'index',
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
        'brands': brands,
    }
    return render(request, 'business_card/index.html', context=data)


def catalogs(request):
    catalog_groups = CatalogGroups.objects.all()
    catalog = Catalog.objects.all()

    data = {
        'page': 'catalogs',
        'catalog_groups': catalog_groups,
        'title': 'ТехТрансИнвест',
        'logo': logo,
        'nav': nav,
        'copyright': copyright,  
    }
    return render(request, 'business_card/catalogs.html', context=data)


def page_not_found(request, exception):
    data = {
        'page': 'pnf',
        'title': 'Опс...',
        'nav': nav,
    }

    return render(request, 'business_card/page404.html', context=data)
