import firebase_admin
from firebase_admin import credentials, firestore, storage

# serviceAccountKey.json கோப்பிற்கான பாதை
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-project-id.appspot.com'
})

db = firestore.client()

# டேட்டாவைச் சேமிக்க
def save_data(collection, doc_id, data):
    db.collection(collection).document(doc_id).set(data)
    print("சேமிக்கப்பட்டது.")

bucket = storage.bucket()

# கோப்பைப் பதிவேற்ற
def upload_file(file_path, destination_name):
    blob = bucket.blob(destination_name)
    blob.upload_from_filename(file_path)
    print("கோப்பு பதிவேற்றப்பட்டது.")
    
