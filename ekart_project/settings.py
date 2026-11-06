from pathlib import Path

# ==================================================
# BASE DIRECTORY
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# SECURITY
# ==================================================

SECRET_KEY = 'django-insecure-as(h4-02!f8w*0eejx*0hgo%-!&pemm!rt9%u2l$h#ijp#y*bs'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# ==================================================
# INSTALLED APPS
# ==================================================

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==================================================
# URL CONFIGURATION
# ==================================================

ROOT_URLCONF = 'ekart_project.urls'


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==================================================
# WSGI
# ==================================================

WSGI_APPLICATION = 'ekart_project.wsgi.application'


# ==================================================
# DATABASE
# ==================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==================================================
# PASSWORD VALIDATION
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==================================================
# LANGUAGE AND TIME
# ==================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ==================================================
# STATIC FILES
# ==================================================

STATIC_URL = 'static/'


# ==================================================
# DEFAULT PRIMARY KEY
# ==================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==================================================
# EMAIL CONFIGURATION
# ==================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ==================================================
# JAZZMIN SETTINGS
# ==================================================

JAZZMIN_SETTINGS = {
    "site_title": "Ekart Command Center",
    "site_header": "EKART",
    "site_brand": "EKART",
    "welcome_sign": "Welcome to the Future of Commerce",
    "copyright": "Ekart Technologies",

    "show_sidebar": True,
    "navigation_expanded": True,

    "topmenu_links": [
        {
            "name": "Dashboard",
            "url": "admin:index",
            "icon": "fas fa-home",
        },
        {
            "name": "View Website",
            "url": "/",
            "new_window": True,
        },
    ],

    "icons": {
        "auth": "fas fa-shield-alt",
        "auth.user": "fas fa-user-astronaut",
        "auth.group": "fas fa-users-cog",
    },

    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "related_modal_active": True,
}


# ==================================================
# JAZZMIN UI TWEAKS
# ==================================================

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,

    "brand_small_text": False,
    "brand_colour": "navbar-dark",

    "accent": "accent-info",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,

    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,

    "theme": "darkly",
    "dark_mode_theme": "darkly",

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "success": "btn-success",
        "warning": "btn-warning",
        "danger": "btn-danger",
    },

    "actions_sticky_top": True,
}


# ==================================================
# GLASSMORPHISM CUSTOM CSS
# ==================================================

JAZZMIN_SETTINGS["custom_css"] = (
    "data:text/css,"

    "body%7B"
    "background:linear-gradient(135deg,%23060918,%230f1b35,%23121c30)!important;"
    "color:%23eaf6ff!important;"
    "%7D"

    ".content-wrapper%7Bbackground:transparent!important;%7D"

    ".main-sidebar%7B"
    "background:rgba(10,18,35,0.88)!important;"
    "backdrop-filter:blur(25px)!important;"
    "-webkit-backdrop-filter:blur(25px)!important;"
    "border-right:1px solid rgba(255,255,255,0.12)!important;"
    "%7D"

    ".main-header%7B"
    "background:rgba(10,18,35,0.78)!important;"
    "backdrop-filter:blur(20px)!important;"
    "-webkit-backdrop-filter:blur(20px)!important;"
    "border-bottom:1px solid rgba(255,255,255,0.12)!important;"
    "%7D"

    ".card,.module,.info-box,.small-box%7B"
    "background:rgba(255,255,255,0.06)!important;"
    "backdrop-filter:blur(20px)!important;"
    "-webkit-backdrop-filter:blur(20px)!important;"
    "border:1px solid rgba(255,255,255,0.12)!important;"
    "border-radius:18px!important;"
    "box-shadow:0 8px 32px rgba(0,0,0,0.30)!important;"
    "%7D"

    ".content-header h1%7B"
    "color:%23ffffff!important;"
    "font-weight:700!important;"
    "letter-spacing:1px!important;"
    "%7D"

    ".btn-primary%7B"
    "background:linear-gradient(135deg,%2300d4ff,%230070ff)!important;"
    "border:0!important;"
    "border-radius:10px!important;"
    "box-shadow:0 0 18px rgba(0,212,255,0.25)!important;"
    "%7D"

    ".form-control%7B"
    "background:rgba(255,255,255,0.06)!important;"
    "border:1px solid rgba(255,255,255,0.15)!important;"
    "border-radius:10px!important;"
    "color:%23ffffff!important;"
    "%7D"

    ".table%7Bcolor:%23eaf6ff!important;%7D"

    ".table thead th%7B"
    "border-bottom:1px solid rgba(255,255,255,0.15)!important;"
    "color:%2300d4ff!important;"
    "%7D"

    ".table tbody tr:hover%7B"
    "background:rgba(0,212,255,0.07)!important;"
    "%7D"

    ".nav-sidebar .nav-link%7B"
    "border-radius:10px!important;"
    "margin:3px 8px!important;"
    "transition:all .3s ease!important;"
    "%7D"

    ".nav-sidebar .nav-link:hover%7B"
    "background:rgba(0,212,255,0.12)!important;"
    "color:%2300d4ff!important;"
    "box-shadow:0 0 12px rgba(0,212,255,0.08)!important;"
    "%7D"

    ".nav-sidebar .nav-link.active%7B"
    "background:linear-gradient(135deg,rgba(0,212,255,0.20),rgba(0,112,255,0.12))!important;"
    "border:1px solid rgba(0,212,255,0.25)!important;"
    "color:%2300d4ff!important;"
    "%7D"

    ".breadcrumb%7B"
    "background:rgba(255,255,255,0.04)!important;"
    "border-radius:10px!important;"
    "%7D"

    ".login-box .card%7B"
    "background:rgba(255,255,255,0.06)!important;"
    "backdrop-filter:blur(25px)!important;"
    "border:1px solid rgba(255,255,255,0.15)!important;"
    "border-radius:20px!important;"
    "%7D"

    "::-webkit-scrollbar%7Bwidth:8px;%7D"

    "::-webkit-scrollbar-track%7B"
    "background:%230b1120;"
    "%7D"

    "::-webkit-scrollbar-thumb%7B"
    "background:rgba(0,212,255,0.35);"
    "border-radius:10px;"
    "%7D"
)