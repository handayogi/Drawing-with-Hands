import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c =img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 8 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 12 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 16 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 20 :
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    cv2.imshow("Hand Landmarks", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()