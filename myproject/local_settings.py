import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

# DATABASES = {
# 	'default': {
# 		"ENGINE": "django.contrib.gis.db.backends.postgis",
# 	    "NAME": "taxi",
# 	    "PASSWORD": "cvthnm",
# 	    "USER": "postgres",
# 	    "HOST": "localhost",
# 	    "PORT": "5432"
# 	}
# }

