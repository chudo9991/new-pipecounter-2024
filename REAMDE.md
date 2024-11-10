Запуск проекта:

```
- docker compose up --build
```

В браузере по адресу localhost:8000 досутпен web-интерфейс
Swagger доcтсупен по адресу localhost:8000/docs

Если нужно повторить эксперимент - запусти run_to_train_model.ipynb. Желательно запускать на GPU.
Если хочешь локально - запускай training_model.py

Структура проекта:
- основной файл main.py
- tasks.py задача Celery на распознавание
- celery_app.py - настройки Celery

Модель, которая используется (YOLOv11) - yolov11n_pipes.pt

Характеристики модели в папке results