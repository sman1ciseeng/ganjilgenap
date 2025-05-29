import streamlit as st

st.title("Aplikasi Gugun Men")

angka = st.number_input("Masukkan sebuah angka", step=1)

if st.button("Cek"):

    if angka % 2 == 0:
        st.success(f"{angka} Adalah Bilanga Genap")
    else:
        st.warning(f"{angka} Adalah Bilanga Ganjil")
    

