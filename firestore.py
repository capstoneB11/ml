from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin

from classes.CountingClass import Chickount

cred = credentials.Certificate("secrets/FirestoreServiceAccount.json")
app = firebase_admin.initialize_app(cred)

def UploadDataToFirestore(data,idRef, collection_name = 'yolo'):
    db = firestore.client()

    data = Chickount(idRef=idRef, imageData=data['image'], count=data['count'])
    doc_ref = db.collection(collection_name).add(data.to_dict())

    return doc_ref[1].id

def GetImageFromFirestore(idRef = None, collection_name = 'esp'):
    db = firestore.client()
    
    img = db.collection(collection_name).document(idRef).get().to_dict()['image']
    img_base64 = img.split(',')[1]

    return img_base64