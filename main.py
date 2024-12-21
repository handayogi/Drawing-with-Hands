import cv2
import mediapipe as mp
import numpy as np
from function import mp_drawing, draw

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.2)

def main():
    last_pos = None
    curr_color = (255, 255, 255)
    
    # Program akan membuka kamera
    cap = cv2.VideoCapture(1)
    _, frame = cap.read()
    graff_layer = np.zeros_like(frame, dtype=np.uint8)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Konversi frame ke RGB untuk MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        # Memproses setiap tangan yang terdeteksi berdasarkan setiap fungsi yang sudah dibuat
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                # Mengambil koordinat ujung jari telunjuk
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, _ = frame.shape
                curr_pos = (int(index_finger_tip.x * w), int(index_finger_tip.y * h))
                
                # Fungsi untuk menggambar
                last_pos = draw(graff_layer, last_pos, curr_pos, curr_color)
                
                # Menggambar landmark tangan
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        else:
            # Reset posisi terakhir jika tidak ada tangan terdeteksi
            last_pos = None
            
        # Menggabungkan frame asli dan layer gambar
        output = cv2.addWeighted(frame, 0.8, graff_layer, 0.5, 0)
        cv2.imshow('Drawing with Hands', output)
        
        # Program akan berhenti jika menekan tombol 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()