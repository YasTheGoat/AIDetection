import os
import facedetection
import car_pedestrians_detection

imageName = ""
videoName = ""

def invalid():
    print("This mode does not exist")
    key = str(input("Press R to restart the app....\n"))
    if key.lower() == "r":
        os.system('python main.py')

print("\n AVAILABLE MODES: \n")
print("---------------FACE DETECTION(1)---------------")
print("----------------CAR DETECTION(2)---------------")

mode = str(input("Mode: "))
if mode == "1":
    pass
elif mode == "2":
    pass
else:
    invalid()


print("\n AVAILABLE TYPES: \n")
print("---------------WEBCAM(1)-------------------")
print("----------------IMAGE(2)-------------------")
print("----------------VIDEO(3)-------------------")

type_ = str(input("Type: "))

if type_ == "1":
    pass
elif type_ == "2":
    imageName = str(input("Name of the image: "))
elif type_ == "3":
    videoName = str(input("Name of the video: "))
else:
    invalid()

print("Program Loading....")
if mode == "1":
    facedetection.run(type_, imageName, videoName)
elif mode == "2":
    car_pedestrians_detection.run(type_, imageName, videoName)


print("Code Completed")