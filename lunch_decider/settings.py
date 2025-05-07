DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.{}'.format(
             os.getenv('DATABASE_ENGINE', 'postgres')
         ),
         'NAME': os.getenv('DATABASE_NAME', 'lunch_db'),
         'USER': os.getenv('DATABASE_USERNAME', 'user'),
         'PASSWORD': os.getenv('DATABASE_PASSWORD', '1234'),
         'HOST': os.getenv('DATABASE_HOST', 'postgres'),
         'PORT': os.getenv('DATABASE_PORT', 5432),
     }
 }
