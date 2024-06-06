# Face-Recognition-Working
An implementation of the face recognition using Dlib and OpenCV 

# Once Cloaning this repository is done, then follow the following steps 
Firstly, add images to the validation folder for the custom problem solving. 
Once adding images are done, run the command "python rekognition.py". The code will atomatically train the model and will be accessing the webcame and display the recognition of the same in a different window. 


Face Recognition with OpenCV and Dlib

Table of Contents
Introduction
Features
Installation
Usage
Configuration
Examples
Contributing
License
Introduction
Face Recognition with OpenCV and Dlib is a Python-based project for recognizing faces in images and videos. This project utilizes the powerful libraries OpenCV and Dlib to detect and recognize faces with high accuracy.

Features
Real-time face detection and recognition
Support for image and video input
High accuracy with Dlib's pre-trained models
Easy to use and extend
Installation
Follow these steps to set up the project:

Clone the repository

bash
Copy code
git clone https://github.com/yourusername/face-recognition-opencv-dlib.git
cd face-recognition-opencv-dlib
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
Install dependencies

bash
Copy code
pip install -r requirements.txt
Download Dlib's pre-trained face recognition model

Download the model from this link
Extract the .bz2 file and place dlib_face_recognition_resnet_model_v1.dat in the models/ directory
Usage
Recognize Faces in an Image
bash
Copy code
python recognize_faces_image.py --image path/to/image.jpg
Recognize Faces in a Video
bash
Copy code
python recognize_faces_video.py --video path/to/video.mp4
Configuration
Models: The pre-trained models should be placed in the models/ directory.
Known Faces: Images of known faces should be stored in the known_faces/ directory. Each person's images should be in a subdirectory named after the person.
Examples
Recognize Faces in an Image
bash
Copy code
python recognize_faces_image.py --image sample.jpg
Sample output:

java
Copy code
Recognized: Person1 at (x1, y1, x2, y2)
Recognized: Person2 at (x1, y1, x2, y2)
Recognize Faces in a Video
bash
Copy code
python recognize_faces_video.py --video sample.mp4
Sample output:

makefile
Copy code
Recognized: Person1 at frame 10
Recognized: Person2 at frame 24
Contributing
We welcome contributions! Please read the contribution guidelines to get started.

License
This project is licensed under the MIT License - see the LICENSE file for details.


