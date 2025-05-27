import streamlit as st

st.title("selamat datang di website kaylaazalia")
st.write(
    "ngoding seru bersama kayla"
)
st.image ("E3878D5F-D924-4738-B8BA-7885B70E2018.jpeg", width=200)



st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.writer(f"{angka} adalah Bilangan Genap")
else:
    st.write("{angka} adalah Bilangan Ganjil")
