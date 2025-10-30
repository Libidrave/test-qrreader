import streamlit as st
import cv2
import numpy as np
import pandas as pd

st.title("Test Action UI")

# Komponen untuk mengambil gambar dari kamera
img_file_buffer = st.camera_input("Ambil gambar via webcam atau kamera HP")

try:
    file_wo = pd.read_csv('./dummy_wo.csv', encoding='utf-8')
except FileNotFoundError:
    st.error("File dummy_wo.csv tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.")
    st.stop()

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    st.image(cv2_img, channels="BGR", caption="Gambar yang Diambil")

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    if data:
        st.success(f"QR Code terdeteksi: {data}")
        
        wo_number_to_find = data
        result_df = file_wo[file_wo['WO Number'] == wo_number_to_find]

        if not result_df.empty:
            st.subheader("Detail WO Ditemukan:")
            st.dataframe(result_df)
        else:
            st.error(f"Nomor WO '{wo_number_to_find}' tidak ditemukan dalam file dummy_wo.csv.")
    else:
        st.warning("Tidak ada QR Code yang terdeteksi pada gambar.")
