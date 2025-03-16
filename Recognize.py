import datetime
import os
import time
import csv
import cv2
import pandas as pd

def recognize_attendence():
    # Load the recognizer and cascade classifier
    recognizer = cv2.face.LBPHFaceRecognizer.create()
    recognizer.read("TrainingImageLabel" + os.sep + "Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier("D:\\work\\FRAS\\FRAS\\haarcascade_frontalface_default (1).xml")

    # Read student details CSV
    csv_path = "StudentDetails" + os.sep + "StudentDetails.csv"
    if not os.path.exists(csv_path):
        print("⚠️ Error: StudentDetails.csv not found!")
        return

    df = pd.read_csv(csv_path)
    
    # Fix column name issues
    df.columns = df.columns.str.strip()
    
    # Ensure 'Id' column exists
    if "Id" not in df.columns:
        print("⚠️ Error: 'Id' column missing in CSV!")
        return

    df['Id'] = df['Id'].astype(str)  # Convert Id column to string

    # Initialize attendance DataFrame
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    
    # Start video capture
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')  # ✅ Fixed format
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                # Get Name from CSV
                name = df.loc[df['Id'] == str(Id), 'Name'].values
                if len(name) > 0:
                    name = name[0]  # Extract name from array
                else:
                    name = "Unknown"

                tt = f"{Id}-{name}"
                attendance.loc[len(attendance)] = [Id, name, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)

            if conf > 75:
                unknown_dir = "ImagesUnknown"
                if not os.path.exists(unknown_dir):
                    os.makedirs(unknown_dir)

                noOfFile = len(os.listdir(unknown_dir)) + 1
                cv2.imwrite(unknown_dir + os.sep + f"Image{noOfFile}.jpg", im[y:y+h, x:x+w])

            cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', im)

        if cv2.waitKey(1) == ord('q'):
            break

    # Save attendance
    attendance_dir = "Attendance"
    if not os.path.exists(attendance_dir):
        os.makedirs(attendance_dir)

    fileName = attendance_dir + os.sep + "Attendance.csv"
    attendance.to_csv(fileName, index=False)
    
    print("✅ Attendance Successful")
    cam.release()
    cv2.destroyAllWindows()
