import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd

def read_file():
    df = pd.read_csv('jataka-444-s3.csv', sep=';')
    return df

def connect_to_firebase():
    cred = credentials.Certificate("/Users/wmwijaya/google-cloud-projects/firebase/cerita-jataka-firebase-adminsdk-ednt0-1fa3908970.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'cerita-jataka',
    })

    db = firestore.client()
    return db

class jataka_firestore:
    db = connect_to_firebase()
    df = read_file()
    for index, row in df.iterrows():
        jataka = db.collection(u'jataka').document(row['title'])
        jataka.set({
            'id': row['_id'],
            'number': row['number'],
            'title' : row['title'],
            'content': row['content'],
            'img_uri': row['img_uri'],
            'read_count': 0,
            'share_count': 0
        })
        print(row['_id'])
    print('finished uploading jataka to firestore')