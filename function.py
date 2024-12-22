import cv2
import mediapipe as mp
import numpy as np

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def draw(layer, last_pos, curr_pos, color, thickness=6):

    """Menggambar garis dari posisi terakhir ke posisi saat ini pada frame video.
    
    Parameters:
        layer (numpy.ndarray): Lapisan pada frame sebagai tempat untuk menggambar.
        last_pos (tuple): Posisi terakhir (x, y).
        curr_pos (tuple): Posisi saat ini (x, y).
        color (tuple): Warna garis dalam format RGB.
        thickness (int): Ketebalan garis.
        
    Returns:
        tuple: Posisi saat ini sebagai posisi terakhir untuk iterasi berikutnya.
    """
    
    # Menggambar garis apabila `last_pos` dan `curr_pos` terdeteksi
    if last_pos is not None and curr_pos is not None:
        cv2.line(layer, last_pos, curr_pos, color, thickness)
    return curr_pos

def change_color(landmarks, curr_color):
    
    """Mengganti warna berdasarkan jarak antara ujung jari manis dan ujung ibu jari.
    
    Parameters:
        landmarks (list): Landmark tangan dari library MediaPipe.
        curr_color (tuple): Warna saat ini.
        
    Returns:
        tuple: Warna baru berdasarkan sentuhan atau jarak antar jari. 
    """
    
    # Mengambil koordinat ujung jari manis dan ujung ibu jari
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    
    # Menghitung jarak antara jari
    distance = np.sqrt((thumb_tip.x - ring_finger_tip.x) ** 2 + (thumb_tip.y - ring_finger_tip.y) ** 2)
    
    # Mengubah warna jika jarak ujung jari dibawah `0.05`
    if distance < 0.05:
        if curr_color == (255, 255, 255):  # Putih
            return (255, 0, 0)  # Merah
        elif curr_color == (255, 0, 0):  # Merah
            return (0, 255, 0)  # Hijau
        elif curr_color == (0, 255, 0):  # Hijau
            return (0, 0, 255)  # Biru
        else:
            return (255, 255, 255)  # Kembali ke putih
    return curr_color