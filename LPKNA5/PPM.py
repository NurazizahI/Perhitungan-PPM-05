import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Perhitungan PPM',
    ['Hitung Nilai PPM',
    'Hitung Nilai PPM Kesadahan Total'],
    default_index=0)
    
    #halaman hitung Nilai PPM
    if (selected == 'Hitung Nilai PPM'):
    st.title('Hitung Nilai PPM')
    
    Nilai Massa Zat Terlarut(mg) = st.number_input("Masukan Nilai Massa Zat Terlarut(mg)",0)
    Nilai Volume Larutan (L) = st.number_input("Masukan Nilai Volume Larutan (L)",0)
    Hitung = st.button ("Hitung Nilai PPM")
    
    if hitung :
        Hitung Nilai PPM = Nilai Massa Zat Terlarut(mg)/Nilai Volume Larutan (L)
        st.write ("Hitung Nilai PPM Adalah = ", Hitung Nilai PPM)
        st.success (f "Hitung Nilai PPM Adalah = {Hitung Nilai PPM} mg/L")
        
    #halaman hitung Nilai PPM Kesadahan Total
    if (selected == 'Hitung Nilai PPM Kesadahan Total'):
    st.title('Hitung Nilai PPM Kesadahan Total')
    
    Nilai Molaritas Titran (mmol/ml) = st.number_input("Masukan Nilai Molaritas Titran (mmol/ml)",0)
    Nilai Volume Titran (ml) = st.number_input("Masukan Nilai Volume Larutan (ml)",0)
    Nilai BM (mg/mmol) = st.number_input("Masukan Nilai BM (mg/mmol)",0)
    Nilai Volume Sampel (L) = st.number_input("Masukan Nilai Volume Sampel (L)",0)
    Hitung = st.button ("Hitung Nilai PPM Kesadahan Total")
    
    if hitung :
        Hitung Nilai PPM Kesadahan Total = (Nilai Molaritas Titran (mmol/ml)*Nilai Volume Titran (ml)*Nilai BM (mg/mmol))/Nilai Volume               Sampel (L)
        st.write ("Hitung Nilai PPM Kesadahan Total Adalah = ", Hitung Nilai PPM Kesadahan Total)
        st.success (f "Hitung Nilai PPM Kesadahan Total Adalah = {Hitung Nilai PPM Kesadahan Total} mg/L")