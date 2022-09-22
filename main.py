from faceRecognition import FaceRecognition

images_path = "./Validation"
swap_color = True
device_id = 0 
display_dimension = [1175, 875]
image_scale_const = 0.25
recognition_tolerance = 0.60 
video_stream = "Webcam Face Recognition"


if __name__ == '__main__' :

    face_recognition = FaceRecognition(images_path, swap_color, device_id, 
                                        display_dimension, image_scale_const, 
                                        recognition_tolerance, video_stream)
    
    face_recognition.Recognize()


