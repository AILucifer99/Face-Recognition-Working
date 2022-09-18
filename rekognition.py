import cv2
import numpy as np
import face_recognition
import os
from tqdm import tqdm


validationPath = "Validation"
imagesList = [] 
classNames = []
myImageList = os.listdir(validationPath)

print("The Validation images that were found are {}{}".format(myImageList, "\n"))

print("Reading Images, please wait....")

for className in tqdm(myImageList):
    currentImage = cv2.imread("{}/{}".format(validationPath, className))
    imagesList.append(currentImage)
    classNames.append(os.path.splitext(className)[0])

print("The class names of the images are {}".format(classNames))


def faceEncodingFinder(parse, imageListObject) :
    if parse :
        encodingList = []
        print("Face Encoding is ongoing....")
        for image in tqdm(imageListObject) :
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            faceEncoding = face_recognition.face_encodings(image)[0]
            encodingList.append(faceEncoding)
        return encodingList
    

validationImageEncodingList = faceEncodingFinder(parse=True, imageListObject=imagesList)
print("There were {} face encodings founded.{}Encoding Completed Successfully.".format(len(validationImageEncodingList), "\n"))


# Initializing the WebCamera
cap = cv2.VideoCapture(0)

# For RTSP Link just paste it here
rtspLink = ""

try :
    while True :
        success, img = cap.read()  
        imageS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imageS = cv2.cvtColor(imageS, cv2.COLOR_BGR2RGB)

        # Encoding Calculation of the WebCamera
        facesCurFrame = face_recognition.face_locations(imageS)
        encodesCurFrame = face_recognition.face_encodings(imageS, facesCurFrame)

        for encodeFace, faceLocation in zip(encodesCurFrame, facesCurFrame) :
            matches = face_recognition.compare_faces(known_face_encodings=validationImageEncodingList, 
                                                    face_encoding_to_check=encodeFace, 
                                                    tolerance=0.6)
            faceDistance = face_recognition.face_distance(face_encodings=validationImageEncodingList, 
                                                        face_to_compare=encodeFace)
            print(faceDistance)

            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex] :
                name = classNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4 

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 3)


        cv2.imshow("Webcame Stream", img)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
        else :
            continue

except KeyboardInterrupt :
    print("Code Exited -1")


cap.release()
cv2.destroyAllWindows()


