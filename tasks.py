from ultralytics import YOLO
from PIL import Image
import io
from celery_app import celery_app

# Загружаем модель YOLO
model = YOLO("yolov11n_pipes.pt")


@celery_app.task
def process_image_task(image_bytes):
    """
    Task to process an image and detect objects using YOLO.

    Accepts:
        image_bytes (bytes): The image data as a bytes object.

    Returns:
        A dictionary with two key-value pairs:
            image (bytes): The annotated image data as a bytes object.
            num_objects (int): The number of objects detected in the image.

    Raises:
        Any exception raised during the image processing.
    """
    try:
        # Преобразование байтов в изображение PIL
        pil_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Обработка изображения моделью YOLO
        results = model(pil_image)
        num_objects = len(results[0].boxes)
        print(f"Detected {num_objects} objects")

        # Рендеринг изображения с аннотациями
        annotated_image = results[0].plot()

        # Преобразование цветовых каналов из BGR в RGB
        annotated_image = Image.fromarray(annotated_image[..., ::-1])

        # Кодирование изображения для отправки в ответ
        buffer = io.BytesIO()
        annotated_image.save(buffer, format='JPEG')
        response_image = buffer.getvalue()

        return {"image": response_image, "num_objects": num_objects}
    except Exception as e:
        print(f"Error processing image: {e}")
        return {"image": None, "num_objects": 0}
