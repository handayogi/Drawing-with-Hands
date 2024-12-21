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