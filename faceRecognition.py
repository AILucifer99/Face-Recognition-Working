import cv2
import numpy as np
import face_recognition
import os
import warnings
from tqdm import tqdm


class FaceRecognition :
    def __init__(self, images_path, swap_color_channels, 
                capturing_device, display_video_window_dimension, 
                image_scaling_constant, 
                face_recognition_tolerance_threshold, video_stream_window_name) :
                
        super(FaceRecognition, self).__init__()

        self.images_path = images_path
        self.swap_color_channels = swap_color_channels
        self.capturing_device = capturing_device
        self.display_video_window_dimension = display_video_window_dimension
        self.image_scaling_constant = image_scaling_constant
        self.face_recognition_tolerance_threshold = face_recognition_tolerance_threshold
        self.video_stream_window_name = video_stream_window_name

    def Recognize(self) :
        validationPath = self.images_path
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
                    image = cv2.cvtColor(
                        image, cv2.COLOR_BGR2RGB if self.swap_color_channels else cv2.COLOR_BGR2HSV
                        )
                    faceEncoding = face_recognition.face_encodings(image)[0]
                    encodingList.append(faceEncoding)
                return encodingList
            

        validationImageEncodingList = faceEncodingFinder(parse=True, imageListObject=imagesList)
        print("There were {} face encodings founded.{}Encoding Completed Successfully.".format(len(validationImageEncodingList), "\n"))


        # Initializing the WebCamera
        cap = cv2.VideoCapture(self.capturing_device)
        video_feed_dimension = self.display_video_window_dimension

        # For RTSP Link just paste it here
        rtspLink = ""

        try :
            while True :
                warnings.filterwarnings('ignore')
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, video_feed_dimension[0])
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, video_feed_dimension[1])

                success, img = cap.read()  
                imageS = cv2.resize(img, (0, 0), None, 
                                        self.image_scaling_constant, 
                                        self.image_scaling_constant)

                imageS = cv2.cvtColor(imageS, cv2.COLOR_BGR2RGB)

                # Encoding Calculation of the WebCamera
                facesCurFrame = face_recognition.face_locations(imageS)
                encodesCurFrame = face_recognition.face_encodings(imageS, facesCurFrame)

                for encodeFace, faceLocation in zip(encodesCurFrame, facesCurFrame) :
                    matches = face_recognition.compare_faces(known_face_encodings=validationImageEncodingList, 
                                                            face_encoding_to_check=encodeFace, 
                                                            tolerance=self.face_recognition_tolerance_threshold)
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


                cv2.imshow(self.video_stream_window_name, img)

                if cv2.waitKey(1) & 0xFF == ord('q') :
                    break
                else :
                    continue

        except KeyboardInterrupt :
            print("Code Exited -1")

        cap.release()
        cv2.destroyAllWindows()


