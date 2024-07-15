
import cv2
import face_recognition
import imutils
import pickle
import time
from lock_control import unlock, lock
from distance_measurement import Distance

TOLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'

# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value range is 97 to 122, subtract 97, multiply by 8
    color = [(ord(c.lower()) - 97) * 8 for c in name[:3]]
    return color

# Open the webcam
vs = cv2.VideoCapture(0)
# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = cv2.VideoCapture(src=0).start()
#vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
#fps = FPS().start()
print("[INFO] loading encodings + face detector...")
known_faces, known_names = pickle.loads(open('face_encodings.pickle', "rb").read())
print('Processing...')

while True:
    try:
        # Using ultrasonic distance sensor to measure the distance of the object
        dist = Distance()
        time.sleep(1)
        # Whenever you press ctrl+c script stops running
    except KeyboardInterrupt:
        break
    print('Distance is {} cms'.format(dist))
    if dist < 150:
        tic = time.time()
        while True:
            # Capture a frame from the webcam
            ret, image = vs.read()
            if not ret:
                break

            #image = imutils.resize(image, width=416)
            # This time we first grab face locations - we'll need them to draw boxes
            locations = face_recognition.face_locations(image, model=MODEL)

            # Now since we know locations, we can pass them to face_encodings as the second argument
            # Without that, it will search for faces once again slowing down the whole process
            encodings = face_recognition.face_encodings(image, locations)

            # We passed our image through face_locations and face_encodings, so we can modify it
            # But this time we assume that there might be more faces in an image - we can find faces of different people
            print(f', found {len(encodings)} face(s)')

            for face_encoding, face_location in zip(encodings, locations):
                # We use compare_faces (but might use face_distance as well)
                # Returns an array of True/False values in order of passed known_faces
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

                # Since the order is being preserved, we check if any face was found then grab index
                # then label (name) of the first matching known face within a tolerance
                match = None
                if True in results:  # If at least one is true, get the name of the first of found labels
                    match = known_names[results.index(True)]

                    if match == 'Farhan' or match == 'Aman':  # In your case, use your name
                        '''
                        Here we are using a solenoid lock to lock-unlock the door,
                        The lock is connected with a relay module, and the relay module is set on pin 26 (BCM mode) of Pi.
                        '''
                        unlock(26)
                        time.sleep(10)  # Lock will remain open for 10 seconds.
                        lock(26)

                    # Each location contains positions in order: top, right, bottom, left
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    # Get color by name using our fancy function
                    color = name_to_color(match)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    # Now we need a smaller, filled frame below for a name
                    # This time we use the bottom in both corners - to start from the bottom and move 50 pixels down
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                    # Write a name
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (200, 200, 200), FONT_THICKNESS)

            tok = time.time()

            # Show image
            cv2.imshow('Webcam', image)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break

            # The camera will only remain open for 20 seconds
            if tok - tic > 20:
                cv2.destroyAllWindows()
                break

# Release the webcam
vs.release()
cv2.destroyAllWindows()
