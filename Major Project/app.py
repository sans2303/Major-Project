# app_with_yolo.py
from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image
import requests

app = Flask(__name__)

def predict_defect(image_path):
    # Load the YOLOv5 model
    model = YOLO(r'Myproject-main\Myproject-main\YoloModel-20240306T045132Z-001\YoloModel\runs\classify\train3\weights\best.pt')

    # Read and resize the input image using Pillow (PIL)
    with Image.open(image_path) as img:
        img = img.resize((255, 255))
    
    # Convert image data to a list
    
    
    # Perform prediction on the image
    results = model(img, show=True)

    # Extract relevant information from the prediction
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    prediction = names_dict[probs.index(max(probs))]

    return prediction

# def send_complaint(image_path, prediction, latitude, longitude):
#     # Dummy URL for government website
#     government_url = 'http://127.0.0.1:5000/'

#     # Prepare complaint data
#     complaint_data = {
#         'image': open(image_path, 'rb'),
#         'prediction': prediction,
#         'latitude': latitude,
#         'longitude': longitude
#     }

#     # Send POST request to government website
#     response = requests.post(government_url, files=complaint_data)

#     # Check if request was successful
#     if response.status_code == 200:
#         return True
#     else:
#         return False

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']

    # Save the file temporarily (optional)
    image_path = 'temp_image.jpg'
    file.save(image_path)
    # Pass the image to the YOLOv5 model for prediction
    prediction = predict_defect(image_path)

    # Render the template with the prediction result
    return render_template('index.html', prediction=prediction)


    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    

    # success = send_complaint(image_path, prediction, latitude, longitude)

    # if success:
    #     return render_template('success.html')  # Render success page
    # else:
    #     return render_template('error.html')    # Render error page

if __name__ == '__main__':
    app.run(debug=True)