import csv
import cv2
import os
import numpy as np


# Check if input is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# Take image function
def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")
    lastname = input("Enter Your Last Name: ")

    if Id.isdigit() and name.isalpha():
        cam = cv2.VideoCapture(0)
        cascadePath = (r"D:\\work\\FRAS\\FRAS\\haarcascade_frontalface_default (1).xml")
        detector = cv2.CascadeClassifier(cascadePath)
        sampleNum = 0

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                cv2.imwrite("TrainingImage" + os.sep + f"{name}.{Id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
                cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum > 60:
                break

        cam.release()
        cv2.destroyAllWindows()
        print(f"✅ Images Saved for ID: {Id}, Name: {name}, Lastname: {lastname}")

        row = [Id, name, lastname]

        # Ensure the "StudentDetails" directory exists
        directory = "StudentDetails"
        if not os.path.exists(directory):
            os.makedirs(directory)  # ✅ Creates the folder if missing

        # Define csv file path correctly
        csv_file_path = os.path.join(directory, "StudentDetails.csv")

        # Check if the CSV file exists
        file_exists = os.path.isfile(csv_file_path)

        # Open the CSV file and write data
        with open(csv_file_path, 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            if not file_exists:
                writer.writerow(["ID", "Name", "Lastname"])  # ✅ Add header if file is new
            writer.writerow(row)

    else:
        if not Id.isdigit():
            print("⚠️ Enter a valid numeric ID")
        if not name.isalpha():
            print("⚠️ Enter a valid alphabetical Name")
