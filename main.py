from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Cargar el modelo entrenado
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Mapeo de clases (ID) a nombres de plantas
plant_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

# Ruta principal que muestra el HTML
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "predicted_name": None, "predicted_id": None})

# Ruta para procesar el formulario
@app.post("/predict/", response_class=HTMLResponse)
async def predict(
    request: Request,
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(data)
    predicted_id = int(prediction[0])
    predicted_name = plant_names[predicted_id]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "predicted_name": predicted_name,
        "predicted_id": predicted_id
    })
