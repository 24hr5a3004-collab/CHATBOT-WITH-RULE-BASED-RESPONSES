import cv2
import face_recognition

# Load known image
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

known_face_names = ["Vinay"]

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame
    ret, frame = video_capture.read()

    # Convert BGR to RGB
    rgb_frame = frame[:, :, ::-1]

    # Find faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        # Compare face
        matches = face_recognition.compare_faces([known_encoding], face_encoding)

        name = "Unknown"

        if True in matches:
            name = known_face_names[0]

        # Draw rectangle
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display name
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 0), 2)

    # Show video
    cv2.imshow("Face Detection & Recognition", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
video_capture.release()
cv2.destroyAllWindows()