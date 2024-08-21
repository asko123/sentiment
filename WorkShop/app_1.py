import os
import pickle
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request

app = FastAPI()

# Print the current working directory
print("Current working directory:", os.getcwd())

# Print the contents of the current working directory
print("Directory contents:", os.listdir(os.getcwd()))

# Load the classifier
clf_path = 'LR_Pipeline.pickle'
print("Classifier path:", clf_path)
clf = pickle.load(open(clf_path, 'rb'))

@app.get("/", response_class=JSONResponse)
async def home():
    return {"message": "Welcome to the prediction API. Use the /predict endpoint to get predictions."}

@app.post("/predict", response_class=JSONResponse)
async def predict_fun(request: Request, message: str = Form(...)):
    if not isinstance(message, str):
        raise HTTPException(status_code=400, detail="Invalid input type. Expected a string.")
    
    data = [message]  # Ensure the message is a string and wrap it in a list
    print("Data to be transformed:", data)
    
    my_prediction = clf.predict(data)
    print("Prediction:", my_prediction)
    
    return {"prediction": my_prediction.tolist()}  # Convert prediction to list for JSON serialization

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    #uvicorn app_1:app --reload