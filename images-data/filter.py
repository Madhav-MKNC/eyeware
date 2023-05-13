# # filter the valid images for data set

# import cv2

# # Load the cascades
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


# def filter(input):
#     # Load the image
#     img = cv2.imread(input)

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Detect
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
#     eyewears = face_cascade.detectMultiScale(gray, 1.3, 5)

#     # Iterate over each detected face
#     pos = False
#     for (x, y, w, h) in faces:
#         # Draw a rectangle around the face
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
#         # Crop the region of interest containing the face
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
        
#         # Detect eyes within the region of interest
#         eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)
#         eyes = eye_cascade.detectMultiScale(roi_gray)

#         # If both eyes are detected, then the person is wearing eye wear
#         if len(eyes) == 2:
#             for (ex,ey,ew,eh) in eyes:
#                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#             cv2.putText(img, "Wearing eye wear", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             pos = True
#         # Otherwise, the person is not wearing eye wear
#         else:
#             pos = False
#             cv2.putText(img, "Not wearing eye wear", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    
#     cv2.imwrite('output.jpg', img)
#     # If no faces with two eyes are detected, then eyewear is not detected
#     return pos

# x = filter('image2.jpg')
# print("Valid" if x else "Not Valid")






import cv2

# Load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect_eyewear(input):
    img = cv2.imread(input)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    results = []
    # Iterate over each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Crop the region of interest containing the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detect eyes within the region of interest
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)

        # Check if eyewear is detected
        if len(eyes) == 2:
            eyewear_detected = True
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.putText(img, "Eyewear detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            eyewear_detected = False
            cv2.putText(img, "Eyewear not detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imwrite('output.jpg', img)
    return eyewear_detected


x = detect_eyewear("image2.jpg")
print(x)
