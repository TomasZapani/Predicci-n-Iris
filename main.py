from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from model_training import model

app = FastAPI()

with open('model.pkl','rb') as f:
    model = pickle.load(f)



class IrisReq(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_lentgh: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a mi API de Machine Learning con FastAPI!"}

@app.get("/predict/")
def predict_get(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    import numpy as np
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(data)
    predicted_class = int(prediction[0])
    return {"predicted_class": predicted_class}
