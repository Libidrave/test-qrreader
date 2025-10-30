import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Action UI Test")

# Komponen untuk mengambil gambar dari kamera
img_file_buffer = st.camera_input("Ambil gambar via webcam atau kamera HP")

if img_file_buffer is not None:
    # Membaca data gambar
    bytes_data = img_file_buffer.getvalue()
    # Mengubah data byte menjadi array numpy
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Menampilkan gambar yang diambil
    st.image(cv2_img, channels="BGR", caption="Gambar yang Diambil")

    # Inisialisasi QRCodeDetector
    detector = cv2.QRCodeDetector()

    # Mendeteksi dan mendekode QR code
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    # Menampilkan hasil jika QR code ditemukan
    if data:
        st.success(f"QR Code terdeteksi: {data}")
    else:
        st.warning("Tidak ada QR Code yang terdeteksi pada gambar.")
