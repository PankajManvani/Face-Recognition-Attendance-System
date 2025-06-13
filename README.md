Face Recognition Attendance System
A real-time face recognition-based attendance system built with Python, OpenCV, and Firebase. This system automatically identifies students through their faces and records their attendance with a user-friendly interface.
Features

Real-time Face Recognition: Uses advanced face recognition algorithms to identify students
Firebase Integration: Cloud-based data storage for student information and attendance records
Automatic Attendance Tracking: Records attendance with timestamps
Duplicate Prevention: Prevents duplicate attendance entries within 30 seconds
Interactive UI: Clean graphical interface showing student information and photos
Cloud Storage: Student photos stored in Firebase Storage
Multi-mode Display: Different display modes for various system states

System Requirements
Hardware

Webcam or camera device
Computer with Python support

Software Dependencies
opencv-python
face-recognition
firebase-admin
cvzone
numpy
pickle
Installation

Clone the repository
bashgit clone <your-repository-url>
cd face-recognition-attendance-system

Install required packages
bashpip install opencv-python
pip install face-recognition
pip install firebase-admin
pip install cvzone
pip install numpy

Set up Firebase

Create a Firebase project at Firebase Console
Enable Realtime Database and Storage
Download the service account key as serviceAccountKey.json
Place the service account key in the project root directory


Create project structure
project/
├── main.py
├── AddDataToDatabase.py
├── encodeGenerator.py
├── serviceAccountKey.json
├── Images/
│   ├── student_id1.png
│   ├── student_id2.png
│   └── ...
├── Resources/
│   ├── background.png
│   └── Modes/
│       ├── 1.png
│       ├── 2.png
│       ├── 3.png
│       └── 4.png
└── EncodeFile.p (generated)


Configuration
Firebase Setup

Update the Firebase configuration in all Python files:
pythonfirebase_admin.initialize_app(cred, {
    'databaseURL': "your-database-url",
    'storageBucket': "your-storage-bucket"
})


Student Database Structure
The system expects student data in the following format:
json{
  "student_id": {
    "name": "Student Name",
    "major": "Major/Department",
    "starting_year": 2021,
    "total_attendance": 0,
    "standing": "A+",
    "year": 4,
    "last_attendance_time": "2024-11-07 12:42:26"
  }
}
Usage
1. Add Student Data
First, add student information to the database:
bashpython AddDataToDatabase.py
2. Generate Face Encodings
Process student images and generate face encodings:
bashpython encodeGenerator.py

Place student photos in the Images/ folder
Name files with student IDs (e.g., 2101031000075.png)
This script uploads images to Firebase Storage and creates EncodeFile.p

3. Run the Attendance System
Start the main attendance system:
bashpython main.py
How It Works

Face Detection: The system continuously captures frames from the webcam
Face Recognition: Detected faces are compared against stored encodings
Student Identification: When a match is found, student information is retrieved from Firebase
Attendance Recording: If more than 30 seconds have passed since last attendance, a new record is created
UI Updates: The interface displays student information, photo, and attendance count

File Descriptions

main.py: Main application file that runs the attendance system
AddDataToDatabase.py: Adds student data to Firebase Realtime Database
encodeGenerator.py: Processes student images and generates face encodings
serviceAccountKey.json: Firebase service account credentials (not included in repo)
Images/: Directory containing student photos
Resources/: UI assets including background and mode images
EncodeFile.p: Pickled file containing face encodings and student IDs

Display Modes
The system has different display modes:

Mode 0: Default/waiting state
Mode 1: Loading student information
Mode 2: Displaying student details
Mode 3: Already marked (duplicate prevention)

Security Features

Duplicate Prevention: Prevents multiple attendance entries within 30 seconds
Face Distance Verification: Uses face distance algorithms for accurate recognition
Secure Cloud Storage: Student data stored securely in Firebase

Troubleshooting
Common Issues

Camera not detected

Check camera permissions
Verify camera index in cv2.VideoCapture(0)


Firebase connection errors

Verify serviceAccountKey.json is correct
Check Firebase project settings and permissions


Face recognition not working

Ensure good lighting conditions
Check if EncodeFile.p exists and is up to date
Verify student images are clear and properly named


Missing dependencies

Install all required packages
Some systems may need additional setup for face_recognition library



Performance Tips

Use well-lit environments for better face detection
Ensure student photos are clear and front-facing
Consider image quality and resolution for better accuracy
Regular database cleanup for optimal performance

Contributing

Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request

License
This project is open source. Please check the license file for more details.
Support
For issues and questions:

Check the troubleshooting section
Review Firebase documentation
Ensure all dependencies are properly installed

Acknowledgments

OpenCV for computer vision capabilities
Firebase for cloud services
face_recognition library for facial recognition algorithms
cvzone for additional computer vision utilities
