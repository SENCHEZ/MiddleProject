# Что используем за сборку языка
FROM python:3.12-slim

WORKDIR /APP

# Устанавливаем системные зависимости
RUN apt-get update && apg-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/list/*

# Копируем все зависимости проекта
COPY requirements.txt

# Устанавливаем зависимости Python
RUN pip install --nocashe-dir -r requirements.txt

# Копируем сам проект
COPY src/app/src/

# Порт, на котором разворачиваем
EXPOSE 8000

# Команды запуска
CMD ['python','src/manage.py', 'runserver', '0.0.0.0:8000']