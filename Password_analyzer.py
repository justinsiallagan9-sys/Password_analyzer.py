import streamlit as st
import math
from streamlit_option_menu import option_menu

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator kombinatorika dan analisis password", page_icon="💻")

# Navigasi opsi menu
with st.sidebar :
    st.title("Menu utama")
    selected = option_menu(
       menu_title=None,
       options= ["Menu utama", "Analisis Password", "Kalkulator Kombinatorika"],
       icons=["home", "lock", "calculator"],
       menu_icon="cast",
       default_index=0,
    )
    st.write("---")

#Modul "Menu utama"
if selected == "Menu utama":
    st.title("Selamat datang di aplikasi analisis password")
    st.write("--- Aplikasi berbasis web ini dirancang untuk menguji keamanan sebuah password." \
    "Tujuan aplikasi ini adalah untuk membuktikan bagaimana logika matematika melindungin data pribadi kita")
    st.info("Gunakan opsi disamping untuk mulai menghitung dan menganalisa password")

elif selected == "Kalkulator Kombinatorika":
    st.header("🧮 Kalkulator Kombinatorik")
    st.write("Mari hitung dasar-dasar matematika diskrit di sini.")
    
    tab1, tab2, tab3 = st.tabs(["Faktorial", "Permutasi", "Kombinasi"])
    
    with tab1 :
        n_faktorial = st.number_input("Masukkan nilai n", min_value= 0)
        if st.button("Hitung n"):
            hasil = math.factorial(n_faktorial)
            st.success(f"Nilai faktorial dari {n_faktorial}! adalah {hasil}")
    
    with tab2 :
        n_p = st.number_input("Masukkan total objek (n) ", min_value=0 , key="p1")
        r_p = st.number_input("Masukkan objek yang dipilh (r)", min_value=0, key="p2")
        if st.button("Hitung permutas(P)") :
            if n_p >= r_p :
                st.success(f"Hasil P {n_p}, {r_p} = {math.perm(n_p, r_p)} ")  
            else :
                st.error("n tidak boleh lebih dari r!")

    with tab3 :
        n_c = st.number_input("Masukkan total objek (n):", min_value=0, key="c1")
        r_c = st.number_input("Masukkan objek yang dipilih (r):", min_value=0, key="c2")
        if st.button("Hitung Kombinasi (C)"):
            if n_c >= r_c:
                st.success(f"Hasil C({n_c}, {r_c}) = {math.comb(n_c, r_c)}")
            else:
                st.error("n tidak boleh lebih kecil dari r!")
                
#Modul "Analisa password"
elif selected == "Analisis Password":
    st.title("🔐 Analisis Password")
    st.write("Ketik password di kolom di bawah ini untuk menguji kekuatan password")

    pw = st.text_input("Input passowrd", type="password")

    if pw :
        #menghitung panjang (k)
        panjang_k = len(pw)

        #mengecek jenis karakter (n)
        jenis_n = 0
        if any(c.islower()for c in pw): jenis_n += 26
        if any(c.isupper()for c in pw): jenis_n += 26
        if any(c.isdigit()for c in pw): jenis_n += 10
        if any(not c.isalnum()for c in pw): jenis_n += 32

        #rumus utama : C = n^k
        total_kombinasi = jenis_n ** panjang_k

        #hitung asumsi waktu brute force
        detik = total_kombinasi / 1_000_000_000

        #tampilan hasil
        st.write("---")
        st.subheader("Hasil analisis")

        col1, col2 = st.columns(2)
        col1.metric("Panjang password (k)", f"{panjang_k} karakter ")
        col2.metric("Variasi karakter (n)", f"{jenis_n} jenis")

        st.write("Total kemungkinan kombinasi :")
        st.info(f"{total_kombinasi:,}")

        #konversi waktu sederhana
        if detik > 60:
            hasil_waktu = f"{detik:.2f} Detik"
        elif detik < 315360:
            hasil_waktu = f"{detik/86400:.2f} Hari"
        else :
            hasil_waktu = f"{detik/31536000:.2f} Tahun"

        st.subheader("Estimasi waktu retas: ")
        st.error(hasil_waktu)

        st.write("*Analisa menggunakan rumus matematika $T = n^k/ R$.*")



        

