import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'project-flask-326916'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
  'projectId': project_id,
})

db = firestore.client()

# print(db)


def get_users():
    return db.collection('users').get()

def get_user(user_id):
  return db.collection('users').document(user_id).get()

def get_todos(user_id):
  return db.collection('users').document(user_id).collection('todos').get()