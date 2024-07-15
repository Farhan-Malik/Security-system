import cv2
import face_recognition
import imutils
import pickle
import time
from lock_control import unlock, lock
from distance_measurement import Distance
from telegramalert import send_alert_with_snapshot

TOLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'

# Returns (R, G, B) from name
def name_to_color(name):
    color = [(ord(c.lower()) - 97) * 8 for c in name[:3]]
    return color

vs = cv2.VideoCapture(0)
print("[INFO] starting video stream...")
known_faces, known_names = pickle.loads(open('face_encodings.pickle', "rb").read())
print('Processing...')

while True:
    try:
        dist = Distance()
        time.sleep(1)
    except KeyboardInterrupt:
        break
    print('Distance is {} cms'.format(dist))
    if dist < 150:
        tic = time.time()
        while True:
            ret, image = vs.read()
            if not ret:
                break

            locations = face_recognition.face_locations(image, model=MODEL)
            encodings = face_recognition.face_encodings(image, locations)

            print(f', found {len(encodings)} face(s)')

            for face_encoding, face_location in zip(encodings, locations):
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
                match = None
                if True in results:
                    match = known_names[results.index(True)]

                    if match == 'Farhan' or match == 'Aman':
                        unlock(26)
                        time.sleep(10)
                        lock(26)
                    else:
                        send_alert_with_snapshot(image)

                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])
                    color = name_to_color(match)

                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (200, 200, 200), FONT_THICKNESS)

            tok = time.time()

            cv2.imshow('Webcam', image)
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break

            if tok - tic > 20:
                cv2.destroyAllWindows()
                break

vs.release()
cv2.destroyAllWindows()
