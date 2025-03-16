import os  # Accessing OS functions
import check_camera
import Capture_Image
import Train_Image
import Recognize

# ----------------------- Title Bar -----------------------
def title_bar():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows: 'cls', Linux/macOS: 'clear'
    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")

# --------------------- Main Menu ------------------------
def mainMenu():
    while True:  # Keep looping until user exits
        title_bar()
        print()
        print(10 * "*", "WELCOME MENU", 10 * "*")
        print("[1] Check Camera")
        print("[2] Capture Faces")
        print("[3] Train Images")
        print("[4] Recognize & Attendance")
        print("[5] Quit")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                checkCamera()
            elif choice == 2:
                CaptureFaces()
            elif choice == 3:
                TrainImages()
            elif choice == 4:
                RecognizeFaces()
            elif choice == 5:
                print("Thank You for using the system!")
                exit()  # Exit properly
            else:
                print("⚠️ Invalid Choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("⚠️ Invalid Input! Please enter a valid number.")

# ---------------------- Function Calls -----------------------
def checkCamera():
    check_camera.camer()
    input("\nPress Enter to return to the main menu...")

def CaptureFaces():
    Capture_Image.takeImages()
    input("\nPress Enter to return to the main menu...")

def TrainImages():
    Train_Image.TrainImages()
    input("\nPress Enter to return to the main menu...")

def RecognizeFaces():
    Recognize.recognize_attendence()
    input("\nPress Enter to return to the main menu...")

# ------------------ Main Driver ----------------------
if __name__ == "__main__":
    mainMenu()
