# инициализация файлов
# Редактирование файла  с опредление окружения для 
# разработки продакшена и тестировки

# cat > src/config/settings/__init__.py << 'EOF'
import os
# Опрделяем окружение 
environment = os.environ.get('DJANGO_ENV',"development")

if environment == "production":
    from .production import *
elif environment == 'testing':
    from .testing import *
else:
    from .development import *



