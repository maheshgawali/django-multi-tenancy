DATABASES = {
    'default': {
        'ENGINE': 'django_mt.mt_core.mysql',
        'NAME': 'djangothon',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3307,
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
    },
    # 'db1': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'user1.app.com',
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'HOST': '127.0.0.1',
    #     'PORT': 3308,
    #     'OPTIONS': {
    #         'charset': 'utf8mb4'
    #     },
    # },
    # 'db2': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'user2.app.com',
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'HOST': '127.0.0.1',
    #     'PORT': 3309,
    #     'OPTIONS': {
    #         'charset': 'utf8mb4'
    #     },
    # }
}
