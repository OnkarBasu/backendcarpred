from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle



# Step 1: Set up the Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Step 2: Load both models
with open('C:/Users/abasu/OneDrive/Desktop/backend1/model_pipeline.pkl', 'rb') as f:
    car_model_pipeline = pickle.load(f)

with open('model_pipelinebike.pkl', 'rb') as f:
    bike_model_pipeline = pickle.load(f)

# Step 3: Car price prediction endpoint
@app.route('/predict-car', methods=['POST'])
def predict_car():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = car_model_pipeline.predict(input_df)[0]
    return jsonify({'predicted_price': round(prediction, 2)})

# Step 4: Bike price prediction endpoint
@app.route('/predict-bike', methods=['POST'])
def predict_bike():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = bike_model_pipeline.predict(input_df)[0]
    return jsonify({'predicted_price': round(prediction, 2)})

# Step 5: Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



