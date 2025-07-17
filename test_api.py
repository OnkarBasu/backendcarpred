import requests

# Sample data matching the model's expected input
sample_data = {
    "km_driven": 120000,
    "fuel": "Diesel",
    "seller_type": "Individual",
    "transmission": "Manual",
    "owner": "First Owner",
    "mileage": 23.4,
    "engine": 1248.0,
    "seats": 5.0,
    "Company": "Maruti",
    "name3": "Swift Dzire",
    "car_age": 11
}

response = requests.post("http://127.0.0.1:5000/predict", json=sample_data)
print("Status code:", response.status_code)
print("Response:", response.json()) 