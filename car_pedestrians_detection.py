from time import sleep
import sys
import cv2

def run(type_, imageName, videoName):
    #load pretrained data
    trained_face_data = cv2.CascadeClassifier("./haarcascade/cars.xml")
    trained_pedestrians_data = cv2.CascadeClassifier("./haarcascade/haarcascade_fullbody.xml")

    #capture video from webcam
    webcam = cv2.VideoCapture(0)
    img = cv2.imread("./image/cars _and_pedestrians/" + imageName)
    video = cv2.VideoCapture("./video/" + videoName)

    sleep(3)

    print("Program Starting")
    print("To close the program press Q")

    if type_ == "1":


        while True:
            successful_frame_read, frame = webcam.read()

            #make the image gray
            grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


            #detect cars ans peoples
            car_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
            pedestrian_coordinates = trained_pedestrians_data.detectMultiScale(grayscaled_img)
            #print(face_coordinates)

            #draw rectangles around the cars and peoples
            for(x, y, w, h) in car_coordinates:
                cv2.rectangle(frame, (x, y), (w+x, h+y), (0, 255, 0), 3)
            for(x, y, w, h) in pedestrian_coordinates:
                cv2.rectangle(frame, (x, y), (w+x, h+y), (0, 255, 0), 3)

            # #show the image
            cv2.imshow('Car and Pedestrians detection', frame)
            key = cv2.waitKey(1)
            
            #####Stop Q is pressed
            if key == 81 or key == 113:
                break
    
        #Release the video capture object
        webcam.release()
    elif type_ == "2":
        #make the image gray
            grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #detect cars ans peoples
            car_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
            pedestrian_coordinates = trained_pedestrians_data.detectMultiScale(grayscaled_img)
            #print(face_coordinates)

            #draw rectangles around the cars and peoples
            for(x, y, w, h) in car_coordinates:
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 3)
            for(x, y, w, h) in pedestrian_coordinates:
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 3)

            # #show the image
            cv2.imshow('Frontal face image', img)
            key = cv2.waitKey()
            
            #####Stop Q is pressed
            if key == 81 or key == 113:
                sys.exit()
    else:
        while True:
            successful_frame_read, frame = video.read()

            #make the image gray
            grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


            #detect cars ans peoples
            car_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
            pedestrian_coordinates = trained_pedestrians_data.detectMultiScale(grayscaled_img)
            #print(face_coordinates)

            #draw rectangles around the cars and peoples
            for(x, y, w, h) in car_coordinates:
                cv2.rectangle(frame, (x, y), (w+x, h+y), (0, 255, 0), 3)
            for(x, y, w, h) in pedestrian_coordinates:
                cv2.rectangle(frame, (x, y), (w+x, h+y), (0, 255, 0), 3)

            # #show the image
            cv2.imshow('Car and Pedestrians detection', frame)
            key = cv2.waitKey(1)
            
            #####Stop Q is pressed
            if key == 81 or key == 113:
                break
