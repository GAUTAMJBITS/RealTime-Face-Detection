import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionrealtime-6b3d4-default-rtdb.firebaseio.com"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Suman Kumar",
            "major": "CS",
            "Starting Year": 2020,
            "total_attendance": 8,
            "standing": 6,
            "year": 4,
            "last_attendance_time": '2020-12-11 00:54:34',
        },
    "321655":
        {
            "name": "Harman Kaur",
            "major": "CS",
            "Starting Year": 2020,
            "total_attendance": 8,
            "standing": 6,
            "year": 4,
            "last_attendance_time": '2020-12-11 00:54:34',
        },

    "963852":
        {
            "name": "Elon Musk",
            "major": "Rocket Propulsion",
            "Starting Year": 2000,
            "total_attendance": 9,
            "standing": 6,
            "year": 4,
            "last_attendance_time": '2020-12-2 00:54:34',
        },

    "852741":
        {
            "name": "Emily Blunt",
            "major": "Modelling/ Acting",
            "Starting Year": 2008,
            "total_attendance": 10,
            "standing": 8,
            "year": 3,
            "last_attendance_time": '2020-12-11 20:54:34',
        },
    "321653":
        {
            "name": "SUMMY SINGH",
            "major": "CSE",
            "Starting Year": 2020,
            "total_attendance": 9,
            "standing": 8,
            "year": 3,
            "last_attendance_time": '2020-12-11 20:54:34',
        }

    }

for key,value in data.items():
    ref.child(key).set(value)

    

