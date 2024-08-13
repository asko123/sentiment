import os
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Print the current working directory
print("Current working directory:", os.getcwd())

# Print the contents of the current working directory
print("Directory contents:", os.listdir(os.getcwd()))

# route() decorator tells Flask the entry points for the application
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict_fun():
    clf_path = '../workspace/WorkShop/LR_Pipeline.pickle'
    
    print("Classifier path:", clf_path)
    
    clf = pickle.load(open(clf_path, 'rb'))

    if request.method == 'POST':
        message = request.form['message']
        if not isinstance(message, str):
            return "Invalid input type. Expected a string.", 400
        
        data = [message]  # Ensure the message is a string and wrap it in a list
        print("Data to be transformed:", data)
        
        my_prediction = clf.predict(data)
        print("Prediction:", my_prediction)
    
    return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)