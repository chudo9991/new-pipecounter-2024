from celery import Celery

# Настройка брокера Redis
celery_app = Celery(
    "tasks",
    # Замените на свой адрес Redis, если необходимо
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
