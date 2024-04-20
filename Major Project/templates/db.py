
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\Sanskruti\\Desktop\\Major Project\\road-nivaaran-firebase-adminsdk-3np47-dd7cd67414.json")


firebase_admin.initialize_app(cred, {
    'storageBucket': 'road-nivaaran.appspot.com'
})

# Access Firebase Storage
bucket = storage.bucket()

# Specify the path to your image in Firebase Storage
blob = bucket.blob('/img/pothole.jpg')

# Download the image to a local file or memory buffer
image_data = blob.download_as_bytes()  # If you want to download the image as bytes
