import pickle
import streamlit as st
import numpy as np
model = pickle.load(open("House_Price_Prection_RVR.sav","rb"))
st.title("SISTEM INFORMASI PREDIKSI HARGA RUMAH")
# luas_tanah = st.number_input("Luas tanah (m2)", placeholder="contoh : 100")
# luas_bangunan = st.number_input("Luas Bangunan (m2)", placeholder="contoh 100")

# jumlah_KM = st.number_input("Jumlah Kamar Mandi", placeholder="contoh : 1")
# jumlah_KT = st.number_input("Jumlah Kamar Tidur", placeholder="contoh : 1")
# jumlah_Garasi = st.number_input("Jumlah Kamar Garasi", placeholder="contoh : 1")

luas_bangunan = st.text_input("Luas Bangunan (m2)", value="100")
luas_tanah = st.text_input("Luas tanah (m2)", value="100")
jumlah_KM = st.number_input("Jumlah Kamar Mandi", min_value=1, step=1, format='%d')
jumlah_KT = st.number_input("Jumlah Kamar Tidur", min_value=1, step=1, format='%d')
jumlah_Garasi = st.number_input("Jumlah Kamar Garasi", min_value=0, step=1, format='%d')
hasil_prediksi  = ""
# LB	LT	KT	KM	GRS

if st.button("Prediksi Harga"): 
    append_data = []
    data = [(luas_bangunan),(luas_tanah), (jumlah_KT), (jumlah_KM), (jumlah_Garasi)]
    append_data = np.array(data).reshape(1, -1)
    hasil_prediksi = model.predict(append_data) 
    st.success(hasil_prediksi)