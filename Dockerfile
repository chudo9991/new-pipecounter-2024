# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем зависимости для OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev

# Устанавливаем зависимости проекта
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Экспортируем порт
EXPOSE 8000
