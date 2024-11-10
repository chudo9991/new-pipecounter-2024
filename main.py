from fastapi import FastAPI, File, UploadFile, Request  # , Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse

from tasks import process_image_task
import base64
# import io

app = FastAPI()
app.mount("/static/", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    """
    Renders the main page where users can upload images for object detection.

    Args:
        request (Request): The HTTP request object.

    Returns:
        TemplateResponse: An HTML response with the rendered upload page.
    """
    # Главная страница с загрузкой изображения
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/upload/")
async def upload_image(image: UploadFile = File(...)):
    """
    Processes an uploaded image using the YOLO model and returns the result as
    a JSON response.

    Args:
        image (UploadFile): The uploaded image file.

    Returns:
        JSONResponse: A JSON response with the number of objects detected and
            the annotated image as a base64-encoded string.
    """
    image_bytes = await image.read()

    # Отправка задачи на обработку изображения
    result = process_image_task(image_bytes)

    if result["image"] is not None:
        # Кодирование изображения в base64 для передачи в JSON
        encoded_image = base64.b64encode(result["image"]).decode('utf-8')

        return JSONResponse({
            "num_objects": result["num_objects"],
            "image": encoded_image
        })
    else:
        return JSONResponse({"error": "Failed to process image"}, status_code=500)
