import cv2  
import numpy as np 
import pyttsx3  

def speak_color(color):
     engine = pyttsx3.init()  
     engine.say(f"You are,,, {color}, student")  
     engine.runAndWait() 

cap = cv2.VideoCapture(0) 


while True: 
    ret, frame = cap.read() 

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    detected_color = None 

    color_ranges = {
    'Second Year': (np.array([40, 40, 40]), np.array([80, 255, 255])),  
    'Fourth Year': (np.array([20, 50, 50]), np.array([40, 255, 255])),
    'Third Year': (np.array([100, 50, 50]), np.array([140, 255, 255])),
    'First Year': (np.array([5, 50, 50]), np.array([15, 255, 255]))
}


    for color, (lower_limit, upper_limit) in color_ranges.items(): 
        mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0: 
            max_contour = max(contours, key=cv2.contourArea) 
            x, y, w, h = cv2.boundingRect(max_contour) 


            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
            if w > 50:
                detected_color = color
                speak_color(color)  
                break  

    if detected_color is not None:
        if detected_color == 'First Year':
            print("You are a First Year Student.")
        elif detected_color == 'Second Year':
            print("You are a Second Year Student.")
        elif detected_color == 'Third Year':
            print("You are a Third Year Student.")
        elif detected_color == 'Fourth Year':
            print("You are a Fourth Year Student.")

    cv2.imshow('ID Year Detector', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()