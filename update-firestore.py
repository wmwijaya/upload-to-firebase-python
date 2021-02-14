import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def connect_to_firebase():
    cred = credentials.Certificate(
        "/Users/wmwijaya/google-cloud-projects/firebase/cerita-jataka-firebase-adminsdk-ednt0-1fa3908970.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'cerita-jataka',
    })

    db = firestore.client()
    return db

def upload_to_firestore(db, jatakas):
    for jataka in jatakas:
        jataka_dev = db.collection(u'jataka_dev').document(jataka['title'])
        jataka_dev.set({
        'id': jataka['id'],
        'number': jataka['number'],
        'title': jataka['title'],
        'content': jataka['content'],
        'img_uri': jataka['img_uri'],
        'read_count': jataka['read_count'],
        'share_count': jataka['share_count'],
        'favorite': 0
        })
    print('finished uploading ', len(jatakas), ' jataka to firestore')

class update_firetore:
    db =  connect_to_firebase()
    docs = db.collection(u'jataka').stream()
    jatakas = list()

    for doc in docs:
        #print(f'{doc.id} => {doc.to_dict()}')
        jataka = doc.to_dict()
        jatakas.append(jataka)
        print(jataka['id'], jataka['title'], len(jatakas))

    upload_to_firestore(db, jatakas)