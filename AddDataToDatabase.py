import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facerecognitionattendancesystm-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2101031000075" :
        {
            "name" : "Harsh Joshi",
            "major" : "Info. Tech.",
            "starting_year" : 2021,
            "total_attendance" : 6,
            "standing" : "A+",
            "year" : 4,
            "last_attendance_time" : "2024-11-07 12:42:26"

        },
    "2101031000106" :
        {
            "name" : "Pankaj Manvani",
            "major" : "Info. Tech.",
            "starting_year" : 2021,
            "total_attendance" : 6,
            "standing" : "E",
            "year" : 4,
            "last_attendance_time" : "2024-11-07 12:42:26"

        },
    "601" :
        {
            "name" : "Sagar Darshan",
            "major" : "Info. Tech.",
            "starting_year" : 2021,
            "total_attendance" : 6,
            "standing" : "O",
            "year" : 3,
            "last_attendance_time" : "2024-11-07 12:42:26"

        },
}
for key,value in data.items():
    ref.child(key).set(value)