import cv2
import shutil
import os
import time
import keyboard

import tomtom
import watson_api
import location
import whatsapp

count = 0
run = True
pathOut='C:/Users/rrohi/OneDrive/Documents/Frames'
urlMain = 'https://www.google.com/maps/dir/?api=1&destination='
myCoords = (12.892122, 77.565379)

#Gets coordinates of closest hospital, using the tomtom api, which
#is used to find ETA between any two coordinates, and location which stores a dictionary of all hospitals

def getLocation():
    global myCoords
    coords = ()
    eta_min = 100000000000
    for place in location.d.keys():
        eta = tomtom.get_ETA(myCoords, location.d[place])
        if eta <= eta_min:
            eta_min = eta
            coords = location.d[place][0], location.d[place][1]
    return coords


#Starts webcam

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

#Creates a new folder. If the folder already exists it deletes it and creates a new one in its place

try:
    os.mkdir(pathOut)
except:
    shutil.rmtree(pathOut)
    os.mkdir(pathOut)

# Main loop

while run:  

    # A frame from the webcam video is saved in the folder created 
    
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    if ret == True:
        print('Read %d frame: ' % count, ret)
        cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)

        # The newly created is sent to the watson api to get a result
        # if it is an accident, a google maps link to the accident location is generated and sent to
        # the phone number of the hospital
        
        if watson_api.watson(pathOut+'/frame{:d}.jpg'.format(count)):
            destCoords = getLocation()
            string_coords = str(destCoords[0]) + ',' + str(destCoords[1])
            string_coords = urlMain + string_coords
            print(string_coords)
            whatsapp.send_message(string_coords)
        count += 1

    # there is a time gap of 5 seconds between every frame that is saved
    # during these 5 seconds we can pressed 'q' to quit the program 
    
    t_end = time.time()+5
    while time.time() < t_end:
        if keyboard.is_pressed('q'):
            print('Quitting...')
            run = False
            cap.release()
            cv2.destroyAllWindows()
            break
