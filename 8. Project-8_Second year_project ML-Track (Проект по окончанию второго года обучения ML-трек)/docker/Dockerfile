# Задаём базовый образ
FROM python:3.11.11
# Задаём рабочую директорию контейнера
WORKDIR /usr/src/app
# Копируем содержимое папки flask_app в рабочую директорию контейнера
COPY flask_app ./
# Копируем файл requirements.txt в рабочую директорию контейнера
COPY requirements.txt ./
# Создаем папку static и копируем туда модель и изображения
RUN mkdir -p /usr/src/app/static/model && \
    mkdir -p /usr/src/app/static/images

COPY static/model /usr/src/app/static/model
COPY static/images /usr/src/app/static/images
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
# Исполняем команду для запуска скрипта
CMD ["python", "./app.py"]